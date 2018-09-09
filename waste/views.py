from django.shortcuts import render
from waste.forms import complain_form

def complainview(request):
	return render(request, 'waste/complain.html')

def submit(request):
	 form = complain_form(request.POST or None)
	 if form.is_valid():
	 	form.save()
	 	return render(request, 'waste/complain.html')

