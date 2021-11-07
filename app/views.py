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


# Create your views here.
def index(request):
    #return HttpResponse("<h1>this is homepage</h1>")
    return render(request,'home.html')

#####################################################################################################
# first drop down list menu


def crime_infanticide(request):
    gdata = crime_template('INFANTICIDE')
    data=gdata
    return render(request,'showData.html',data)
