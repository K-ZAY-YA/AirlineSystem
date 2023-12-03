from django.db import models

# Create your models here.
class Traveller(models.Model):
    flight = models.CharField(max_length=20, blank=False)
    timeframe = models.CharField(max_length=20, blank=False)
    name = models.CharField(max_length=20, blank=False)
    dob = models.IntegerField(10)
    nrc = models.CharField(max_length=50, blank=False)
    gender = models.CharField(max_length=6, blank=False)
    depature_port = models.CharField(max_length=10, blank=False)
    depature_date_time = models.DateTimeField()
    arrival_port = models.CharField(max_length=10, blank=False) 
    arrival_date_time = models.DateTimeField()
    action = models.CharField(max_length=10, blank=True, null=True)


class Airline(models.Model):
    operating_date = models.DateTimeField()
    airline = models.CharField(max_length=20, blank=False)
    airline_name = models.CharField(max_length=20, blank=False)
    airline_nO = models.IntegerField(10)
    depature_port = models.CharField(max_length=10, blank=False)
    depature_date_time = models.DateTimeField()
    arrival_date_time = models.DateTimeField()
    flight_status = models.CharField(max_length=10, blank=False)
    delay_issue = models.CharField(max_length=10, blank=False)
    remarks = models.CharField(max_length=10, blank=False)
    action = models.CharField(max_length=10, blank=True, null=True)
    
class Riskaction(models.Model):
    no = models.IntegerField(5)
    name = models.CharField(max_length=20, blank=False)
    dob = models.IntegerField(10)
    father = models.CharField(max_length=20, blank=False)
    passport = models.IntegerField(10)
    gender = models.CharField(max_length=10, blank=False)
    nrc = models.CharField(max_length=50, blank=False)
    nationality = models.CharField(max_length=10, blank=False)
    status = models.CharField(max_length=10, blank=False)
    action = models.CharField(max_length=10, blank=True, null=True)

    
class Crew(models.Model):
    flight = models.CharField(max_length=20, blank=False)
    service_status = models.CharField(max_length=10, blank=False)
    name = models.CharField(max_length=20, blank=False)
    depature_port = models.CharField(max_length=10, blank=False)
    arrival_port = models.CharField(max_length=10, blank=False) 
    depature_date_time = models.DateTimeField()
    arrival_date_time = models.DateTimeField()
    action = models.CharField(max_length=10, blank=True, null=True)


class journeysearch(models.Model):
    no = models.IntegerField(5)
    name = models.CharField(max_length=20, blank=False)
    dob = models.IntegerField(10)
    father = models.CharField(max_length=20, blank=False)
    passport = models.IntegerField(10)
    gender = models.CharField(max_length=10, blank=False)
    flightname = models.CharField(max_length=20, blank=False)
    sector = models.CharField(max_length=10)
    depature_date_time = models.DateTimeField()
    arrival_date_time = models.DateTimeField()
    risk_Satus = models.CharField(max_length=10, blank=False)
    action = models.CharField(max_length=10, blank=True, null=True)