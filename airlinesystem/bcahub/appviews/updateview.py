from django.shortcuts import render, redirect
from ..models import *
from django.contrib import messages


def airlineedit(request, pk):
    airlines = Airline.objects.get(id=pk)
    return render(request, 'pages/airlineedit.html', {'airlines': airlines})

def airlineupdate(request, pk):
    if request.method == 'POST':
        try:
            airline = Airline.objects.get(pk=pk)
            airline.Operating_date = request.POST.get('Operating_date')
            airline.Airline = request.POST.get('Airline')
            airline.Airline_name = request.POST.get('Airline_name')
            airline.Airline_NO = request.POST.get('Airline_NO')
            airline.Depature_Port = request.POST.get('Depature_Port')
            airline.Depature_Date_time = request.POST.get('Depature_Date_time')
            airline.Arrival_Date_Time = request.POST.get('Arrival_Date_Time')
            airline.Flight_status = request.POST.get('Flight_status')
            airline.Delay_issue = request.POST.get('Delay_issue')
            airline.Remarks = request.POST.get('Remarks')
            airline.save()   
            messages.success(request, "Airline Updated Successfully")
        except Airline.DoesNotExist:
            messages.error(request, "Airline does not exist")
        return redirect('/pages/airline') 

def creweidt(request, pk):
    crews = Crew.objects.get(id=pk)
    return render(request, 'pages/crewedit.html', {'crews': crews})

def crewupdate(request, pk):
    if request.method == 'POST':
        try:
            crew = Crew.objects.get(pk=pk)
            crew.Flight = request.POST.get('flight')
            crew.Service_status = request.POST.get('service_status')
            crew.Name = request.POST.get('name')
            crew.Depature_Port = request.POST.get('departure_port')
            crew.Arrival_Port = request.POST.get('arrival_port')
            crew.Depature_Date_time = request.POST.get('departure_date_time')
            crew.Arrival_Date_Time = request.POST.get('arrival_date_time')
            crew.save()  
            messages.success(request, "Crew Updated Successfully")
        except Crew.DoesNotExist:
            messages.error(request, "Crew does not exist")
        return redirect('/pages/crew') 


def homeedit(request, pk):
    travels = Traveller.objects.get(id=pk)
    return render(request, 'pages/homeeidt.html', {'travels':travels})

def homeupdate(request, pk):
    if request.method == 'POST':
        try:
            travel = Traveller.objects.get(pk = pk)
            travel.Flight = request.POST.get('Flight')
            travel.TimeFrame = request.POST.get('TimeFrame')
            travel.Name = request.POST.get('Name')
            travel.DOB = request.POST.get('DOB')
            travel.NRC = request.POST.get('NRC')
            travel.Gender = request.POST.get('Gender')
            travel.Depature_Port = request.POST.get('Depature_Port')
            travel.Depature_Date_time = request.POST.get('Depature_Date_time')
            travel.Arrival_Port = request.POST.get('Arrival_Port')
            travel.Arrival_Date_Time = request.POST.get('Arrival_Date_Time')
            travel.save()
            messages.success(request, "Traveller Updated Successfully")
        except Traveller.DoesNotExist:
            messages.error(request, "Traveller does not exist")
        return redirect('/pages/home') 

def journeyedit(request, pk):
    journeys = journeysearch.objects.get(id=pk)
    return render(request, 'pages/journeyedit.html', {'journeys':journeys})

def journeyupdate(request, pk):
    if request.metho == 'POST':
        try:
            joureny = journeysearch(pk=pk)
            joureny.No = request.POST.get('No')
            joureny.Name = request.POST.get('Name')
            joureny.DOB = request.POST.get('DOB')
            joureny.Father = request.POST.get('Father')
            joureny.Passport = request.POST.get('Passport')
            joureny.Gender = request.POST.get('Gender')
            joureny.FlightName = request.POST.get('FlightName')
            joureny.sector = request.POST.get('sector')
            joureny.Depature_Date_time = request.POST.get('Depature_Date_time')
            joureny.Arrival_Date_Time = request.POST.get('Arrival_Date_Time')
            joureny.Risk_Satus = request.POST.get('Risk_Satus')
            joureny.save()
            messages.success(request, "Journey Added Successfully")
        except journeysearch.DoesNotExist:
            messages.error(request, "Journey does not exist")
        return redirect('/pages/journey')

def riskedit(request, pk):
    risks = Riskaction.objects.get(id=pk)
    return render(request, 'pages/riskedit.html', {'risks':risks})

def riskupdate(request, pk):
    if request.method == 'POST':
        try:
            risk = Riskaction(pk=pk)
            risk.No = request.POST.get('No')
            risk.Name = request.POST.get('Name')
            risk.DOB = request.POST.get('DOB')
            risk.Father = request.POST.get('Father')
            risk.Passport = request.POST.get('Passport')
            risk.Gender = request.POST.get('Gender')
            risk.FlightName = request.POST.get('FlightName')
            risk.sector = request.POST.get('sector')
            risk.Depature_Date_time = request.POST.get('Depature_Date_time')
            risk.save()
            messages.success(request, "Risk Added Successfully")
        except Riskaction.DoesNotExist:
            messages.error(request, "Riskaction does not exist")
        return redirect('pages/risk')


