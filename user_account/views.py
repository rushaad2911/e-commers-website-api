from re import U
from django.shortcuts import render
from rest_framework import generics,permissions
from .models import UserAccount
from django.http import HttpResponseRedirect 
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Permission

    
    

  

    

    