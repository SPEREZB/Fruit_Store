from django import forms
from .models import FruitsModel
 
class FruitsForm(forms.ModelForm):  
    class Meta: 
        model = FruitsModel 
        fields = '__all__' 