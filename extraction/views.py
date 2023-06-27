from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from .models import UploadedFile
from .forms import UploadFileForm
from .extract import get_text
import os

# Create your views here.

# def home(request):
#     return render(request,"extraction/home")

def home(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            new_file = UploadedFile(file=uploaded_file)
            new_file.save()
            get_text(uploaded_file)

            # TODO: delete the file after operation is complete
            return render(request,'extraction/home.html') 
    else:
        form = UploadFileForm()
    #     text = get_text(request.FILES["myfile"])
    #     return render(request,'extraction/home.html',{"text":text})

    # else:
    #     return HttpResponseBadRequest()
    
    return render(request,'extraction/home.html',{"form":form}) 

