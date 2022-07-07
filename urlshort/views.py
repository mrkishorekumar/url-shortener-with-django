from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import urlModels
from random import sample

# Create your views here.
def HomePage(request):
    return render(request,"index.html")


def makeShortUrl(request):
    if request.method=="POST":
        longurl = request.POST["longurl"]

        base62 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        shorturl = "".join(sample(base62,7))

        obj = urlModels.objects.create(longurl = longurl,shorturl = shorturl)
        print("Created")
    return render(request,"shorturl.html",{"longurl":longurl,"shorturl":shorturl})

def redirectURL(request,shorturl):
    try:
        obj = urlModels.objects.get(shorturl=shorturl)
    except urlModels.DoesNotExist:
        obj = None

    
    if obj is not None:
        obj.count+=1
        obj.save()
        return redirect(obj.longurl)
    else:
        return render(request,"404.html")

