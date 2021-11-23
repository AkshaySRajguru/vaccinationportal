from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

from .models import Person
from .forms import PersonForm


def home(request):
    return render(request, 'home.html')


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
            messages.success(request, 'Vaccination details of a {} added successfully.'.format(person_object.data['name']))
        return redirect('dashboard')
    return render(request, 'add-vaccine-details.html', {'person_object': person_object})


def update_view(request, pk):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Person, id=pk)

    # pass the object as instance in form
    form = PersonForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to dashboard view
    if form.is_valid():
        form.save()
        messages.success(request, 'Vaccination details of a {} updated successfully.'.format(str(obj)))
        return redirect('dashboard')

    # add form dictionary to context
    context['person_object'] = form

    return render(request, 'add-vaccine-details.html', context)


def delete_view(request, pk):
    # dictionary for initial data with
    # field names as keys
    context = {}
    # fetch the object related to passed id
    obj = get_object_or_404(Person, id=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Vaccination details of a {} deleted successfully.'.format(str(obj)))
        return redirect('dashboard')

    context['object'] = obj
    return render(request, 'delete_template.html', context)
