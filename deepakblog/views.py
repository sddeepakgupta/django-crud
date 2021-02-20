from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.serializers import serialize
from deepakblog.forms import *
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

# def login(request):
#     if not request.user.is_authenticated:
#         fm = AuthenticationForm()
#         return render(request, 'deepakblog/login.html', {'form':fm})
#     else:
#         return redirect('/')       
def userlogin(request):
    if request.method == "POST":
        fm = AuthenticationForm(request = request, data = request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                # A backend authenticated the credentials
                login(request, user)
                messages.success(request, 'login sucessfully!!')
                return redirect('/')
            else:
                messages.info(request, 'User Name and password is incorrect')
    fm = AuthenticationForm()
    return render(request, 'deepakblog/login.html', {'form':fm})

    # Musician Details Add Edit
def userLogout(request):
        logout(request)
        return redirect('deepakblog:userlogin')
@login_required(login_url='deepakblog:userlogin')    
def index(request):
    if request.method =='POST' and request.POST.get('mid'):
        mId = request.POST.get('mid')
        Musiciandata = Musician.objects.get(pk=mId)
        serializedData = serialize('json', [ Musiciandata, ])
        return HttpResponse(serializedData)
    elif request.method =='POST':
        if request.POST.get('EditId'):
            EditId = request.POST.get('EditId')
            cmaster = Musician.objects.filter(pk=EditId).update(first_name = request.POST.get('first_name'), last_name = request.POST.get('last_name'), instrument = request.POST.get('instrument'))
            messages.success(request, 'Musician data updated sucessfully!!')
            return redirect('/')
        else:
            fm = MusicianForm(request.POST)
            if fm.is_valid():
                fn = fm.cleaned_data['first_name']
                fl = fm.cleaned_data['last_name']
                ins = fm.cleaned_data['instrument']
                reg = Musician(first_name = fn, last_name = fl, instrument = ins)
                messages.success(request, 'Musician data added sucessfully!!')
                reg.save()
                fm = MusicianForm()
    else:
        fm = MusicianForm()
    music = Musician.objects.all()
    current_user = request.user
    # print (current_user.id)
    return render(request, 'deepakblog/index.html', {'form': fm, 'music': music ,'name':request.user})
    
    # Delete Musician Records
@login_required(login_url='deepakblog:userlogin')
def musicianDelete(request):
    if request.method=='POST':
        musicID = request.POST.get('musicID')
        musicianDel = Musician.objects.filter(pk=musicID).delete()
        # print(musicianDel)
        messages.success(request, 'Musician data deleted sucessfully!!')
        return redirect('/')
# products Page

@login_required(login_url='deepakblog:userlogin')
def productMaster(request):
    return render(request, 'deepakblog/products.html')

@login_required(login_url='deepakblog:userlogin')
def productMasterDetails(request):
    if request.method == 'POST':
        forms = productMasterForm(request.POST, request.FILES)
        if forms.is_valid():
            handle_uploaded_file(request.FILES['file'])
            messages.success(request, 'Product saved sucessfully!!')
            forms.save()
            forms = productMasterForm()
    forms = productMasterForm()
    context = {'Productform': forms}
    return render(request, 'deepakblog/productMasterDetails.html', context)    

