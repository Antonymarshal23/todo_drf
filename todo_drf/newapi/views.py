from django.shortcuts import render


# Create your views here.
def newList(request):
    return render(request, 'newapi/list.html')