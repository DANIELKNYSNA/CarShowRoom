from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def showroom(request):
  context = {}
  return render(request, 'showroom/showroom.html', context)