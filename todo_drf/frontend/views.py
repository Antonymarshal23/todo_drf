from django.shortcuts import render


# Create your views here.
def List(request):
    return render(request, 'frontend/index.html')
