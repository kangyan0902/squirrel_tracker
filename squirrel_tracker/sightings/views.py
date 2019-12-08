from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView

from .models import Squirrel
from .forms import SquirrelForm


# Create your views here.

def list_of_squirrels(request):
	list_squirrels = Squirrel.objects.all()
	context = {'squirrels': list_squirrels}
	return render(request, 'sighting/list_squirrels.html', context)

def edit_squirrel(request, squirrel_id):
	squirrel = get_object_or_404(Squirrel, Unique_Squirrel_ID=squirrel_id)
	if request.method=='Post':
		form = SquirrelForm(request.POST, instance=squirrel)
		if form.is_valid():
			form.save()
			return redirect(f'/sighting/{squirrel_id}')
	else:
		form = SquirrelForm(instance=squirrel)
	context ={
		'form':form
			}
	return render(request, 'sighting/edit.html', context)

def add_squirrel(request):
	if request.method=='Post':
		form = SquirrelForm(request.POST, instance=squirrel)
		if form.is_valid():
			form.save()
			return redirect(f'/sighting/')
	else:
		form = SquirrelForm()
	context ={
		'form':form
			}
	return render(request, 'sighting/add_squirrel.html', context)
