from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def indexView2(request):
    return render(request,'accounts/home.html')

#@login_required()
def dashboardView(request):
    return render(request,'accounts/dashboard.html')

def registerView(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_urls')
    else:
        form=UserCreationForm()
    return render(request,'accounts/register.html',{'form':form})

def loginView(request):
    return render(request,'accounts/login.html')
#
# def loginout(request):
#     return render()
