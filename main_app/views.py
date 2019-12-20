from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Record, Comic, Photo, Cphoto
import uuid
import boto3
# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class RecordList(LoginRequiredMixin, ListView):
    def get_queryset(self):
      return Record.objects.filter(user=self.request.user)

class RecordDetail(LoginRequiredMixin, DetailView):
    model = Record

class RecordCreate(LoginRequiredMixin, CreateView):
    model = Record
    fields = ['album_name', 'artist', 'year', 'label', 'condition']

    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class RecordUpdate(LoginRequiredMixin, UpdateView):
  model = Record
  fields = ['album_name', 'artist', 'year', 'label', 'condition']

class RecordDelete(LoginRequiredMixin, DeleteView):
  model = Record
  success_url = '/records/'

class ComicList(LoginRequiredMixin, ListView):
    def get_queryset(self):
      return Comic.objects.filter(user=self.request.user)

class ComicDetail(LoginRequiredMixin, DetailView):
    model = Comic

class ComicCreate(LoginRequiredMixin, CreateView):
    model = Comic
    fields = ['comic_name', 'edition', 'year', 'publisher', 'condition']

    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class ComicUpdate(LoginRequiredMixin, UpdateView):
  model = Comic
  fields = ['comic_name', 'edition', 'year', 'publisher', 'condition']

class ComicDelete(LoginRequiredMixin, DeleteView):
  model = Comic
  success_url = '/comics/'

@login_required
def add_photo(request, record_id):
  S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
  BUCKET = 'catcollector-rpc'
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, record_id=record_id)
      photo.save()
    except:
      print('An error occurred uploading file to S3')
  return redirect('records_detail', pk=record_id)

@login_required
def add_image(request, comic_id):
  S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
  BUCKET = 'catcollector-rpc'
  photo_file = request.FILES.get('photo-file', None)
  print("THIS IS THE PHOTO FILE: ", photo_file)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Cphoto(url=url, comic_id=comic_id)
      photo.save()
    except:
      print('An error occurred uploading file to S3')
  return redirect('comics_detail', pk=comic_id)