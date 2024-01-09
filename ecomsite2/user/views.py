from django.shortcuts import render, redirect
from .form import UserSignupForm
from django.contrib import messages
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        try:
            user = form.save()
            user.set_password(user.password)
            user.save()
            messages.success(request, f' LogIn to application')
            return redirect('login')
        except:
            messages.error(
                request, f' Something went wrong , Try a strong password!')
            return redirect('signup')
    else:
        form = UserSignupForm()

    context = {
        'form': form
    }
    return render(request, 'registration/signup.html', context)
