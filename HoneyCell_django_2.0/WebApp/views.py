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
                                 )
    new_folder_instance.save()
    print("Already save new_folder_instance.")

    # create four default labels at first.
    new_label_none_instance = Label(user=new_user,
                                    label_name="None",
                                    label_description="This label is None."
                                    )
    new_label_none_instance.save()
    print("Already save new_label_none_instance.")
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

    new_status_completed_instance = Status(user=new_user,
                                           status_name="Completed",
                                           status_description="This task is completed.")
    new_status_completed_instance.save()
    print("Already save new_status_completed_instance.")
    new_status_pending_instance = Status(user=new_user,
                                           status_name="Pending",
                                           status_description="This task is pending.")
    new_status_pending_instance.save()
    print("Already save new_status_pending_instance.")
    new_status_denied_instance = Status(user=new_user,
                                           status_name="Denied",
                                           status_description="This task is denied.")
    new_status_denied_instance.save()
    print("Already save new_status_denied_instance.")

    new_algorithm_KNN_instance = Algorithm(user=new_user,
                                       algorithm_name="KNN",
                                       algorithm_description="This is KNN algorithm.")
    new_algorithm_KNN_instance.save()
    print("Already save new_algorithm_KNN_instance.")

    new_algorithm_linear_regression_instance = Algorithm(user=new_user,
                                                         algorithm_name="Linear regression",
                                                         algorithm_description="This is linear regression algorithm.")
    new_algorithm_linear_regression_instance.save()
    print("Already save new_algorithm_linear_regression_instance.")

    new_algorithm_decision_tree_instance = Algorithm(user=new_user,
                                                     algorithm_name="Decision tree",
                                                     algorithm_description="This is decision tree algorithm.")
    new_algorithm_decision_tree_instance.save()
    print("Already save new_algorithm_decision_tree_instance.")

    new_algorithm_neural_network_instance = Algorithm(user=new_user,
                                                      algorithm_name="Neural network",
                                                      algorithm_description="This is neural network algorithm.")
    new_algorithm_neural_network_instance.save()
    print("Already save new_algorithm_neural_network_instance.")




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

    algorithms = Algorithm.objects.filter(user=user)
    context['algorithms'] = algorithms

    return render(request, 'WebApp/newTask.html', context)


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def historyTask(request):
    print("in the historyTask function")
    context = {}
    user = request.user
    context['user'] = user

    tasks = Task.objects.filter(user=request.user)

    paginator = Paginator(tasks, 3)
    page = request.GET.get('page')

    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)

    context['tasks'] = tasks

    return render(request, 'WebApp/historyTask.html', context)

@login_required
def fileManage(request):
    print("in the fileManage function")
    context = {}
    user = request.user
    context['user'] = user

    all_folders = Folder.objects.filter(user=request.user)
    context['all_folders'] = all_folders

    folders = Folder.objects.filter(user=request.user)
    paginator = Paginator(folders, 3)
    page = request.GET.get('page')
    try:
        folders = paginator.page(page)
    except PageNotAnInteger:
        folders = paginator.page(1)
    except EmptyPage:
        folders = paginator.page(paginator.num_pages)
    context['folders'] = folders

    print("%" * 30)
    print(folders)
    for folder in folders:
        print(folder)
        print(folder.folder_name)
        print(folder.id)
        print("*" * 10)
    print("%" * 30)

    return render(request, 'WebApp/fileManage.html', context)

@login_required
def fileManage_tasks(request, folder_id):
    print("in the fileManage_tasks function")
    context = {}
    user = request.user
    context['user'] = user

    folders = Folder.objects.filter(user=request.user)
    context['folders'] = folders

    folder = Folder.objects.get(id=folder_id)
    context['folder'] = folder

    tasks = Task.objects.filter(task_folder=folder)
    paginator = Paginator(tasks, 3)
    page = request.GET.get('page')

    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)
    context['tasks'] = tasks

    return render(request, 'WebApp/fileManage_tasks.html', context)




@login_required
def profile_allFollowers(request):
    print("in the profile_allFollowers function.")
    context = {}
    user = request.user
    context['user'] = user

    activities = Activity.objects.all()
    context['activities'] = activities

    return render(request, 'WebApp/profile_allFollowers.html', context)

@login_required
def profile_allFollowings(request):
    print("in the profile_allFollowings function.")
    context = {}
    user = request.user
    context['user'] = user

    activities = Activity.objects.all()
    context['activities'] = activities

    return render(request, 'WebApp/profile_allFollowings.html', context)



