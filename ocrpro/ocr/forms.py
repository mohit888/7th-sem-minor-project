from django import forms 
class ImageForm(forms.Form):
    image = forms.ImageField(help_text="Upload image: ", required=False)
