from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Contact
from .forms import UserForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class ContactListView(LoginRequiredMixin, ListView):
    model = Contact
    context_object_name = 'contacts'

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    fields = ['name', 'email','telephone', 'relation', 'residence', 'cover', 'is_male']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ContactUpdateView(UpdateView):
    model = Contact
    fields = ['name', 'email', 'telephone', 'relation', 'residence', 'cover', 'is_male']


class ContactDeleteView(DeleteView):
    model = Contact
    success_url = '/'


def signup(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = form.save(commit=False)
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('phonebook:contact-index')

    return render(request, 'phonebook/signup.html', {'form': form})

