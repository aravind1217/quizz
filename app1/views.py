from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Exam
from .forms import UserRegisterForm
def home(request):
	exam = Exam.objects.all()
	return render(request,'base.html',{"exam":exam})
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration.html', {'form': form})



