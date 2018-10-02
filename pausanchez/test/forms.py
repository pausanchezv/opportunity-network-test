# -*- coding: utf-8 -*-

from django import forms

''' 
As it was asked at the office a Django form has been created including the three compelled fields 
The last one is not mandatory to be filled out, following David's instructions. It means that
the form can be sent having only filled out the username and email fields. In this case, a generic message
will appear when listing the posts on the website.
'''


class PublicationForm(forms.Form):
    """ Publication form class """

    username = forms.CharField(label='Username', max_length=20, required=True)
    email = forms.EmailField(label='Email', max_length=50, required=True)
    note = forms.CharField(label="Write your note", widget=forms.widgets.Textarea(), required=False)

