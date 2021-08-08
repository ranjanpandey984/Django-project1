from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
	views = {}
	views['comments'] = Review.objects.all()  #Review bhanney model name
	return render(request,'index.html',views)

def about(request):
	return render(request,'about.html')

def contact(request):
	if request.method == 'POST':
		name = request.POST['name']   #agadiko name variable ho pachadi ko name form ko input tag ko name ho
		email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']
		data = Contact.objects.create(
			name = name,  #agadiko name model ko name ho pachadiko name mathiko variable ho
			email = email,
			subject = subject,
			message = message
			)	
		data.save()
	views = {}
	views['infos'] = Info.objects.all()  #infos j rakhda ni huncha and Info bhanney model name
	return render(request,'contact.html',views)

def portfolio(request):
	return render(request,'portfolio.html')

def price(request):
	return render(request,'price.html')

def services(request):
	return render(request,'services.html')