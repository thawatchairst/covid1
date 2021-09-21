from django.shortcuts import render
import requests

# Create your views here.


def index(request):
    req = requests.get('https://covid19.ddc.moph.go.th/api/Cases/today-cases-all')
    jsonData = req.json()
    Statuscode =req.status_code
    ##print(jsonData)
    return render(request ,'index.html',{'status':Statuscode,'data':jsonData})
