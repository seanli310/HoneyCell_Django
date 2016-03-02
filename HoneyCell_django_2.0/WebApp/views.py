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

    if errors:
        return render(request, 'WebApp/register.html', context)

    # create a new user from the valid form data, using create_user function with 2 arguments, 'username' and 'password'
    new_user = User.objects.create_user(username=request.POST['user_name'], password=request.POST['password'], first_name=request.POST['first_name'], last_name=request.POST['last_name'])
    new_user.save()

    # using 'authenticate' function
    new_user = authenticate(username = request.POST['user_name'], password = request.POST['password'])

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
    return render(request, 'WebApp/newTask.html', context)

@login_required
def historyTask(request):
    print("in the historyTask function")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/historyTask.html', context)


@login_required
def profile(request):
    print("in the profile function")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/profile.html', context)

from WebApp.forms import *
from django.utils import timezone

@login_required
def create_new_task(request):
    print("in the create_new_task function")

    errors = []
    context = {}

    context['user'] = request.user

    print(request.user)
    print(request.POST['task_name'])
    print(request.POST['task_description'])
    print(request.POST['task_folder'])
    print(request.POST['task_label'])

    print(timezone.now().date().year)
    print(timezone.now().date().month)
    print(timezone.now().date().day)


    form = DocumentForm(request.POST, request.FILES)
    print(form)
    if form.is_valid():
        print("The form is valid.")
        new_task_instance = Document(user = request.user,
                                     name=request.POST['task_name'],
                                     description=request.POST['task_description'],
                                     folder=request.POST['task_folder'],
                                     label=request.POST['task_label'],
                                     docfile=request.FILES['docfile'])
        new_task_instance.save()
        print("already save the new_task_instance.")
        return HttpResponseRedirect(reverse('newTask'))
    else:
        print("The form is not valid.")

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
    return render(request, 'WebApp/settings.html', context)


@login_required
def global_page(request):
    print("in the global function.")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/global_page.html', context)


@login_required
def follow(request, user_id):
    print("in the follow function.")

    print("*" * 30)

    print(request)
    print(user_id)

    context = {}
    context['current_user'] = request.user

    selected_user = User.objects.get(id=user_id)

    new_followship_instance = Followship(following=request.user,
                                         follower=selected_user)
    new_followship_instance.save()
    print("Already save new_followship_instance.")

    return HttpResponseRedirect(reverse("show_users"))


@login_required
def unfollow(request, user_id):
    print("in the unfollow function.")

    print(request)
    print(user_id)

    context = {}
    context['current_user'] = request.user

    selected_user = User.objects.get(id=user_id)

    followship = Followship.objects.get(following=request.user,
                                        follower=selected_user)
    followship.delete()
    print("The Followship object already delete.")

    return HttpResponseRedirect(reverse("show_users"))