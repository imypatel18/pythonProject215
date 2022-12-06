from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="indexfile"),
    path('aboutus',views.about,name="aboutusfile"),
    path('sports',views.sports,name="sports")
]