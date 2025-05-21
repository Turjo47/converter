from django.shortcuts import render

# Create your views here.
def convert(request):
    return render (request,"converter_core/convert.html")