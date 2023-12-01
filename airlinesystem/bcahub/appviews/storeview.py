from django.shortcuts import render, redirect
from ..models import *
from django.contrib import messages

def crewstore(request):
    if request.method == "POST":
        crews = Crew.objects.get()
        crews.Flight = request.POST.get('flight')
        crews.Service_status = request.POST.get('service_status')
        crews.Name = request.POST.get('name')
        crews.Depature_Port = request.POST.get('departure_port')
        crews.Arrival_Port = request.POST.get('arrival_port')
        crews.Depature_Date_time = request.POST.get('departure_date_time')
        crews.Arrival_Date_Time = request.POST.get('arrival_date_time')
        crews.save()  
        messages.success(request, "Crew Add Successfully")
        return redirect('/pages/crewstoreview')
    return render(request, 'pages/createcrew')