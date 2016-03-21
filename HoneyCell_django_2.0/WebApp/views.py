from django.shortcuts import render

# allow us to redirect
from django.shortcuts import redirect
from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.http import HttpResponse
from django.template import RequestContext, loader

# import the User class in models.py
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

# import the auth.models User
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from WebApp.models import *

# registration is normal route, and login is login is "django.contrib.views.login"
def registration(request):
    errors = []
    context = {}
    if request.method == "GET":
        return render(request, 'WebApp/register.html', context)

    # add 'errors' attribute to the context
    context['errors'] = errors

    password1 = request.POST['password']
    password2 = request.POST['password_confirmation']

    if password1 != password2:

        print("Passwords did not match.")

        # error1 happens
        errors.append("Passwords did not match.")

    if len(User.objects.all().filter(username = request.POST['user_name'])) > 0:
        print("Username is already taken.")

        # error2 happens
        errors.append("Username is already taken.")

    if len(User.objects.all().filter(email = request.POST['email'])):
        print("The email already register.")

        errors.append("The email already register.")

    if errors:
        return render(request, 'WebApp/register.html', context)

    # create a new user from the valid form data, using create_user function with 2 arguments, 'username' and 'password'
    new_user = User.objects.create_user(username=request.POST['user_name'],
                                        password=request.POST['password'],
                                        first_name=request.POST['first_name'],
                                        last_name=request.POST['last_name'],
                                        email=request.POST['email'])
    new_user.save()

    # using 'authenticate' function
    new_user = authenticate(username = request.POST['user_name'],
                            password = request.POST['password'],)

    new_activity_instance = Activity(user=new_user)
    new_activity_instance.description = new_user.username + " register an account."
    new_activity_instance.save()

    # create Profile object for the user
    new_profile_instance = Profile(user=new_user,
                                   )
    new_profile_instance.save()

    # create default folder
    new_folder_instance = Folder(user=new_user,
                                 folder_name="Default",
                                 folder_description="This is default folder.",
                                 )
    new_folder_instance.save()
    print("Already save new_folder_instance.")

    # create three default labels at first.
    new_label_important_instance = Label(user=new_user,
                                        label_name="Important",
                                        label_description="This task is important.",
                                        )
    new_label_important_instance.save()
    print("Already save new_label_important_instance.")
    new_label_warning_instance = Label(user=new_user,
                                       label_name="Warning",
                                       label_description="This task is warning.")
    new_label_warning_instance.save()
    print("Already save new_label_warning_instance.")
    new_label_information_instance = Label(user=new_user,
                                           label_name="Information",
                                           label_description="This task is information.")
    new_label_information_instance.save()
    print("Already save new_label_information_instance.")

    # using 'login' function
    login(request, new_user)

    # using 'redirect' function
    return redirect(reverse('index'))

# def logout view
def my_logout(request):
    logout(request)
    return redirect(reverse('index'))

@login_required
def index(request):
    print("in the index function")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/index.html', context)

@login_required
def newTask(request):
    print("in the newTask function")
    context = {}
    user = request.user
    context['user'] = user

    folders = Folder.objects.filter(user=user)
    context['folders'] = folders

    labels = Label.objects.filter(user=user)
    context['labels'] = labels

    return render(request, 'WebApp/newTask.html', context)

@login_required
def historyTask(request):
    print("in the historyTask function")
    context = {}
    user = request.user
    context['user'] = user

    tasks = Task.objects.filter(user=request.user)
    context['tasks'] = tasks

    return render(request, 'WebApp/historyTask.html', context)

@login_required
def fileManage(request):
    print("in the fileManage function")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/fileManage.html', context)

@login_required
def fileManage_tasks(request):
    print("in the fileManage_tasks function")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/fileManage_tasks.html', context)


@login_required
def profile(request):
    print("in the profile function")
    context = {}
    user = request.user
    context['user'] = user

    # check own profile
    context['self'] = True

    profile = Profile.objects.get(user=user)
    context['profile'] = profile

    number_of_followers = len(Followship.objects.filter(follower=request.user))
    number_of_followings = len(Followship.objects.filter(following=request.user))

    context['number_of_followers'] = number_of_followers
    context['number_of_followings'] = number_of_followings

    return render(request, 'WebApp/profile.html', context)

from WebApp.forms import *
from django.utils import timezone

