from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from deepakblog.forms import *
from .models import *


# Create your views here.


def index(request):
    if request.method =='POST':
        fm = MusicianForm(request.POST)
        if fm.is_valid():
            fn = fm.cleaned_data['first_name']
            fl = fm.cleaned_data['last_name']
            ins = fm.cleaned_data['instrument']
            reg = Musician(first_name = fn, last_name = fl, instrument = ins)
            reg.save()
            fm = MusicianForm()
    else:
        fm = MusicianForm()
    music = Musician.objects.all()
    return render(request, 'deepakblog/index.html', {'form': fm, 'music': music})

# Delete Musician Records

def musicianDelete(request, id):
    musicianDel = Musician.objects.get(pk=id)
    musicianDel.delete()
    return render(request, 'deepakblog/index.html')


