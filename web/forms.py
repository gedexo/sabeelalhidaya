from django import forms
from .models import Contact
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
        widgets={
            'name':TextInput(attrs={'placeholder':"Your Name", 'name':"your-name",'type':'text','required':'required'}),

            'phone':TextInput(attrs={'placeholder':"Cell Phone", 'name':'your-phone', 'type':'text','required':'required'}),

            'email':EmailInput(attrs={'placeholder':"Email", 'name':'email', 'type':'email', 'required':'required'}),

            'address':TextInput(attrs={'placeholder':"Venue ", 'type':'text','name':"venue",'required':'required'}),

            'message':Textarea(attrs={'placeholder':"Message",'cols':'20', 'name':"message", 'required':'required'}),
         }