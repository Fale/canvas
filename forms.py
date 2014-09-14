from django.forms import ModelForm
from canvas.models import Canvas, Item

class CanvasForm(ModelForm):
    class Meta:
        model = Canvas
        exclude=['owner']

class ItemForm(ModelForm):
    class Meta:
        model = Item
        exclude = ['canvas', 'box']

class ExtendedItemForm(ModelForm):
    class Meta:
        model = Item
        exclude = ['canvas']
