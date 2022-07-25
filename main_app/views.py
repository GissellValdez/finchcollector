from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Add the following import
from django.http import HttpResponse
from .models import Finch
from .forms import FeedingForm

# views.py
from django.views.generic import ListView

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
    success_url = '/finches/'
class FinchUpdate(UpdateView):
    model = Finch
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['description', 'wingspan']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'

# # Add the Finch class & list and view function below the imports
# class Finch:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name):
#     self.name = name

# finches = [
#   Finch('Lolo'),
#   Finch('Sachi'),
#   Finch('Raven')
# ]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello Screen</h1>')
  
def about(request):
  return render(request, 'about.html')

def finches(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', { 'finches': finches })

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  feeding_form = FeedingForm()
  return render(request, 'finches/detail.html', { 'finch': finch, 'feeding_form': feeding_form })

def add_feeding(request, finch_id):
    # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the finch_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)