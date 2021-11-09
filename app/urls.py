from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    #for the homepage
    path("", views.index, name='home'),

    #first drop-down menu

    path("crime_infanticide", views.crime_infanticide ,name='crime_infanticide'),
    path("crime_murder_of_children", views.crime_murder_of_children,name='crime_murder_of_children'),
    path("crime_rape_of_children", views.crime_rape_of_children ,name='crime_rape_of_children'),
    path("crime_kidnapping_and_abduction_of_children", views.crime_kidnapping_and_abduction_of_children ,name='crime_kidnapping_and_abduction_of_children'),
    path("crime_foeticide", views.crime_foeticide ,name='crime_foeticide'),
    path("crime_abetment_of_suicide", views.crime_abetment_of_suicide ,name='crime_abetment_of_suicide'),
    path("crime_exposure_and_abandonment", views.crime_exposure_and_abandonment,name='crime_exposure_and_abandonment'),
    path("crime_procuration_of_minor_girls", views.crime_procuration_of_minor_girls ,name='crime_procuration_of_minor_girls'),
    path("crime_buying_of_girls_for_prostitution", views.crime_buying_of_girls_for_prostitution ,name='crime_buying_of_girls_for_prostitution'),
    path("crime_selling_of_girls_for_prostitution", views.crime_selling_of_girls_for_prostitution ,name='crime_selling_of_girls_for_prostitution'),
    path("crime_prohibition_of_child_marriage_act", views.crime_prohibition_of_child_marriage_act ,name='crime_prohibition_of_child_marriage_act'),
    path("crime_other_crimes_against_children", views.crime_other_crimes_against_children ,name='crime_other_crimes_against_children'),
    path("Total_Crime", views.total_crime ,name='Total_Crime'),
    path("INDIA_CRIME_CHART", views.INDIA_CRIME_CHART ,name='INDIA_CRIME_CHART')

    

]