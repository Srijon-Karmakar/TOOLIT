# myapp/forms.py
from django import forms

class DownloadForm(forms.Form):
    url = forms.URLField(label='', widget=forms.TextInput(attrs={'placeholder': 'Paste YouTube video link'}))




