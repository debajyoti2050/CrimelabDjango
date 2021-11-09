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





