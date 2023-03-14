from django.shortcuts import render,redirect
from .models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.

def category(request):
    return render(request, 'category.html')

def cattable(request):
    data = Catsample.objects.all()
    return render(request, 'cattable.html', {'data':data})

def getdata(request):
    if request.method == 'POST':
        categoryname = request.POST.get('catname')
        categoryimage = request.FILES['catimage']
        data1 = Catsample(cat_name = categoryname, cat_image = categoryimage)
        data1.save()
        return redirect('cattable')

def editcat(request,id):
    data = Catsample.objects.filter(id=id)
    return render(request, 'editcat.html', {'data':data})

def update(request,id):
    if request.method == 'POST':
        categoryname = request.POST['catname']
        try:
            img_c = request.FILES['catimage']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Catsample.objects.get(id=id).catimage
        Catsample.objects.filter(id=id).update(cat_name = categoryname, cat_image = file)
        return redirect('cattable')

def deletecat(request,id):
    Catsample.objects.filter(id=id).delete()
    return redirect('cattable')

def product(request):
    data = Catsample.objects.all()
    return render(request, 'product.html', {'data':data})

def prdtable(request):
    data = Prdsample.objects.all()
    return render(request, 'prdtable.html', {'data':data})

def gdata(request):
    if request.method == 'POST':
        pname = request.POST.get('prdname')
        pimage = request.FILES['prdimage']
        pprice = request.POST.get('prdprice')
        cat = request.POST.get('prdcat')
        data1 = Prdsample(prd_name = pname, prd_image = pimage, prd_price = pprice, prd_cat = cat)
        data1.save()
        return redirect('prdtable')
    
def editprd(request, id):
    dataC = Catsample.objects.all()
    dataP = Prdsample.objects.filter(id = id)
    return render(request, 'editprd.html', {'dataP':dataP,'dataC':dataC})

def updateprd(request,id):
    if request.method == 'POST':
        pname = request.POST.get('prdname')
        pprice = request.POST.get('prdprice')
        cat = request.POST.get('prdcat')
        try:
            img_c = request.FILES['prdimage']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Prdsample.objects.get(id=id).prdimage
        Prdsample.objects.filter(id = id).update(prd_name = pname, prd_price = pprice, prd_cat = cat, prd_image = file)
        return redirect('prdtable')
    
def deleteprd(request,id):
    Prdsample.objects.filter(id=id).delete()
    return redirect('prdtable')

def index(request):
    dataC = Catsample.objects.all()
    return render(request, 'index.html', {'dataC':dataC})

def table(request, catname):
    data = Prdsample.objects.filter(prd_cat = catname)
    return render(request, 'prdtable.html', {'data':data})