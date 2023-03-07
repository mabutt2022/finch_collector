from django.shortcuts import render, redirect
import uuid
import boto3
from .models import Finch, Features, Photo
from .forms import FeedingForm
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import  ListView, DetailView

S3_BASE_URL = 'https://s3.us-west-1.amazonaws.com/'
BUCKET = 'finchcollector2023'

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
#  inserting Feeding Form into the detail function
   feeding_form = FeedingForm()
   feature_finch_does_not_have = Features.objects.exclude(id__in = finch.strength.all().values_list('id'))
  #  print(finch)
   return render(request, 'finches/detail.html', 
                 {'finch': finch, 'feeding_form':feeding_form,
                  'features': feature_finch_does_not_have})

def add_feeding(request, finch_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)

def assoc_feature(request, finch_id, feature_id):
   Finch.objects.get(id=finch_id).strength.add(feature_id)
   return redirect('detail', finch_id=finch_id)

def add_photo(request, finch_id):
  # photo-file will be the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
      s3 = boto3.client('s3')
      # need a unique "key" for S3 / needs image file extension too
      key = 'finchcollector2023/' + uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
      # just in case something goes wrong
      try:
          s3.upload_fileobj(photo_file, BUCKET, key)
          # build the full url string
          url = f"{S3_BASE_URL}{BUCKET}/{key}"
          # we can assign to finch_id or cat (if you have a finch object)
          #  the below finch_id = finch_id refers to the finch_id from Finch Model
          Photo.objects.create(url=url, finch_id=finch_id)
      except:
          print('An error occurred uploading file to S3')
  return redirect('detail', finch_id=finch_id)

class FinchCreate(CreateView):
   model = Finch
   fields = ['name', 'habitat', 'nesting', 'behavior', 'conservation', 'description']

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

class FeatureList(ListView):
  model = Features

class FeatureDetail(DetailView):
  model = Features

class FeatureCreate(CreateView):
  model = Features
  fields = '__all__'

class FeatureUpdate(UpdateView):
  model = Features
  fields = ['strength', 'characteristic']

class FeatureDelete(DeleteView):
  model = Features
  success_url = '/features/'

