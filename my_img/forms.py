from django import forms 
from . models import up_img

class imgform(forms.ModelForm):
    class Meta:
        model = up_img
        fields = '__all__'
        labels = {'Image':''}
        widgets = {
            'Image': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',  # Bootstrap class or any custom class
                'style': 'display: inline-block;',  # Ensures it stays inline
            })
        }