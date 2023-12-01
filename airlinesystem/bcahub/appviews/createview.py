from django.shortcuts import render, redirect
from ..models import *

def createhome(request):
    return render(request, 'pages/homecreate.html')

def createairline(request):
    return render(request, 'pages/airlinecreate.html')

def createcrew(request):
    return render(request, 'pages/crewcreate.html')

def createjourney(request):
    return render(request, 'pages/journeycreate.html')

def createrisk(requrst):
    return render(requrst, 'pages/riskcreate.html')