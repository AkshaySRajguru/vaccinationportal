from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *


def home(request):
    return render(request, 'home.html', {"name": "Akshay"})


def dashboard(request):
    person_object = Person.objects.all()
    paginator = Paginator(person_object, 4)
    page = request.GET.get('page')
    try:
        persons = paginator.page(page)
    except PageNotAnInteger:
        persons = paginator.page(1)
    except EmptyPage:
        persons = paginator.page(paginator.num_pages)

    context = {'person_object': person_object, 'persons': persons}
    return render(request, 'dashboard.html', context)
