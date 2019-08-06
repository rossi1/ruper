from django.shortcuts import render, reverse
from django.contrib.auth.forms  import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from django.contrib import messages


from .forms import SignupForm

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    else:
        form = SignupForm()

   
    return render(request, 'registration/signup.html', {'form': form})


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

