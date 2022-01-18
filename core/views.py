from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views import View
from django.contrib.auth.hashers import make_password

from core.models import Profile


class RegisterView(View):
    def get(self, request):
        return render(request, "core/register.html")

    def post(self, request):
        if 'register' in request.POST:
            username = request.POST.get('username', )
            email = request.POST.get('email', )
            password = request.POST.get('password1', )
            password2 = request.POST.get('password2', )

            try:
                query_username = User.objects.get(username=username)
                messages.error(request, "Username has been taken already, use another.")
                redirect('core:register')
            except User.DoesNotExist:
                pass

            try:
                query_email = User.objects.get(email=email)
                messages.error(request, "Email has been taken already, use another.")
                redirect('core:register')
            except:
                pass

            if password != password2:
                messages.error(request, "Password does not exist, try again!!!")
                redirect('core:register')

            user = User.objects.create(username=username, email=email, password=make_password(password))
            user.save()
            messages.success(request, "Registration successful.")
            login(request, user)
            return redirect('voter:index')
        else:
            username = request.POST.get('username', )
            password = request.POST.get('password', )
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}")
                    return redirect('dashboard:index')
                else:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}")
                    return redirect('voter:index')
            else:
                messages.error(request, "Invalid username and password")
                return redirect('core:register')


class IndexView(View):
    def get(self, request):
        return render(request, "core/home.html")


class UpdateProfileView(View):
    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        user = User.objects.get(id=request.user.id)
        context = {
            'profile': profile,
            'user': user,
        }
        return render(request, "core/updateProfile.html", context)

    def post(self, request):
        username = request.POST.get('username', )
        email = request.POST.get('email', )
        phone_number = request.POST.get('phone_number', )
        dob = request.POST.get('dob', )
        gender = request.POST.get('gender', )

        user = User.objects.get(id=request.user.id)
        profile = Profile.objects.get(user=request.user)

        if 'profile_image' in request.FILES:
            profile_image = request.FILES['profile_image']
            profile.profile_image = profile_image

        if username:
            user.username = username
            profile.username = username

        if email:
            user.email = email
            profile.email = email

        if phone_number:
            profile.phone_number = phone_number

        if dob:
            profile.dob = dob

        if gender:
            profile.gender = gender

        profile.save()
        user.save()
        messages.success(request, "Profile Updated Successfully!!")

        return redirect('core:update_profile')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('core:register')
