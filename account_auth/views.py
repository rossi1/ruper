from django.shortcuts import render
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
            return redirect('account/home')
        else:
            form = SignupForm()
    context = {'form': form}
    return render(request, 'registration/signup.html',  context=context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            request.session['count'] = 0
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data=['password'])
            if user:
                login(request, user)
                return redirect('account/home')
            else:
                request.session['count'] += 1
                if request.session['count'] != 3:
                    messages.warning(request, 'Invalid Credentials')
                else request.session['count'] == 3:
                    messages.error(request, 'You have entered a wrong credentials more than \
                    3 times please try again in the next 5 minutes'
                    
                    )

        form =  AuthenticationForm()
        context = {'form': form}
        return render(request, 'registration/login.html',  context)


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

