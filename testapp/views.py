import requests 
from django.shortcuts import render
from .models import city
from .forms import CityForm

# Create your views here.
def index(request):
    
    appid='b1daf741010b21dce953bcc4d65ef3e3'
    appid2='82b797b6ebc625032318e16f1b42c016'
    
    url='https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+appid2

    if(request.method=='POST'):
        form=CityForm(request.POST)
        form.save()
    
    form=CityForm()
    cities=city.objects.all()

    all_cities=[]
    for i in cities:
        res=requests.get(url.format(i.name)).json()
        city_info={
            'city':i.name,
            'temp':res['main']['temp'],
            'icon':res['weather'][0]['icon']
        }
        all_cities.append(city_info)


    context={'all_info':all_cities,'form':form}
    return render(request,'testapp/index.html',context)
