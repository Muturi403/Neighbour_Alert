from django.shortcuts import render, redirect
from .models import Postii, Business, Neighborhood, Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm, BusinessForm, PostiiForm
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    if request.user.profile.neighborhood == None:
        messages.success(request, 'Please fill out you Neighbourhood')
        return redirect('uprofile')
    else:
        neighdetails = Neighborhood.objects.get(
            name=request.user.profile.neighborhood)
        businesses = Business.objects.filter(
            neighborhood=request.user.profile.neighborhood)
        stories = Postii.objects.filter(
            neighborhood=request.user.profile.neighborhood)

        params = {
            'neighdetails': neighdetails,
            'businesses': businesses,
            'stories': stories,
        }
        return render(request, 'index.html', params)
