from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
	if request.method =='EVENTS':
		form = UserRegisterForm(request.EVENT)
		if form.is_valid():
			form.save(commit=True)
			username = form.cleaned_data.get('username')
			messages.success(request, f'{ username }')
			return redirect('/login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})
