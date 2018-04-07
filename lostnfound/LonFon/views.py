from django.shortcuts import render
from . import models
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView
from . import forms

# Create your views here.


def home(request):

    return HttpResponse('ok')


def add_entry(request):
    if request.method=='POST':
        form = forms.Add(request.POST)
        if form.is_valid():
            '''add a functionality to check the date entered '''
            form.save()
            return HttpResponse('Added')
        else:
            error = 'Invalid Entries'
            return HttpResponse(render(request,'add_entry.html',{'form':form,'error':error}))
    else:
        form = forms.Add()
        return HttpResponse(render(request,'add_entry.html',{'form':form}))


def search(request):
    if request.method == 'POST':
        form = forms.Search(request.POST)
        if form.is_valid():
            lrf = form.cleaned_data['lost_or_found']
            date = form.cleaned_data['date']
            subject = form.cleaned_data['subject']
            location = form.cleaned_data['location']
            if not lrf and not date and not subject and not  location:
                return HttpResponse('None')
            a=models.LostAndFound.objects.all()
            if lrf:
                a=a.filter(lost_or_found=lrf)
            if subject:
                a=a.filter(subject__icontains=subject)
            if location:
                a=a.filter(location__icontains=location)
            if date:
                a=a.filter(date=date)
            form=forms.Search()
            return HttpResponse(render(request,'unified.html',{'search':form,'query':a}))
        else:
            return HttpResponse(render(request,'unified.html',{'search':form}))
        #return HttpResponse('ok')
    else:
        form = forms.Search()
        return HttpResponse(render(request,'unified.html',{'search':form,}))