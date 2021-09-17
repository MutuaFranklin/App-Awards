from awardsApp.models import Project, Profile
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, PublishProjectForm, RatingsForm, ReviewForm
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
    current_user = request.user
    if request.method == 'POST':
        pForm = PublishProjectForm(request.POST, request.FILES)
        if pForm.is_valid():
            project_post = pForm.save(commit=False)
            project_post.publisher = current_user.profile
            project_post.save()
            return redirect('home')
    else:
        pForm = PublishProjectForm()

   
    title = 'Publish'
    context = {
        "title": title,
        "pForm":pForm
    }
    return render(request, 'awards/submit-project.html', context)


def projectDetails(request, id):
    current_user = request.user
    project = get_object_or_404(Project, id=id)
    currentProf = get_object_or_404(Profile, user=request.user)

   

    #Rating Form
    if request.method == 'POST':
        rateForm = RatingsForm(request.POST, request.FILES)
        if rateForm.is_valid():
            project_rating = rateForm.save(commit=False)
            project_rating.project = project
            project_rating.rated_by = current_user
            project_rating.save()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        rateForm = RatingsForm()

    #Review Form
    if request.method == 'POST':
        reviewForm = ReviewForm(request.POST, request.FILES)
        if reviewForm.is_valid():
            project_review = reviewForm.save(commit=False)
            project_review.project = project
            project_review.reviewed_by = current_user
            project_review.save()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        reviewForm = ReviewForm()

   
    title = 'Project Details'
    context = {
        "title": title,
        "project": project,
        "reviewForm":reviewForm,
        "rateForm":rateForm,
        "profile":currentProf,
    }
    template = loader.get_template('awards/project-details.html')

    # return render(request, 'awards/project-details.html', context )
    return HttpResponse(template.render(context, request))


