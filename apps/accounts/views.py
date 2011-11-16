from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
#from django.contrib.auth.decorators import logout_required
from django.contrib.auth.forms import UserCreationForm

import jingo
from session_csrf import anonymous_csrf


#@logout_required
@anonymous_csrf
def register(request):
    """Register a new user."""
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('landings.home'))
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
