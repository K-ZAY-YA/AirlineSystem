from django.shortcuts import render, redirect
from ..models import *
from django.contrib import messages

def crewstore(request):
    if request.method == "POST":
        crews = Crew.objects.get()
        crews.flight = request.POST.get('flight')
        crews.service_status = request.POST.get('service_status')
        crews.name = request.POST.get('name')
        crews.depature_port = request.POST.get('departure_port')
        crews.arrival_port = request.POST.get('arrival_port')
        crews.depature_date_time = request.POST.get('departure_date_time')
        crews.arrival_date_time = request.POST.get('arrival_date_time')
        crews.save()  
        messages.success(request, "Crew Add Successfully")
        return redirect('/pages/crewstoreview')
    return render(request, 'pages/createcrew')