from django import forms

class CanvasForm(forms.Form):
    name = forms.CharField(max_length=256)
