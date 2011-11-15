from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm

import jingo

def register(request):
    """Register a new user."""
    form = handle_register(request)
    if form.is_valid():
        return jingo.render(request, 'accounts/register_done.html')
    return jingo.render(request, 'accounts/register.html',
                        {'form': form})


def handle_register(request):
    """Handle to help registration."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return form
    return UserCreationForm()
