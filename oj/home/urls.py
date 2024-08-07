from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home , name='home'),
    path('problems/', views.problemlist, name='problemlist' ),
    path('problems/<int:id>/', views.problemdetails, name='problemdetails'),
    path('recent-submissions/', views.recent_submissions, name='recent_submissions'),
]