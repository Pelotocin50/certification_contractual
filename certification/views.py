from django.shortcuts import render

# Create your views here.
def home(request):
    ctx = {
        'title': "Servicios en Ingreso",
        }
    return render(request, 'index.html', ctx)