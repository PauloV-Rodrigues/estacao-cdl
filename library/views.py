from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import logout
from .models import *
from .forms import *
from .decorators import *

def BookList(request):
	data = Book.objects.all()
	booking = {
		"book_list": data
	}

	return render(request, 'library/book_list.html', booking)

class BookDetail(DetailView):
	model = Book

def registerPage(request):	
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='student')
			user.groups.add(group)

			messages.success(request, 'Account was created for ' + username)
			
			return redirect('library:login')	
	
	form = CreateUserForm()
	return render(request, 'library/register.html', context={'form':form})

def contactPage(request):
    form = ContactForm()
    context = {'form': form}
    return render(request, 'library/contact.html', context)

def loginPage(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('library:home')
			else:
				messages.info(request, 'Username OR password is incorrect')

	form = AuthenticationForm()
	return render(request, 'library/login.html', context={"login_form":form})

def logoutPage(request):
	logout(request)
	return render(request, 'library/login.html')

@login_required
def profilePage(request):
	return render(request, 'library/profile.html')
