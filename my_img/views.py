from django.shortcuts import render,redirect
from . forms import imgform
from . models import up_img

# Create your views here.
def home(request):
    if request.method == "POST":
        form = imgform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = imgform()
    img = up_img.objects.all()
    return render(request, 'my_img/home.html',{'img':img,'form':form})

def delete(request):
    pass