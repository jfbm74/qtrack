from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View

from userext.models import UserProfile
from .forms import UserForm, UserProfileForm
from django.contrib import messages

def user_list(request):
    users = User.objects.all()  # Obtener todos los usuarios
    return render(request, 'config/users/user_list.html', {'users': users})


class CreateUserView(View):
    def get(self, request):
        user_form = UserForm()
        profile_form = UserProfileForm()
        return render(request, 'config/users/add_user.html', {'user_form': user_form, 'profile_form': profile_form})

    def post(self, request):
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            if profile_form.is_valid():
                # Check if profile already exists
                profile, created = UserProfile.objects.get_or_create(user=user, defaults=profile_form.cleaned_data)
                if not created:
                    # If the profile already exists, update it
                    for key, value in profile_form.cleaned_data.items():
                        setattr(profile, key, value)
                    profile.save()
                messages.success(request, 'User created successfully')               
            return redirect('user-list')
        else:
            print("User form errors:", user_form.errors)
            print("Profile form errors:", profile_form.errors)
            messages.error(request, 'Please correct the error below.')
            users = User.objects.all()  # Obtener todos los usuarios
            return render(request, 'config/users/user_list.html',  {'users': users})