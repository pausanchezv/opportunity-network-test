# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.http import require_http_methods
from .forms import PublicationForm

from models import Publication

''' 
This is the application controller, which through queries from the database, provides the information
needed to the templates by rendering the request with a template and giving them a unique context used to
show the information on the website.
'''


@require_http_methods(["GET", "POST"])
def index(request):
    """
    Index view
    It can be accessed via GET: when we first access the web page
    It can also be accessed via POST: when the form is executed
    The view behaviour depends on the http method making the call: get or post.
    Let's take a look at the implementation!
    """

    # if it is called through post method, register the publication will be needed
    if request.method == 'POST':

        # getting the arguments via POST
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        note = request.POST.get('note', '')

        # check whether or not the fields have a real value
        # it also has to be checked here taking into account the fact of how easy avoid the front-end security through the browser console is
        if username.strip() and email.strip():

            # if the user has not filled the note out, a generic message is added
            if not note.strip():
                note = 'This user did not want to write a note!'

            # this is the Django ORM method used to insert elements into the database
            Publication(username=username, email=email, note=note).save()

            # redirect to the publications' page
            return redirect("/test/publications")

    # applications context: in this case it only contains the form
    context = {
        'form': PublicationForm()
    }

    # if it is called via get, the landing page will be shown normally
    return render(request, 'index.html', context)


@require_http_methods("GET")
def publications(request):
    """
    Publications view: it will always be called via http-GET
    :param request:
    :return: render
    """

    # get all the publications from DB
    publications_objects = Publication.objects.all().order_by('id').reverse()

    # create a context containing all the publications
    context = {
        'publications': publications_objects
    }

    # rendering the template
    return render(request, 'publications.html', context)


@require_http_methods("POST")
def remove_publication(request):
    """ This method is reachable via POST but never through GET """

    # get POST object id
    obj_id = request.POST.get('id', None)
    obj_id = obj_id.replace('remove_', '')

    # delete publication from database
    Publication.objects.filter(id=obj_id).delete()

    # returning the id so as to delete the html front-end block
    return HttpResponse(obj_id)