from WebApp.forms import *
from django.utils import timezone

@login_required
def create_new_task(request):
    print("in the create_new_task function")

    context = {}
    context['user'] = request.user

    errors = []
    context['errors'] = errors

    user = request.user
    task_name = request.POST['task_name']
    task_algorithm = request.POST['task_algorithm']
    task_description = request.POST['task_description']
    task_folder = request.POST['task_folder']
    task_label = request.POST['task_label']
    docfile = request.FILES['docfile']
    task_folder_object = Folder.objects.get(user=request.user, folder_name=task_folder)



    context['user'] = user
    context['task_name'] = task_name
    context['task_algorithm'] = task_algorithm
    context['task_description'] = task_description
    context['task_folder'] = task_folder
    context['task_label'] = task_label
    context['docfile'] = docfile
    context['folders'] = Folder.objects.filter(user=request.user)
    context['labels'] = Label.objects.filter(user=user)
    context['algorithms'] = Algorithm.objects.filter(user=request.user)
    context['labels'] = Label.objects.filter(user=request.user)

    if not task_name:
        errors.append("Please type in the task name.")

    if not docfile:
        errors.append("Please upload a file for the task.")

    if len(Task.objects.filter(user=user, task_name=task_name)):
        errors.append("The task_name for this user already exist.")

    # Do not select a task algorithm
    if task_algorithm == "None":
        errors.append("Please select the task algorithm.")

    if errors:
        return render(request, 'WebApp/newTask.html', context)

    task_label_object = Label.objects.get(user=request.user, label_name=task_label)
    task_algorithm_object = Algorithm.objects.get(user=request.user, algorithm_name=task_algorithm)


    new_task_instance = Task(user=user,
                             task_name=task_name,
                             task_algorithm = task_algorithm_object,
                             task_description=task_description,
                             task_label=task_label_object,
                             task_folder=task_folder_object,
                             docfile=docfile,
                             # default status is pending
                             task_status=Status.objects.get(user=request.user, status_name="Pending"))

    new_task_instance.save()
    print("Already save the new_task_instance.")

    print(new_task_instance)

    new_activity_instance = Activity(user=request.user,
                                     task=new_task_instance,
                                     )
    new_activity_instance.description = "Create a new task name: " + new_task_instance.task_name
    new_activity_instance.save()
    print("Already save new_activity_instance.")

    # return HttpResponseRedirect(reverse('newTask'))

    return HttpResponseRedirect(reverse('taskDetail', kwargs={'task_id': new_task_instance.id}))


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

    context['public_profile'] = True
    context['password'] = False

    return render(request, 'WebApp/settings.html', context)


@login_required
def global_page(request):
    print("in the global function.")
    context = {}
    user = request.user

    users = User.objects.all()
    context['users'] = users

    activities = Activity.objects.all()
    context['activities'] = activities

    print("%" * 30)
    for activity in activities:
        print(activity.description)
        comments = Comment.objects.filter(activity=activity)
        print(activity.comment_set.all())
        print(comments)
    print("%" * 30)

    print("%" * 30)
    print(Comment.objects.all())
    for comment in Comment.objects.all():
        print(comment.user)
        print(comment.activity.description)
        print(comment.text)
    print("%" * 30)


    return render(request, 'WebApp/global_page.html', context)


# @login_required
# def other_user(request, user_id):
#     print("in the other_user function.")
#     print(request)
#     print(user_id)
#     context = {}
#     context['user'] = request.user
#     other_user = User.objects.get(id=user_id)
#     context['other_user'] = other_user
#
#     if len(Followship.objects.filter(following=request.user,
#                                      follower=other_user)):
#         is_followed = True
#         context['is_followed'] = is_followed
#     else:
#         is_followed = False
#         context['is_followed'] = is_followed
#
#     return render(request, 'WebApp/other_user.html', context)



@login_required
def follow(request, user_id):
    print("in the follow function.")

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

    return HttpResponseRedirect(reverse("other_profile", kwargs={'user_id': other_user.id}))

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

    return HttpResponseRedirect(reverse("other_profile", kwargs={'user_id': other_user.id}))


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
def change_password(request):
    print("in the change_password function.")
    context = {}

    user = request.user
    context['user'] = user

    errors = []
    context['errors'] = errors

    new_password1 = request.POST['new_password1']
    new_password2 = request.POST['new_password2']

    print("%" * 30)
    print(request.user.password)
    print(new_password1)
    print(new_password2)
    print("%" * 30)

    if new_password1 != new_password2:
        errors.append("Two password did not match, please type in again.")
        context['public_profile'] = False
        context['password'] = True
        return render(request, 'WebApp/settings.html', context)
    else:
        user.set_password(new_password1)
        user.save()
        print("Already reset the password.")
        user = authenticate(username = user.username,
                            password = new_password1,)
        login(request, user)
        return HttpResponseRedirect(reverse('settings'))


