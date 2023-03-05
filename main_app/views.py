from django.shortcuts import render
from .models import Finch
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finch_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', { 'finches': finches })

def finch_detail(request, finch_id):
    # cat_id is coming from the url definition
    # in urls.py
    # <int:cat_id>
    finch = Finch.objects.get(id=finch_id)
    print(finch)
    return render(request, 'finches/detail.html', {'finch': finch})

class FinchCreate(CreateView):
   model = Finch
   fields = '__all__'

   def __str__(self):
      return self.name
   
   def get_absolute_url(self):
      return reverse('detail', kwargs={'finch_id': self.id})
   
class FinchUpdate(UpdateView):
   model = Finch
   fields = ['habitat', 'behavior', 'nesting']

class FinchDelete(DeleteView):
   model = Finch
   success_url = '/finch/'
