from django.shortcuts import render
from .forms import DocumentForm
from .forms import SaveForm
from .models import Document
from readpdf import *
import os
# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            doc = form.save(commit = False)
            doc.name = request.FILES['document']
            doc.save()
            filename, file_extension = os.path.splitext('documents/'+str(request.FILES['document']))
            if file_extension != ".pdf":
                form1 = DocumentForm()
                return render(request,'historia1/model_form_error.html',
                {
                'form' : form1
                })

            strng =leer('documents/'+str(request.FILES['document']))
            url = doc.document.url

            document = Document.objects.get(name=doc.name)
            form = SaveForm(instance = document)

            return editar(request, strng, url,form)
    else:
        form = DocumentForm()
    return render(request,'historia1/model_form_upload.html', {
    'form' : form
    })

def editar(request, strng, url, form):
    print("editar")
    if request.method == 'POST':
        #form1 = SaveForm(request.POST)
        print("guardar form 1")

        if form.is_valid():
            print("LLEGUE")
            form.save()
            print("LLEGUE")
            return render(request,'historia1/editar.html',
            {
            'strng' : strng,
            'url' : url,
            'form': form
            })
        else: 
            print("LLEGUE")  
            #form.save()
            return render(request,'historia1/editar.html', {
            'form' : form,
            'strng': strng,
            'url': url
            })
    else:
        return render(request,'historia1/editar.html', {
    'form' : form,
    'strng': strng,
    'url': url
    })
