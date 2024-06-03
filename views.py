from django.shortcuts import render
import requests

def settings(request):
    response = requests.get('https://api.example.com/api/settings')
    if response.status_code == 200:
        data = response.json()
        return HttpResponse(data)
    else:
        return HttpResponse("Error retrieving data")


