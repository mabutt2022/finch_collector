from django.shortcuts import render
from .models import Finch

# Create your views here.
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

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