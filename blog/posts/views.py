from django.shortcuts import render

# Create your views here.
def home(request):
	retuen render(request, 'posts/home.html')