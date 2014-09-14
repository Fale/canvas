from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.utils import simplejson
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseForbidden
from canvas.models import Canvas, Item
from canvas.forms import CanvasForm, ItemForm, ExtendedItemForm

@login_required
def edit(request, canvas_id, item_id = None, box = None):
    if item_id:
        canvas = get_object_or_404(Canvas, pk=canvas_id)
        item = get_object_or_404(Item, pk=item_id)
        if item.canvas != canvas:
            return HttpResponseForbidden()
        if item.canvas.owner != request.user:
            return HttpResponseForbidden()
    else:
        canvas = get_object_or_404(Canvas, pk=canvas_id)
        item = Item(canvas=canvas, box=box)

    if request.POST:
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('showCanvas', canvas_id)
    else:
        if item_id:
            form = ExtendedItemForm(instance=item)
        else:
            form = ItemForm(instance=item)

    return render(request, 'canvas/add.html', {
        'form': form,
    })


@login_required
def delete(request, canvas_id, item_id):
    try:
        item = Item.objects.get(id=item_id)
        canvas = Canvas.objects.get(id=canvas_id)
        if item.canvas.id != canvas.id:
            raise Exception('item is not part of this canvas')
        if item.canvas.owner != request.user:
            raise Exception('item is not owned by user')
    except ObjectDoesNotExist:
        return HttpResponse('{"status": "error", "code": "item does not exists"}', mimetype='application/json')
    except Exception as inst:
        return HttpResponse('{"status": "error", "code": "' + str(inst) + '"}', mimetype='application/json')
    item.delete()
    return HttpResponse('{"status": "success"}', mimetype='application/json')

