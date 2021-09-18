from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Profile
from awardsApp.models import Project
from .forms import UpdateUserProfileForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy




# Create your views here.



def userProfile(request, username):
    otherUser = get_object_or_404(User, username=username)
    userProfile = Profile.objects.get(user=otherUser)
    myProfile = Profile.objects.get(user=request.user)
    projects = Project.objects.filter(publisher = myProfile)

    context ={
        "otherUser":otherUser,
        "profile":userProfile,
        "projects": projects,
                  
    }


    return render(request, 'profile/userProfile.html', context)




class UpdateProfileView(UpdateView):
        model=Profile
        slug_field = "username"
        form_class =UpdateUserProfileForm
        template_name ='profile/editProfile.html'
        
        def get_queryset(self): 
            return Profile.objects.all()


        def get_success_url(self):
        
            return reverse_lazy('userProfile',args=[self.request.user.username]) 


