from django.shortcuts import render

# Create your views here.


def data_rendor(request):
    data='this is madhu royal'
    d={'madhu':data}
    return render(request,'data.html',context=d)