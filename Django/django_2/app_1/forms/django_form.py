from django import forms
from ..models import User

# class UserForm(forms.Form):
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=30)
#     email = forms.EmailField()
#     password = forms.CharField(max_length=20)
#     confirm_password = forms.CharField(max_length=30)
'''
to save the user automatically in the database first we have to connect the form 
with a model in which the form will be saved and to do this we can create 
a form of parent forms.ModelForm.
'''
class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
    confirm_password = forms.CharField(max_length=30)
    # now we have to define the model in which the form will be saved.
    # to do this we need to make a class of name Meta.
    class Meta:
        # after importing the model we need to use.
        model = User
        # define that how many fields should be saved.
        # selecting custom fields:
        # fields = ('first_name','last_name')
        # selecting all fields:
        fields = ('__all__')