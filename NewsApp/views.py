from newsapi import NewsApiClient
import requests
import json
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from .models import *     

def Index(request):
    
    topheadlines =requests.get(url="https://newsapi.org/v2/top-headlines?country=in&apiKey=2424b12b52e04473bdca438ed6813ba6").json()
    articles = topheadlines['articles']
 
    desc = []
    news = []
    img = []
 
    for i in range(len(articles)):
        myarticles = articles[i]
 
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
 
 
    mylist = zip(news, desc, img)
 
 
    return render(request, 'index.html', context={"mylist":mylist})

def register(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already Taken')
                return redirect('register')
            else:
                email = request.POST.get('email')
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                print("User Added")
                return redirect('login')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        uname = request.POST['Username']
        password = request.POST['Password']
        user = auth.authenticate(username=uname, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invaild credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def sports(request):
    newsapi = NewsApiClient(api_key="2424b12b52e04473bdca438ed6813ba6")
    #topheadlines = newsapi.get_top_headlines(sources='google-news-en')
    topheadlines = requests.get(url="https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=2424b12b52e04473bdca438ed6813ba6").json()
    articles = topheadlines['articles']
 
    desc = []
    news = []
    img = []
 
    for i in range(len(articles)):
        myarticles = articles[i]
 
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
 
 
    mylist = zip(news, desc, img)
 
 
    return render(request, 'sports.html', context={"mylist":mylist})

def technology(request):
    newsapi = NewsApiClient(api_key="2424b12b52e04473bdca438ed6813ba6")
    #topheadlines = newsapi.get_top_headlines(sources='google-news-en')
    topheadlines = requests.get(url="https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=2424b12b52e04473bdca438ed6813ba6").json()
    articles = topheadlines['articles']
 
    desc = []
    news = []
    img = []
 
    for i in range(len(articles)):
        myarticles = articles[i]
 
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
 
 
    mylist = zip(news, desc, img)
 
 
    return render(request, 'technology.html', context={"mylist":mylist})

def buisness(request):
    newsapi = NewsApiClient(api_key="2424b12b52e04473bdca438ed6813ba6")
    #topheadlines = newsapi.get_top_headlines(sources='google-news-en')
    topheadlines = requests.get(url="https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=2424b12b52e04473bdca438ed6813ba6").json()
    articles = topheadlines['articles']
 
    desc = []
    news = []
    img = []
 
    for i in range(len(articles)):
        myarticles = articles[i]
 
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
 
 
    mylist = zip(news, desc, img)
 
 
    return render(request, 'buisness.html', context={"mylist":mylist})

def international(request):
    newsapi = NewsApiClient(api_key="2424b12b52e04473bdca438ed6813ba6")
    #topheadlines = newsapi.get_top_headlines(sources='google-news-en')
    topheadlines = requests.get(url="https://newsapi.org/v2/top-headlines?country=us&apiKey=2424b12b52e04473bdca438ed6813ba6").json()
    articles = topheadlines['articles']
 
    desc = []
    news = []
    img = []
 
    for i in range(len(articles)):
        myarticles = articles[i]
 
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
 
 
    mylist = zip(news, desc, img)
 
 
    return render(request, 'international.html', context={"mylist":mylist})