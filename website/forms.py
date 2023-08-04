from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)
        
        self.fields["username"].widget.attrs["class"] = "input100"
        self.fields["username"].widget.attrs["placeholder"] = "Username"

        self.fields["email"].widget.attrs["class"] = "input100"
        self.fields["email"].widget.attrs["placeholder"] = "Email"

        self.fields["password1"].widget.attrs["class"] = "input100"
        self.fields["password1"].widget.attrs["name"] = "password1"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"

        self.fields["password2"].widget.attrs["class"] = "input100"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm Password"


class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required = True, widget = forms.widgets.TextInput(attrs={'placeholder':"First Name","class":"form-control"}), label="")
    last_name = forms.CharField(required = True, widget = forms.widgets.TextInput(attrs={'placeholder':"Last Name","class":"form-control"}), label="")
    email = forms.CharField(required = True, widget = forms.widgets.TextInput(attrs={'placeholder':"Email","class":"form-control"}), label="")
    phone = forms.CharField(required = True, widget = forms.widgets.TextInput(attrs={'placeholder':"Phone","class":"form-control"}), label="")
    address = forms.CharField(required = True, widget = forms.widgets.TextInput(attrs={'placeholder':"Address","class":"form-control"}), label="")
    city = forms.CharField(required = True, widget = forms.widgets.TextInput(attrs={'placeholder':"City","class":"form-control"}), label="")
    state = forms.CharField(required = True, widget = forms.widgets.TextInput(attrs={'placeholder':"State","class":"form-control"}), label="")
    zipcode = forms.CharField(required = True, widget = forms.widgets.TextInput(attrs={'placeholder':"Zipcode","class":"form-control"}), label="")

    class Meta:
        model = Record
        exclude = ("user",)
     



    