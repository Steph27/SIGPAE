from django.shortcuts import render, redirect, get_object_or_404
from .forms import DocumentForm, SaveForm, SearchForm, SearchFormProg, ViewProgForm, PASAForm, ViewPASAForm
from .models import Document, Programa
from readpdf import *
from datetime import *
import os
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return render(request, 'historia1/index.html')

def buscar(request):
    return render(request, 'historia1/buscar.html')

def buscar_s(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        docs = False
        if form.is_valid():
            codigo = form.cleaned_data['codigo'].upper()
            year = form.cleaned_data['year']
            trim = form.cleaned_data['trimestre']
            if year is not None:
                docs = Document.objects.all().filter(codigo=codigo,year=year,trimestre=trim,guardar="PASA")
            else:
                docs = Document.objects.all().filter(codigo=codigo,guardar="PASA")
        return render(request, 'historia1/buscar_s.html', {'form': form, 'query': docs})
    else:
        form = SearchForm()
        return render(request, 'historia1/buscar_s.html', {'form': form})

def view_s(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    if doc.guardar == 'TRAN':
        return redirect('index')

    form = ViewPASAForm(request.POST or None, instance=doc)
    return render(request, 'historia1/view_s.html', {'form':form})

def buscar_t(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        docs = False
        if form.is_valid():
            codigo = form.cleaned_data['codigo'].upper()
            year = form.cleaned_data['year']
            trim = form.cleaned_data['trimestre']
            if year is not None:
                docs = Document.objects.all().filter(codigo=codigo,year=year,trimestre=trim,guardar="TRAN")
            else:
                docs = Document.objects.all().filter(codigo=codigo,guardar="TRAN")
        return render(request, 'historia1/buscar_t.html', {'form': form, 'query': docs})
    else:
        form = SearchForm()
        return render(request, 'historia1/buscar_t.html', {'form': form})

def buscar_p(request):
    if request.method == 'POST':
        form = SearchFormProg(request.POST)
        docs = False
        if form.is_valid():
            codigo = form.cleaned_data['codigo'].upper()
            year = form.cleaned_data['fecha_vigano']
            trim = form.cleaned_data['fecha_vigtrim']
            if year is not None:
                docs = Programa.objects.all().filter(codigo=codigo, fecha_vigtrim=trim, fecha_vigano=year)
            else:
                docs = Programa.objects.all().filter(codigo=codigo)
        return render(request, 'historia1/buscar_p.html', {'form': form, 'query': docs})
    else:
        form = SearchFormProg()
        return render(request, 'historia1/buscar_p.html', {'form': form})

def model_form_upload(request):
    error = ""
    scan=False
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if request.POST.get('scanned') == 'on':
            scan = True

        if form.is_valid():
            doc = form.save(commit = False)
            doc.name = request.FILES['document']
            filename, file_extension = os.path.splitext('documents/'+str(request.FILES['document']))
            if file_extension != ".pdf":
                form1 = DocumentForm()
                error = "UN ERROR HA OCURRIDO, ARCHIVO EN FORMATO ERRONEO"
                return render(request,'historia1/model_form_upload.html',
                {
                'form' : form1,
                'error': error
                })
            #try: 
                #search = Document.objects.get(name=doc.name)
                #form1 = DocumentForm()
                #error = "ERROR. YA EXISTE UN ARCHIVO CON ESE NOMBRE"
                #return render(request,'historia1/model_form_upload.html',
                #{
                #'form' : form1,
                #'error': error
                #})
            #except Document.DoesNotExist:
                #pass
            doc.save()
            if scan:
                strng = leerImg('documents/'+str(request.FILES['document']))
            else:
                strng = leer('documents/'+str(request.FILES['document']))

            doc.pdf_to_text = strng
            doc.save()

            document = Document.objects.get(name=str(request.FILES['document']))

            return redirect('editar_t', document.id)
    else:
        form = DocumentForm()
    return render(request,'historia1/model_form_upload.html', {
    'form' : form, 'error': error
    })

def view_p(request, pk):
    prog = get_object_or_404(Programa, pk=pk)
    form = ViewProgForm(request.POST or None, instance=prog)
    return render(request, 'historia1/view_p.html', {'form':form})

def editar_t(request, pk):
    ## TODO
    # GUARDAR STRNG SI LO MODIFICO !!
    doc = get_object_or_404(Document, pk=pk)
    url = doc.document.url
    strng = doc.pdf_to_text

    if doc.guardar == 'PASA':
        return redirect('index')

    form = SaveForm(request.POST or None, instance=doc)
    if form.is_valid():
        month = 1
        if form.cleaned_data['trimestre'] == 'EM':
            month = 1
        elif form.cleaned_data['trimestre'] == 'AB':
            month = 4
        elif form.cleaned_data['trimestre'] == 'SD':
            month = 9

        if form.cleaned_data['year'] is not None: 
            fecha = date(form.cleaned_data['year'], month, 1)
            temp.fecha = fecha

        temp = form.save(commit=False)
        temp.codigo = form.cleaned_data['codigo'].upper()
        temp.save()

        # PARA PASA => VERIFICAR QUE CAMPOS OBLI NO VACIOS, OTRAS RESTRICCIONES
        if form.cleaned_data['guardar'] == 'PASA':
            return redirect('form_pasa', pk)
        else:
            return redirect('editar_t', pk)

    return render(request, 'historia1/editar.html', {'strng': strng, 'url': url, 'form_s': form})

def form_pasa(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    form = PASAForm(request.POST or None, instance=doc)
    
    if form.is_valid():
        form.save()
        return redirect('index')
        
    return render(request, 'historia1/pasa.html', {'form':form, 'pk':pk})



   