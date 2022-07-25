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
