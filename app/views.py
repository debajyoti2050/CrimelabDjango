from django.shortcuts import render, HttpResponse
import base64
from io import BytesIO
import pandas as pd
import matplotlib.pyplot as plt


#required dataset
df=pd.read_csv("data.csv") #load the dataset   #df is the data frame here(data set)
df['TOTAL']=df.iloc[:,-12:].sum(axis=1)  #new col for total crimes
d=df[:-38] #to drop total crime rows      #d is the updated data set 

#required in the coding part
list_state_ut = d['STATE/UT'].tolist()
list_state_ut = list_state_ut[0:36:]     #total state/ut coloumn
list_state_ut.remove('TOTAL (STATES)')   #particular state and UT only
list_all_ut = list_state_ut[28:36:]     #particular ut
list_state = list_state_ut[:28:]    #particular state

#required in the coding part
font1 = {'family':'serif','color':'orange','size':20}
font2 = {'family':'serif','color':'red','size':15}



#####################################################################################
#important required templates

def crime_template(str):
    temp1 = d[d['CRIME HEAD'].str.contains(str)] 
    temp2 = temp1.drop(temp1.index[[-1,-2,-10]]) 
    #temp2 = temp2.sort_values(by='TOTAL',ascending=False)
    tl=temp2['TOTAL'].tolist()
    temp2.plot(kind='bar',x='STATE/UT',y='TOTAL',color='red',figsize=(15,6))
    plt.xticks(rotation='vertical')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title(str, fontdict = font1)
    plt.xlabel("LIST OF STATES/UT", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    for i in range(35):                         #to show the value on the bar
        plt.text(x=i-0.4, y = tl[i]+2, s = tl[i], size = 10)
    buf = BytesIO()
    plt.savefig(buf, format="png", bbox_inches='tight')
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data
def state_ut_template(str):
    temp1 = d[d['STATE/UT'].str.contains(str)]
    #temp1 = temp1.sort_values(by='TOTAL',ascending=False)
    tl=temp1['TOTAL'].tolist() 
    temp1.plot(kind='bar',x='CRIME HEAD',y='TOTAL',color='red',figsize=(8,6))
    plt.xticks(rotation='vertical')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title(str, fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    for i in range(12):
        plt.text(x=i-0.3, y = tl[i]+2, s = tl[i], size = 10)
    buf = BytesIO()
    plt.savefig(buf, format="png", bbox_inches='tight')
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data

def crime_by_year_template(str):
    y=d[d['STATE/UT'].str.contains('ALL-INDIA')]
    sc=y.loc[:,['CRIME HEAD',str]]
    #sc = sc.sort_values(by=str,ascending=False)
    tl=sc[str].tolist()
    sc.plot(kind='bar',x='CRIME HEAD',y=str,color='red',figsize=(8,4))
    plt.xticks(rotation="vertical")
    plt.grid(b=True, color='grey',alpha=0.5)
    plt.title(str, fontdict = font1)
    plt.xlabel("TYPE OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIME", fontdict = font2)
    for i in range(12):
        plt.text(x=i-0.3, y = tl[i]+10, s = tl[i], size = 10)
    buf = BytesIO()
    plt.savefig(buf, format="png", bbox_inches='tight')
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data

def all_states_and_ut_templates(list,id,str,a,m,n): 
    total_list=[]
    for i in list:
        temp1 = d[d['STATE/UT'].str.contains(i)] 
        temp2=temp1.sum(axis=0)
        temp2=temp2['TOTAL']
        total_list.append(temp2)
    data = {'STATE/UT':list, 'TOTAL':total_list}
    ts=pd.DataFrame(data)
    ts = ts.sort_values(by ='TOTAL' ,ascending=False)
    tl=ts['TOTAL'].tolist() 
    ts.plot(kind='bar',x='STATE/UT',y='TOTAL',color='red',figsize=(float(a),6))
    plt.xticks(rotation='vertical')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title(str, fontdict = font1)
    for i in range(int(id)):
        plt.text(x=i-float(m), y = tl[i]+int(n), s = tl[i], size = 10)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    
    buf = BytesIO()
    plt.savefig(buf, format="png", bbox_inches='tight')
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data




# Create your views here.
#redirecting to the home page 
def index(request):
    #return HttpResponse("<h1>this is homepage</h1>")
    return render(request,'home.html')

######################################################################################################
# first drop down list menu


def crime_infanticide(request):
    gdata = crime_template('INFANTICIDE')
    #print (gdata)
    data=gdata
    return render(request,'showData.html',{"data":data})

def  crime_murder_of_children(request):
    gdata = crime_template('MURDER OF CHILDREN')
    data=gdata
    return render(request,'showData.html',{"data":data})

def  crime_rape_of_children(request):
    gdata = crime_template('RAPE OF CHILDREN')
    data=gdata
    return render(request,'showData.html',{"data":data})

def   crime_kidnapping_and_abduction_of_children(request):
    gdata = crime_template('KIDNAPPING and ABDUCTION OF CHILDREN')
    data=gdata
    return render(request,'showData.html',{"data":data})

def  crime_foeticide(request):
    gdata = crime_template('FOETICIDE')
    data=gdata
    return render(request,'showData.html',{"data":data})

def  crime_abetment_of_suicide(request):
    gdata = crime_template('ABETMENT OF SUICIDE')
    data=gdata
    return render(request,'showData.html',{"data":data})

def  crime_exposure_and_abandonment(request):
    gdata = crime_template('EXPOSURE AND ABANDONMENT')
    data=gdata
    return render(request,'showData.html',{"data":data})

def  crime_procuration_of_minor_girls(request):
    gdata = crime_template('PROCURATION OF MINOR GILRS')
    data=gdata
    return render(request,'showData.html',{"data":data})

def  crime_buying_of_girls_for_prostitution(request):
    gdata = crime_template('BUYING OF GIRLS FOR PROSTITUTION')
    data=gdata
    return render(request,'showData.html',{"data":data})

def  crime_selling_of_girls_for_prostitution(request):
    gdata = crime_template('SELLING OF GIRLS FOR PROSTITUTION')
    data=gdata
    return render(request,'showData.html',{"data":data})

def  crime_prohibition_of_child_marriage_act(request):
    gdata = crime_template('PROHIBITION OF CHILD MARRIAGE ACT')
    data=gdata
    return render(request,'showData.html',{"data":data})

def  crime_other_crimes_against_children(request):
    gdata = crime_template('OTHER CRIMES AGAINST CHILDREN')
    data=gdata
    return render(request,'showData.html',{"data":data})

def total_crime(request):
    temp1 = d[d['STATE/UT']=='TOTAL (ALL-INDIA)']
    temp1 = temp1.sort_values(by ='TOTAL' ,ascending=False)
    tl=temp1['TOTAL'].tolist()
    temp1.plot(kind='bar',x='CRIME HEAD',y='TOTAL',color='red',figsize=(8,6))
    plt.xticks(rotation='vertical')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("TOTAL CRIMES", fontdict = font1)
    for i in range(12):
        plt.text(x=i-0.2, y = tl[i]+1000, s = tl[i], size = 8)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png", bbox_inches='tight')
    gdata = base64.b64encode(buf.getbuffer()).decode("ascii")
    data=gdata
    return render(request ,'showData.html',{"data":data})

def INDIA_CRIME_CHART(request):
    total_list=[]
    for i in list_state_ut:
        temp1 = d[d['STATE/UT'].str.contains(i)] 
        temp2=temp1.sum(axis=0)
        temp2=temp2['TOTAL']
        total_list.append(temp2)
    data = {'STATE/UT':list_state_ut, 'TOTAL':total_list}
    ts=pd.DataFrame(data)
    ts = ts.sort_values(by ='TOTAL' ,ascending=False)
    tl=ts['TOTAL'].tolist() 
    ts.plot(kind='bar',x='STATE/UT',y='TOTAL',color='red',figsize=(16.6,6))
    plt.xticks(rotation='vertical')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("INDIAN CRIME CHART", fontdict = font1)
    for i in range(35):
        plt.text(x=i-0.5, y = tl[i]+1000, s = tl[i], size = 8)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png", bbox_inches='tight')
    gdata = base64.b64encode(buf.getbuffer()).decode("ascii")
    data=gdata
    return render(request,'showData.html',{"data":data})


#######################second drop down menu ####################

def ANDHRA_PRADESH(request):
    gdata = state_ut_template('ANDHRA PRADESH')
    data=gdata
    return render(request,'showData.html',{"data":data})

def ARUNACHAL_PRADESH(request):
    gdata = state_ut_template('ARUNACHAL PRADESH')
    data=gdata
    return render(request,'showData.html',{"data":data})

def ASSAM(request):
    gdata = state_ut_template('ASSAM')
    data=gdata
    return render(request,'showData.html',{"data":data})

def BIHAR(request):
    gdata = state_ut_template('BIHAR')
    data=gdata
    return render(request,'showData.html',{"data":data})

def CHHATTISGARH(request):
    gdata = state_ut_template('CHHATTISGARH')
    data=gdata
    return render(request,'showData.html',{"data":data})

def GOA(request):
    gdata = state_ut_template('GOA')
    data=gdata
    return render(request,'showData.html',{"data":data})

def GUJARAT(request):
    gdata = state_ut_template('GUJARAT')
    data=gdata
    return render(request,'showData.html',{"data":data})

def HARYANA(request):
    gdata = state_ut_template('HARYANA')
    data=gdata
    return render(request,'showData.html',{"data":data})

def HIMACHAL_PRADESH(request):
    gdata = state_ut_template('HIMACHAL PRADESH')
    data=gdata
    return render(request,'showData.html',{"data":data})

def JAMMU_and_KASHMIR(request):
    gdata = state_ut_template('JAMMU & KASHMIR')
    data=gdata
    return render(request,'showData.html',{"data":data})

def JHARKHAND(request):
    gdata = state_ut_template('JHARKHAND')
    data=gdata
    return render(request,'showData.html',{"data":data})

def KARNATAKA(request):
    gdata = state_ut_template('KARNATAKA')
    data=gdata
    return render(request,'showData.html',{"data":data})

def KERALA(request):
    gdata = state_ut_template('KERALA')
    data=gdata
    return render(request,'showData.html',{"data":data})

def MADHYA_PRADESH(request):
    gdata = state_ut_template('MADHYA PRADESH')
    data=gdata
    return render(request,'showData.html',{"data":data})

def MAHARASHTRA(request):
    gdata = state_ut_template('MAHARASHTRA')
    data=gdata
    return render(request,'showData.html',{"data":data})

def MANIPUR(request):
    gdata = state_ut_template('MANIPUR')
    data=gdata
    return render(request,'showData.html',{"data":data})

def MEGHALAYA(request):
    gdata = state_ut_template('MEGHALAYA')
    data=gdata
    return render(request,'showData.html',{"data":data})

def MIZORAM(request):
    gdata = state_ut_template('MIZORAM')
    data=gdata
    return render(request,'showData.html',{"data":data})

def NAGALAND(request):
    gdata = state_ut_template('NAGALAND')
    data=gdata
    return render(request,'showData.html',{"data":data})

def ODISHA(request):
    gdata = state_ut_template('ODISHA')
    data=gdata
    return render(request,'showData.html',{"data":data})

def PUNJAB(request):
    gdata = state_ut_template('PUNJAB')
    data=gdata
    return render(request,'showData.html',{"data":data})

def RAJASTHAN(request):
    gdata = state_ut_template('RAJASTHAN')
    data=gdata
    return render(request,'showData.html',{"data":data})

def SIKKIM(request):
    gdata = state_ut_template('SIKKIM')
    data=gdata
    return render(request,'showData.html',{"data":data})

def TAMIL_NADU(request):
    gdata = state_ut_template('TAMIL NADU')
    data=gdata
    return render(request,'showData.html',{"data":data})

def TRIPURA(request):
    gdata = state_ut_template('TRIPURA')
    data=gdata
    return render(request,'showData.html',{"data":data})

def UTTAR_PRADESH(request):
    gdata = state_ut_template('UTTAR PRADESH')
    data=gdata
    return render(request,'showData.html',{"data":data})

def UTTARAKHAND(request):
    gdata = state_ut_template('UTTARAKHAND')
    data=gdata
    return render(request,'showData.html',{"data":data})

def WEST_BENGAL(request):
    gdata = state_ut_template('WEST BENGAL')
    data=gdata
    return render(request,'showData.html',{"data":data})

def A_and_N_ISLANDS(request):
    gdata = state_ut_template('A & N ISLANDS')
    data=gdata
    return render(request,'showData.html',{"data":data})

def CHANDIGARH(request):
    gdata = state_ut_template('CHANDIGARH')
    data=gdata
    return render(request,'showData.html',{"data":data})

def D_and_N_HAVELI(request):
    gdata = state_ut_template('D & N HAVELI')
    data=gdata
    return render(request,'showData.html',{"data":data})

def DAMAN_and_DIU(request):
    gdata = state_ut_template('DAMAN & DIU')
    data=gdata
    return render(request,'showData.html',{"data":data})

def DELHI(request):
    gdata = state_ut_template('DELHI')
    data=gdata
    return render(request,'showData.html',{"data":data})

def LAKSHADWEEP(request):
    gdata = state_ut_template('LAKSHADWEEP')
    data=gdata
    return render(request,'showData.html',{"data":data})

def PUDUCHERRY(request):
    gdata = state_ut_template('PUDUCHERRY')
    data=gdata
    return render(request,'showData.html',{"data":data})

def All_States(request):
    gdata =  all_states_and_ut_templates(list_state,28,'TOTAL STATES',16.5,0.4,1000)
    data=gdata
    return render(request ,'showData.html', {"data":data})

def All_UT(request):
    gdata =  all_states_and_ut_templates(list_all_ut,7,'TOTAL UNION TERRITORY',8,0.2,100)
    data=gdata
    return render(request,'showData.html',{"data":data})


############################ third dropdown menu ####################

def crime_2001(request):
    gdata = crime_by_year_template('2001')
    data=gdata
    return render(request ,'showData.html',{"data":data})

def crime_2002(request):
    gdata = crime_by_year_template('2002')
    data=gdata
    return render(request ,'showData.html',{"data":data})

def crime_2003(request):
    gdata = crime_by_year_template('2003')
    data=gdata
    return render(request ,'showData.html',{"data":data})

def crime_2004(request):
    gdata = crime_by_year_template('2004')
    data=gdata
    return render(request ,'showData.html',{"data":data})

def crime_2005(request):
    gdata = crime_by_year_template('2005')
    data=gdata
    return render(request ,'showData.html',{"data":data})

def crime_2006(request):
    gdata = crime_by_year_template('2006')
    data=gdata
    return render(request ,'showData.html',{"data":data})

def crime_2007(request):
    gdata = crime_by_year_template('2007')
    data=gdata
    return render(request ,'showData.html',{"data":data})

def crime_2008(request):
    gdata = crime_by_year_template('2008')
    data=gdata
    return render(request ,'showData.html',{"data":data})

def crime_2009(request):
    gdata = crime_by_year_template('2009')
    data=gdata
    return render(request ,'showData.html',{"data":data})

def crime_2010(request):
    gdata = crime_by_year_template('2010')
    data=gdata
    return render(request ,'showData.html',{"data":data})

def crime_2011(request):
    gdata = crime_by_year_template('2011')
    data=gdata
    return render(request ,'showData.html',{"data":data})

def crime_2012(request):
    gdata = crime_by_year_template('2012')
    data=gdata
    return render(request ,'showData.html',{"data":data})

    


                  ###################################        THE END               ########################












