from django.urls import path
from .views import * 
 
urlpatterns = [
path('', Index, name = 'Index'),
path('register', register, name='register'),
path('login', login, name='login'),
path('logout', logout, name='logout'),
path('sports', sports, name='sports'),
path('technology', technology, name='technology'),
path('buisness', buisness, name='buisness'),
path('international', international, name='international')
]

