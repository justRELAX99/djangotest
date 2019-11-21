from django.forms import ModelForm,TextInput

from .models import city

class CityForm(ModelForm):
    class Meta:
        model=city
        fields=['name']
        widgets={'name':TextInput(attrs={
            'class':'form-control',
            'name':'city',
            'id':'city',
            'placeholder':'Введите город'
        })}