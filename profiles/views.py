from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Profile
from awardsApp.models import Project

# Create your views here.



def userProfile(request, username):
    otherUser = get_object_or_404(User, username=username)
    userProfile = Profile.objects.get(user=otherUser)
    myProfile = Profile.objects.get(user=request.user)
    # projects = Project.objects.filter(posted_by = userProfile).order_by('-posted_on')

    context ={
        "otherUser":otherUser,
        "userProfile":userProfile,
        # "projects": projects,
                  
    }


    return render(request, 'profile/userProfile.html', context)


