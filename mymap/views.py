from django.shortcuts import render

def home(request):
	return render(request, 'mymap/index.html')

# Create your views here.
