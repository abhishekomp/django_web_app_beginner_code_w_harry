from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
  context = {
    "variable1": "This is variable 1 value",
    "variable2": "This is variable 2 value",
  }
  #return render(request, 'index.html')
  return render(request, 'index.html', context)
  #return HttpResponse("Home page for Hello app version 1")
def about(request):
  return render(request, 'about.html')
def services(request):
  return render(request, 'services.html')
def contact(request):
  return render(request, 'contact.html')
