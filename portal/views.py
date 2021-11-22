from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Person
from .forms import PersonForm


def home(request):
    return render(request, 'home.html', {"name": "Akshay"})


def dashboard(request):
    person_object = Person.objects.all().order_by('-id')
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


def add_vaccine_details(request):
    person_object = PersonForm()
    if request.method == 'POST':
        person_object = PersonForm(request.POST, request.FILES)
        if person_object.is_valid():
            person_object.save()
        return redirect('home')
    return render(request, "add-vaccine-details.html", {'person_object': person_object})