@login_required
def taskDetail(request, task_id):
    print("in the taskDetail function")
    context = {}
    user = request.user
    context['user'] = user

    task = Task.objects.get(id=task_id)
    context['task'] = task

    print(task)


    return render(request, 'WebApp/taskDetail.html', context)




@login_required
def update_task(request, task_id):
    print("in the update_task function.")
    context = {}
    context['user'] = request.user

    errors = []
    context['errors'] = errors

    task = Task.objects.get(id=task_id)
    context['task'] = task

    task_name = request.POST['task_name']
    task_description = request.POST['task_description']


    if ( task.task_name != task_name and len(Task.objects.filter(task_name=task_name))):
        # The way to return back the error message needs to be changed later
        errors.append("The task name already exist, please type in another task name.")
        print("The task name already exist, please type in another task name.")
        return HttpResponseRedirect(reverse('taskDetail', kwargs={'task_id': task_id}))


    if ( task.task_description != task_description and len(Task.objects.filter(task_description=task_description)) ):
        # The way to return back the error message needs to be changed later
        errors.append("The task description already exist, please type in another task description.")
        print("The task description already exist, please type in another task description.")
        return HttpResponseRedirect(reverse('taskDetail', kwargs={'task_id': task_id}))

    task.task_name = task_name
    task.task_description = task_description
    task.save()
    print("Already update task's information.")

    return HttpResponseRedirect(reverse('taskDetail', kwargs={'task_id': task_id}))



@login_required
def new_folder(request):
    print("in the new_folder function.")

    context = {}
    context['user'] = request.user

    errors = []
    context['errors'] = errors

    folder_name = request.POST['folder_name']

    if(Folder.objects.filter(folder_name=folder_name)):
        # The way to return back the error message needs to be changed later
        errors.append("This folder name already exist, please type in another folder name.")
        print("This folder name already exist, please type in another folder name.")
        return HttpResponseRedirect(reverse('fileManage'))

    new_folder_instance = Folder(user=request.user,
                                 folder_name=folder_name)
    new_folder_instance.save()
    print("Already save the new_folder_instance.")

    return HttpResponseRedirect(reverse('fileManage'))



@login_required
def update_folder(request, folder_id):
    print("in the update_folder function.")
    print("folder_id: " + folder_id);
    context = {}
    context['user'] = request.user

    errors = []
    context['errors'] = errors

    folder = Folder.objects.get(id=folder_id)

    folder_name = request.POST['folder_name']
    # folder_description = request.POST['folder_description']

    if ( (folder.folder_name != folder_name) and len(Folder.objects.filter(folder_name=folder_name)) ):
        # The way to return back the error message needs to be changed later
        errors.append("The folder name already exists, please type in another folder name.")
        print("The folder name already exists, please type in another folder name.")
        return HttpResponseRedirect(reverse('fileManage'))


    # if ( (folder.folder_description != folder_description) and len(Folder.objects.filter(folder_description=folder_description)) ):
        # The way to return back the error message needs to be changed later
        # errors.append("The folder description already exists, please type in another folder description.")
        # print("The folder description already exists, please type in another folder description.")
        # return HttpResponseRedirect(reverse('fileManage'))

    folder.folder_name = folder_name
    # folder.folder_description = folder_description
    folder.save()
    print("Already update folder's information")

    return HttpResponseRedirect(reverse('fileManage'))



@login_required
def delete_folder(request, folder_id):
    print("in the delete_folder function.")
    context = {}
    context['user'] = request.user

    folder = Folder.objects.get(id=folder_id)
    context['folder'] = folder

    tasks_inside_folder = Task.objects.filter(task_folder=folder)

    for task in tasks_inside_folder:
        task.delete()
        print("Successfully delete one task inside folder.")

    folder.delete()
    print("Successfully delete the folder.")

    return HttpResponseRedirect(reverse('fileManage'))


