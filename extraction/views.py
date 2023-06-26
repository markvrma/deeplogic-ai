from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from .forms import UploadFileForm
from .extract import get_text

# Create your views here.

# def home(request):
#     return render(request,"extraction/home")

def home(request):
    if request.method == "POST":
        text = get_text(request.FILES["myfile"])
        return render(request,'extraction/home.html',{"text":text})

    # else:
    #     return HttpResponseBadRequest()
    
    return render(request,'extraction/home.html') 

