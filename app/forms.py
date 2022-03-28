from django import forms
from .models import UserModel

class UserForm(forms.ModelForm):
    name = forms.CharField(label='Your Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name Here'}), required=True, error_messages={'required':'Must Enter a Correct Name'})
    address = forms.CharField(label='You Address', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Your Address Here', 'rows':3, 'cols': 50}), error_messages={'required':'Must Enter a Correct Address'})
    bloodgrp = forms.CharField(label='Your Blood group', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Bloodgrp Here'}), required=True, error_messages={'required':'Must Enter a Correct Bloodgrp'})
    # image = forms.ImageField()
    
    # docfile = forms.FileField(
    #     label='Select a file',
    #     help_text='max. 42 megabytes'
    # )
    
    class Meta:
        model = UserModel
        fields = '__all__'
        widgets = {
            
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email Here'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Mobile Here'}),
            'standard': forms.Select(attrs={'class': 'form-control'}),
            'classs': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'hobby': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }
        error_messages = {
            'gender' : { 'required' : 'Must Select a Gender'},
            'email' : { 'required' : 'Enter Correct Email'},
            'hobby' : { 'required' : 'Select Language You Know'},
            # 'image' : { 'required' : 'Must Select an Image'},
        }

