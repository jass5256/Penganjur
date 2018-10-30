from django.shortcuts import render,redirect,get_object_or_404
from .models import Aktiviti
from .forms import Aktivitiform
from django.db import models
from .models import Aktiviti
from django.urls import reverse_lazy

# Create your views here.

# home penganjur

def home(request):

	#print(request.GET['aktivitiid'])
	a=Aktiviti.objects.all()
	# for ak in a:
	# 	print(ak.tajuk,ak.tempat,ak.penceramah)


	return render(request,'penganjur/home.html',{'aktiviti':a})

def update_aktiviti(request,pk):
	aktiviti=get_object_or_404(Aktiviti.pk)
	aktiviti= Aktiviti(tajuk='Yes Cheddar', tempat='Anywhere', penceramah='anybody',hadpeserta=55)
	aktiviti.save()

	return render(request,'penganjur/home.html')


def delete_penganjur(request):
	aktiviti = get_object_or_404(Aktiviti.pk)

	aktiviti.delete

	return render(request,'penganjur/home.html')

def tambah_penganjur(request):


	akt= Aktiviti(tajuk='Not Cheddar', tempat='Anywhere', penceramah='anybody',hadpeserta=55)
	akt.save()

	return render(request,'penganjur/home.html')


def addaktiviti(request):

	if request.method=="POST":
		form=Aktivitiform(request.POST)
		print(form)
		if form.is_valid():
			aktiviti=form.save(commit=False)
			aktiviti.save()
			return redirect(reverse_lazy('home_penganjur'))		

	else:
		form=Aktivitiform()

	return render(request,'penganjur/tambah_aktiviti.html',{ 'form':form})

def deleteaktiviti(request,pk):

	aktiviti =get_object_or_404(Aktiviti,pk=pk)

	if request.method=="POST":

		if request.POST.get("submit_yes"):
			aktiviti.delete()
			return redirect(reverse_lazy('home_penganjur'))		

	return render(request,'penganjur/delete_aktiviti.html',{ 'aktiviti':aktiviti})


def editaktiviti(request,pk):

	aktiviti =get_object_or_404(Aktiviti,pk=pk)
	if request.method=="POST":
		form=Aktivitiform(request.POST,instance=aktiviti)
		print(form)
		if form.is_valid():
			aktiviti=form.save(commit=False)
			aktiviti.save()
			return redirect(reverse_lazy('home_penganjur'))		

	else:
		form=Aktivitiform(instance=aktiviti)

	return render(request,'penganjur/kemaskini_aktiviti.html',{ 'form':form})
