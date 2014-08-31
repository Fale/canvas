from django import forms
from canvas.models import BUNDLES

class CanvasForm(forms.Form):
    name = forms.CharField(max_length=200)

class ItemForm(forms.Form):
    title = forms.CharField(max_length=200)
    bundle = forms.CharField(max_length=3, widget=forms.Select(choices=BUNDLES))
