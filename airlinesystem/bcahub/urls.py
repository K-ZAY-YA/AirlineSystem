from django.contrib import admin
from django.urls import path
from bcahub.appviews import view, createview, storeview, updateview, deleteview
from .views import *

urlpatterns = [
    path('pages/home', view.home, name='home'),
    path('pages/airlines', view.airline, name='airline'),
    path('pages/riskaction', view.risk, name='risk'),    
    path('pages/crew', view.crew, name='crew'),
    path('pages/journey', view.journey, name='journey'),

    path('pages/airlinecreate', createview.createairline, name='createair'),
    path('pages/crewcreate', createview.createcrew, name='createcrew'),
    path('pages/homecreate', createview.createhome, name='createhome'),
    path('pages/journey', createview.createjourney, name='createjourney'),
    path('pages/riskcreate', createview.createrisk, name='createrisk'),
    path('pages/crewcreate', storeview.crewstore, name='crewstoreview'),

    path('pages/airlineedit/<int:pk>', updateview.airlineedit, name='editairline'),
    path('pages/airlineupdate/<int:pk>', updateview.airlineupdate, name='updateairline'),
    path('pages/homeedit/<int:pk>', updateview.homeedit, name='edithome'),
    path('pages/homeupdate<int:pk>', updateview.homeupdate, name='updatehome'),
    path('pages/journeyedit<int:pk>', updateview.journeyedit, name='editjoureny'),
    path('pages/journeyupdate<int:pk>', updateview.journeyupdate, name='updatejourney'),
    path('pages/crewedit/<int:pk>', updateview.creweidt, name='editcrew'),
    path('pages/crewupdate/<int:pk>', updateview.crewupdate, name='updatecrew' ),
    path('pages/riskedit/<int:pk>', updateview.riskedit, name='editrisk'),
    path('pages/riskupdate/<int:pk>', updateview.riskupdate, name='updaterisk'),


    path('pages/crewdelete/<int:pk>', deleteview.crewdelete, name='deletecrew'),
    path('pages/airlinedelet/<int:pk>', deleteview.airlinedelete, name='deleteairline'),
    path('pages/homedelete/<int:pk>', deleteview.homedelete, name='delethome'),
    path('pages/journeydelete/<int:pk>', deleteview.journeydelete, name='deletejourney'),
    path('pages/riskdelete/<int:pk>', deleteview.riskdelete, name='deleterisk')

]
