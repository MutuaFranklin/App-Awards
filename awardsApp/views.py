from awardsApp.models import Project
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm
from .email import send_welcome_email
from django.http import HttpResponse
from django.template import loader






# Create your views here
def register(request):
    reg_form = UserRegistrationForm()

    if request.method == 'POST':
        reg_form = UserRegistrationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            user = reg_form.cleaned_data.get('username')
            email = reg_form.cleaned_data['email']
            messages.success(request, 'Account was created for ' + user)
            send_welcome_email(user,email)
            return redirect('login')
        else:
            reg_form = UserRegistrationForm()

    
    return render(request, 'registration/sign_up.html', {'reg_form': reg_form})


def login_user(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'registration/login.html')


def home(request):
    projects= Project.objects.all()

    context = {
        "projects": projects
    }
    return render(request, 'awards/index.html', context)


@login_required(login_url='login')
def publishProject(request):


    title = 'Publish'
    context = {
        "title": title
    }
    return render(request, 'awards/submit-project.html', context)


def projectDetails(request, id):
    
    project = get_object_or_404(Project, id=id)

    # currentProf = get_object_or_404(Project, user=request.user)
    
    context = {

        "project":project
    }
    # return render(request, 'awards/project-details.html', context )
    template = loader.get_template('awards/project-details.html')
    context = {
         "project":project
    }
    return HttpResponse(template.render(context, request))


