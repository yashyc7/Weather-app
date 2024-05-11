from django.shortcuts import render,HttpResponse
import datetime
import requests
# Create your views here.
def home(request):
    if 'city' in request.POST:
        city=request.POST.get('city')
    else:
        city='indore'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=0ea822a4ce124c0668a9a536ea3a226e'

    PARAMS={'units':'metric'}

    data=requests.get(url,PARAMS).json()
    
    try:
        description = data['weather'][0].get('description', 'N/A')
        icon = data['weather'][0].get('icon', 'N/A')
        temp = data['main'].get('temp', 'N/A')
    except KeyError as e:
        # Handle the case where the expected keys are missing in the data dictionary
        print(f"KeyError: {e}")
        description = 'N/A'
        icon = 'N/A'
        temp = 'N/A'



    day=datetime.date.today()

    return render(request,'index.html',{'description':description,'icon':icon,'temp':temp,'day':day,'city':city})