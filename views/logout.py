from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.utils import simplejson
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from canvas.models import Canvas, Item
from canvas.forms import CanvasForm, ItemForm, ExtendedItemForm

def user_logout(request):
    logout(request)
    return redirect('/')

