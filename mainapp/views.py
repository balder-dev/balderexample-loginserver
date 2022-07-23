from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def intern(request):
    """View function for home page of site."""

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'intern.html',
        context={'num_visits': num_visits})