@login_required
def create_new_task(request):
    print("in the create_new_task function")

    context = {}
    context['user'] = request.user

    errors = []
    context['errors'] = errors

    print(request.user)
    print(request.POST['task_name'])
    print(request.POST['task_description'])
    print(request.POST['task_folder'])
    print(request.POST['task_label'])
    print(request.FILES['docfile'])

    user = request.user
    task_name = request.POST['task_name']
    task_description = request.POST['task_description']
    task_folder = request.POST['task_folder']
    task_label = request.POST['task_label']
    docfile = request.FILES['docfile']

    task_folder_object = Folder.objects.get(user=request.user, folder_name=task_folder)
    task_label_object = Label.objects.get(user=request.user, label_name=task_label)

    context['user'] = user
    context['task_name'] = task_name
    context['task_description'] = task_description
    context['task_folder'] = task_folder
    context['task_label'] = task_label
    context['docfile'] = docfile
    folders = Folder.objects.filter(user=user)
    context['folders'] = folders

    labels = Label.objects.filter(user=user)
    context['labels'] = labels

    if not task_name:
        errors.append("Please type in the task name.")

        return render(request, 'WebApp/newTask.html', context)

    if not task_description:
        errors.append('Please type in the task description.')

        return render(request, 'WebApp/newTask.html', context)

    if not docfile:
        errors.append("Please upload a file for the task.")

        return render(request, 'WebApp/newTask.html', context)

    if len(Task.objects.filter(user=user, task_name=task_name)):
        print("The task_name for this user already exist.")
        errors.append("The task_name for this user already exist.")

        return render(request, 'WebApp/newTask.html', context)

    new_task_instance = Task(user=user,
                             task_name=task_name,
                             task_description=task_description,
                             task_label=task_label_object,
                             task_folder=task_folder_object,
                             docfile=docfile)
    new_task_instance.save()
    print("Already save the new_task_instance.")

    new_activity_instance = Activity(user=request.user)
    new_activity_instance.description = "Create a new task name: " + new_task_instance.task_name
    new_activity_instance.save()

    print("Already save new_activity_instance.")

    return HttpResponseRedirect(reverse('newTask'))

@login_required
def guide(request):
    print("in the guide function")
    return render(request, 'WebApp/guide.html')

@login_required
def settings(request):
    print("in the settings function")
    context = {}
    user = request.user
    context['user'] = user

    profile = Profile.objects.get(user=request.user)
    context['profile'] = profile

    return render(request, 'WebApp/settings.html', context)


@login_required
def global_page(request):
    print("in the global function.")
    context = {}
    user = request.user
    context['user'] = user

    activities = Activity.objects.all()
    context['activities'] = activities

    return render(request, 'WebApp/global_page.html', context)


@login_required
def other_user(request, user_id):
    print("in the other_user function.")
    print(request)
    print(user_id)
    context = {}
    context['user'] = request.user
    other_user = User.objects.get(id=user_id)
    context['other_user'] = other_user

    if len(Followship.objects.filter(following=request.user,
                                     follower=other_user)):
        is_followed = True
        context['is_followed'] = is_followed
    else:
        is_followed = False
        context['is_followed'] = is_followed

    return render(request, 'WebApp/other_user.html', context)



@login_required
def follow(request, user_id):
    print("in the follow function.")

    print("*" * 30)

    print(request)
    print(user_id)

    context = {}
    context['current_user'] = request.user

    errors = []
    context['errors'] = errors

    other_user = User.objects.get(id=user_id)

    if Followship.objects.filter(following=request.user,
                                 follower=other_user):
        errors.append("The followship already exist.")

        return HttpResponseRedirect(reverse('global_page'))

    new_followship_instance = Followship(following=request.user,
                                         follower=other_user)
    new_followship_instance.save()
    print("Already save new_followship_instance.")

    return HttpResponseRedirect(reverse("other_user", kwargs={'user_id': other_user.id}))

@login_required
def unfollow(request, user_id):
    print("in the unfollow function.")

    print(request)
    print(user_id)

    context = {}
    context['current_user'] = request.user

    other_user = User.objects.get(id=user_id)

    followship = Followship.objects.get(following=request.user,
                                        follower=other_user)
    followship.delete()
    print("The Followship object already delete.")

    return HttpResponseRedirect(reverse("other_user", kwargs={'user_id': other_user.id}))


from django.http import Http404
from mimetypes import guess_type

# get back the user picture
@login_required
def get_user_picture(request, user_id):
    print("in the get_user_picture function.")
    context = {}
    errors = []
    context['errors'] = errors
    try:
        user = User.objects.get(id=user_id)
        profile = Profile.objects.get(user=user)
    except Exception:
        errors.append("profile not existed")
    content_type = guess_type(profile.image.name)
    return HttpResponse(profile.image, content_type=content_type)




@login_required
def update_profile(request):
    print("in the update_profile function.")
    context = {}
    errors = []
    context['errors'] = errors

    context['user'] = request.user
    profile = Profile.objects.get(user=request.user)

    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    company = request.POST['company']
    location = request.POST['location']
    website = request.POST['website']

    request.user.first_name = first_name
    request.user.last_name = last_name
    request.user.email = email

    profile.company = company
    profile.location = location
    profile.website = website

    profile.save()
    print("Already update the profile.")

    return HttpResponseRedirect(reverse('profile'))




@login_required
def taskDetail(request):
    print("in the taskDetail function")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/taskDetail.html', context)