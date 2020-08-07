from django.shortcuts import render, redirect, get_object_or_404
from .forms import JssForm
from .models import Jasoseol
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):

    all_jss = Jasoseol.objects.all()

    return render(request, 'index.html', {'all_jss' : all_jss})

@login_required(login_url='/login')
def create(request):
    if request.method == "POST":
        filled_form = JssForm(request.POST)
        if filled_form.is_valid():
            temp_form = filled_form.save(commit=False)
            temp_form.author = request.user
            temp_form.save()
            return redirect('index')
    else:
        jss_form = JssForm()
        return render(request, 'create.html', {'jss_form' : jss_form})

def detail(request, jss_id):

    jss = get_object_or_404(Jasoseol, pk=jss_id)


    return render(request, 'detail.html', {'jss' : jss })

def delete(request, jss_id):
    
    jss = get_object_or_404(Jasoseol, pk=jss_id)    
    if request.user == jss.author:
        jss.delete()
        return redirect('index')

    raise PermissionDenied

def update(request, jss_id):
    jss = get_object_or_404(Jasoseol, pk=jss_id)
    if request.user != jss.author:
        raise PermissionDenied
    jss_form = JssForm(instance=jss)

    if request.method == "POST":
        updated_form = JssForm(request.POST, instance=jss)
        if updated_form.is_valid():
            updated_form.save()
            return redirect('detail', jss_id)

    return render(request, 'create.html', {'jss_form' : jss_form})