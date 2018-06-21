from django import forms
from .models import Subscribers

class SubForms(forms.ModelForm):
    class Meta:
        model = Subscribers
        #fields = [""]   #Поля которые необходимо включить, можно указать все через запятую
        exclude = [""]   #Поля которые необходимо исключить, если не указать, покажет все