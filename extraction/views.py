from django.shortcuts import render
from django.shortcuts import render
from .models import UploadedFile
from .forms import UploadFileForm
from .extract import get_text


def home(request):
    '''
    view for uploading pdf/img file and to display results
    '''
    # once user uploads their file, check if valid and process
    if request.method == "POST":
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            # creating instance
            new_file = UploadedFile(file=uploaded_file)
            new_file.save()

            # processing file to csv based on id and file name
            data = get_text(new_file.id,uploaded_file)

            return render(request,'extraction/home.html',{"data":data}) 
    else:
        form = UploadFileForm()
    
    return render(request,'extraction/home.html',{"form":form}) 


