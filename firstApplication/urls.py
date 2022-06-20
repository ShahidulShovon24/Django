from django.conf.urls import url
from django.urls import path
from firstApplication import views

app_name = 'firstApplication'

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.details, name = 'details'),
    path('form/', views.form, name = 'form'),

]
