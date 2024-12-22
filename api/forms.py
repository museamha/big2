from django import forms

from .models import Field



class formt(forms.ModelForm):
    class Meta:
        model = Field
        fields = "__all__"
        
    