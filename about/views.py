from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#this is the about view
def about(request):
    return HttpResponse("This would be a perfect view")