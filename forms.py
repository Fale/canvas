from django.forms import ModelForm
from canvas.models import Canvas, Item

class CanvasForm(ModelForm):
    class Meta:
        model = Canvas
        fields = ['name']

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'bundle']

class ExtendedItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'box', 'bundle']