@login_required
def important_tasks(request):
    print("in the important_tasks function.")
    context = {}
    context['user'] = request.user

    context['important_label'] = True

    task_label_important = Label.objects.get(user=request.user, label_name="Important")
    context['label'] = task_label_important

    tasks = Task.objects.filter(user=request.user, task_label=task_label_important)
    paginator = Paginator(tasks, 3)
    page = request.GET.get('page')
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)
    context['tasks'] = tasks

    return render(request, 'WebApp/label_task.html', context)


@login_required
def warning_tasks(request):
    print("in the warning_tasks function.")
    context = {}
    context['user'] = request.user

    context['warning_label'] = True

    task_label_warning = Label.objects.get(user=request.user, label_name="Warning")
    context['label'] = task_label_warning

    tasks = Task.objects.filter(user=request.user, task_label=task_label_warning)
    paginator = Paginator(tasks, 3)
    page = request.GET.get('page')
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)
    context['tasks'] = tasks

    return render(request, 'WebApp/label_task.html', context)



@login_required
def information_tasks(request):
    print("in the information_tasks function.")
    context = {}
    context['user'] = request.user

    context['information_label'] = True

    task_label_information = Label.objects.get(user=request.user, label_name="Information")
    context['label'] = task_label_information

    tasks = Task.objects.filter(user=request.user, task_label=task_label_information)
    paginator = Paginator(tasks, 3)
    page = request.GET.get('page')
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)
    context['tasks'] = tasks

    return render(request, 'WebApp/label_task.html', context)




@login_required
def followers(request):
    print("in the followers function.")
    context = {}
    context['user'] = request.user

    followers = Followship.objects.filter(following=request.user)
    context['followers'] = followers


    return render(request, 'WebApp/profile_allFollowers.html', context)



@login_required
def followings(request):
    print("in the followings function.")
    context = {}
    context['user'] = request.user

    followings = Followship.objects.filter(follower=request.user)
    context['followings'] = followings

    return render(request, 'WebApp/profile_allFollowings.html', context)



def task_finished(request):
    print("in the task_finished function.")

    return render(request, 'WebApp/index.html', {})


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


@login_required
def other_profile(request, user_id):
    print("in the other_profile function.")
    context = {}
    context['user'] = request.user

    other_user = User.objects.get(id=user_id)

    if(request.user == other_user):
        print("Enter myself profile page.")

        # check own profile
        context['self'] = True

        profile = Profile.objects.get(user=request.user)
        context['profile'] = profile

        number_of_followers = len(Followship.objects.filter(follower=request.user))
        number_of_followings = len(Followship.objects.filter(following=request.user))

        context['number_of_followers'] = number_of_followers
        context['number_of_followings'] = number_of_followings

        return render(request, 'WebApp/profile.html', context)

    else:
        print("Enter others' profile page.")
        context['other_user'] = other_user

        # check own profile
        context['self'] = False

        other_profile = Profile.objects.get(user=other_user)
        context['other_profile'] = other_profile

        number_of_followers = len(Followship.objects.filter(follower=other_user))
        number_of_followings = len(Followship.objects.filter(following=other_user))

        context['number_of_followers'] = number_of_followers
        context['number_of_followings'] = number_of_followings


        if len(Followship.objects.filter(following=request.user,
                                         follower=other_user)):
            is_followed = True
            context['is_followed'] = is_followed
            print("is_followed equals to true.")
        else:
            is_followed = False
            context['is_followed'] = is_followed
            print("is_followed equals to false.")

        return render(request, 'WebApp/other_profile.html', context)


@login_required
def add_comment(request, activity_id):
    print("in the add_comment function.")
    context = {};

    print("%" * 30)
    print(request)
    print(activity_id)
    print("%" * 30)

    user = request.user
    context['user'] = user

    activity = Activity.objects.get(id=activity_id)

    comment_text = request.POST['comment_text']

    new_comment_instance = Comment(user=user,
                                   activity=activity,
                                   text=comment_text)
    new_comment_instance.save()
    print("Successfully save new_comment_instance.")


    return HttpResponseRedirect(reverse('global_page'))


def task_finished_ajax_check_database(request):
    context = {}
    if request.user:
      context['user'] = request.user

    try: 
      if request.method == "GET":
        print("in post")
        curr_username = request.GET.get("username")
        # print curr_username

        curr_user = User.objects.get(username = curr_username)

        # print curr_user

        task_status = Status.objects.get(user=curr_user, status_name="Pending")

        completed_tasks = Task.objects.filter(user=curr_user, task_status = task_status)

        print completed_tasks




        return HttpResponse(completed_tasks)

    except ObjectDoesNotExist:
      context['errors'] = ["task_finished_popup fail"]

    return HttpResponse()








