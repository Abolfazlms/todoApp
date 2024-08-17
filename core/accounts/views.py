from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login

# Create your views here.
class SignInView(LoginView):
    template_name = "accounts/signin.html"
    fields = "username","password"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("task_list")

class SignUpView(FormView):
    template_name = 'accounts/signup.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("task_list")

    def form_valid(self,form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(SignUpView, self).form_valid(form)
    #receive single object
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task_list')
        return super(SignUpView, self).get(*args, **kwargs)