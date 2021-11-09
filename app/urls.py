from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    #for the homepage
    path("", views.index, name='home'),

    ################first drop-down menu###############

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
    path("INDIA_CRIME_CHART", views.INDIA_CRIME_CHART ,name='INDIA_CRIME_CHART'),

    ##################second drop down menu #################

    path(" ANDHRA_PRADESH", views. ANDHRA_PRADESH ,name=' ANDHRA_PRADESH'),
    path("ARUNACHAL_PRADESH", views.ARUNACHAL_PRADESH ,name='ARUNACHAL_PRADESH'),
    path("ASSAM", views.ASSAM ,name='ASSAM'),
    path("BIHAR", views.BIHAR ,name='BIHAR'),
    path("CHHATTISGARH", views.CHHATTISGARH ,name='CHHATTISGARH'),
    path("GOA", views.GOA ,name='GOA'),
    path("GUJARAT", views.GUJARAT ,name='GUJARAT'),
    path("HARYANA", views.HARYANA ,name='HARYANA'),
    path("HIMACHAL_PRADESH", views.HIMACHAL_PRADESH,name='HIMACHAL_PRADESH'),
    path("JAMMU_and_KASHMIR", views.JAMMU_and_KASHMIR ,name='JAMMU_and_KASHMIR'),
    path("JHARKHAND", views.JHARKHAND ,name='JHARKHAND'),
    path("KARNATAKA", views.KARNATAKA,name='KARNATAKA'),
    path("KERALA", views.KERALA ,name='KERALA'),
    path("MADHYA_PRADESH", views.MADHYA_PRADESH ,name='MADHYA_PRADESH'),
    path("MAHARASHTRA", views.MAHARASHTRA ,name='MAHARASHTRA'),
    path("MANIPUR", views.MANIPUR ,name='MANIPUR'),
    path("MEGHALAYA", views.MEGHALAYA ,name='MEGHALAYA'),
    path("MIZORAM", views.MIZORAM ,name='MIZORAM'),
    path("NAGALAND", views.NAGALAND,name='NAGALAND'),
    path("ODISHA", views.ODISHA ,name='ODISHA'),
    path("PUNJAB", views.PUNJAB,name='PUNJAB'),
    path("RAJASTHAN", views.RAJASTHAN,name='RAJASTHAN'),
    path("SIKKIM", views.SIKKIM,name='SIKKIM'),
    path("TAMIL_NADU", views.TAMIL_NADU ,name='TAMIL_NADU'),
    path("TRIPURA", views.TRIPURA,name='TRIPURA'),
    path("UTTAR_PRADESH", views.UTTAR_PRADESH ,name='UTTAR_PRADESH'),
    path("UTTARAKHAND", views.UTTARAKHAND,name='UTTARAKHAND'),
    path("WEST_BENGAL", views.WEST_BENGAL,name='WEST_BENGAL'),
    path("A_and_N_ISLANDS", views.A_and_N_ISLANDS,name='A_and_N_ISLANDS'),
    path("CHANDIGARH", views.CHANDIGARH,name='CHANDIGARH'),
    path("D_and_N_HAVELI", views.D_and_N_HAVELI,name='D_and_N_HAVELI'),
    path("DAMAN_and_DIU", views.DAMAN_and_DIU,name='DAMAN_and_DIU'),
    path("DELHI", views.DELHI,name='DELHI'),
    path("LAKSHADWEEP", views.LAKSHADWEEP,name='LAKSHADWEEP'),
    path("PUDUCHERRY", views.PUDUCHERRY,name='PUDUCHERRY'),
    path("All_States", views.All_States,name='All_States'),
    path("All_UT", views.All_UT,name='All_UT'),

    ##########################  third drop down menu  #################

    path("crime_2001", views.crime_2001,name='crime_2001'),
    path("crime_2002", views.crime_2002,name='crime_2002'),
    path("crime_2003", views.crime_2003,name='crime_2003'),
    path("crime_2004", views.crime_2004,name='crime_2004'),
    path("crime_2005", views.crime_2005,name='crime_2005'),
    path("crime_2006", views.crime_2006,name='crime_2006'),
    path("crime_2007", views.crime_2007,name='crime_2007'),
    path("crime_2008", views.crime_2008,name='crime_2008'),
    path("crime_2009", views.crime_2009,name='crime_2009'),
    path("crime_2010", views.crime_2010,name='crime_2010'),
    path("crime_2011", views.crime_2011,name='crime_2011'),
    path("crime_2012", views.crime_2012,name='crime_2012')


    ############################# end of url management ########################


]