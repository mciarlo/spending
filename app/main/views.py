from annoying.decorators import render_to
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


@render_to('index.html')
def index(request):
    return {}


@render_to('login.html')
def custom_login(request):
    errors = []
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('readlists:index'))

        else:
            errors.append('Invalid username or password')

    else:
        form = AuthenticationForm()

    return {
        'errors': errors,
        'form': form
    }
