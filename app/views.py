from django.shortcuts import render

# Create your views here.
import datetime
def filters(request):
    date = datetime.datetime.now()
    a='jay Shri ram'
    d={'a':a,'date':date}
    return render(request,'filter.html',d)

def usd(request):
    d={'data':'haI harshad How are you'}
    return render(request,'usdfilter.html',d)