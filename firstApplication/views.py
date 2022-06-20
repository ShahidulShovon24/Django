from django.shortcuts import render
from django.http import HttpResponse
from firstApplication.models import StudentList
from firstApplication import forms


def index(request):
    student_list = StudentList.objects.order_by('First_Name')
    diction = {'textOne': 'Student List of Cardif Metropolitan University',
    'student': student_list}
    return render(request, 'firstApplication/index.html', context=diction)


def form(request):
    new_form = forms.StudentList()
    
    if request.method == 'POST':
        new_form = forms.StudentList(request.POST)
        
        if new_form.is_valid():
            new_form.save(commit = True) 
            return index(request)
        
    diction = {'test_form' : new_form}
    return render(request, 'firstApplication/form.html', context=diction) 

def details(request):
    another_form = forms.user_login()
    diction = {'login_form': another_form}
    
    if request.method == 'POST':
        another_form = forms.user_login(request.POST)
        
        if another_form.is_valid():
            
            email = another_form.cleaned_data['email']
            password = another_form.cleaned_data['password']
            
            diction.update({'email' : email})
            diction.update({'password': password})
            diction.update({"form_submitted" : "yes"})
    
        return render(request, 'firstapplication/form.html', context=diction)