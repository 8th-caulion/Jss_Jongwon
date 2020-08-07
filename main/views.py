from django.shortcuts import render, redirect
from .forms import JssFormm

# Create your views here.
def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method == "POST":
        filled_form = JssFormm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('index')
    else:
        jss_form = JssFormm()
        return render(request, 'create.html', {'jss_form' : jss_form})