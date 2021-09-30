from django.shortcuts import render, redirect
from .models import Postii, Business, Neighborhood, Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm, BusinessForm, PostiiForm
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
