from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Add the Finch class & list and view function below the imports
class Finch:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name):
    self.name = name

finches = [
  Finch('Lolo'),
  Finch('Sachi'),
  Finch('Raven')
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Home Screen</h1>')
  
def about(request):
  return render(request, 'about.html')

def all(request):
  return render(request, 'finches/index.html', { 'finches': finches })