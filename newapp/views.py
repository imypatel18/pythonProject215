from django.shortcuts import render
import requests

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def sports(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=sports"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['sportsdata'] = inshorts_data
    return render(request,'sports.html',records)

