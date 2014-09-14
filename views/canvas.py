from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.utils import simplejson
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from canvas.models import Canvas, Item
from canvas.forms import CanvasForm, ItemForm, ExtendedItemForm

@login_required
def list(request):
    canvas_list = Canvas.objects.all().filter(owner=request.user).order_by('name')
    context = {'canvas_list': canvas_list}
    return render(request, 'canvas/index.html', context)

@login_required
def show(request, canvas_id):
    canvas = get_object_or_404(Canvas, id = canvas_id)
    context = {
        'canvas': canvas,
        'kps': canvas.items.filter(box = "KP"),
        'kas': canvas.items.filter(box = "KA"),
        'krs': canvas.items.filter(box = "KR"),
        'vps': canvas.items.filter(box = "VP"),
        'crs': canvas.items.filter(box = "CR"),
        'chs': canvas.items.filter(box = "CH"),
        'css': canvas.items.filter(box = "CS"),
        'csss': canvas.items.filter(box = "CSS"),
        'rsss': canvas.items.filter(box = "RSS"),
    }
    return render(request, 'canvas/canvas.html', context)

@login_required
def edit(request, canvas_id = None):
    if canvas_id:
        canvas = get_object_or_404(Canvas, pk=canvas_id)
        if canvas.owner != request.user:
            return HttpResponseForbidden()
    else:
        canvas = Canvas(owner=request.user)

    if request.POST:
        form = CanvasForm(request.POST, instance=canvas)
        if form.is_valid():
            form.save()
            return redirect('listCanvas')
    else:
        form = CanvasForm(instance=canvas)

    return render(request, 'canvas/add.html', {
        'form': form,
    })

@login_required
def delete(request, canvas_id):
    try:
        canvas = Canvas.objects.get(id=canvas_id)
        if canvas.owner != request.user:
            raise Exception('canvas is not owned by user')
    except ObjectDoesNotExist:
        return HttpResponse('{"status": "error", "code": "item does not exists"}', mimetype='application/json')
    except Exception as inst:
        return HttpResponse('{"status": "error", "code": "' + str(inst) + '"}', mimetype='application/json')
    canvas.delete()
    return HttpResponse('{"status": "success"}', mimetype='application/json')
