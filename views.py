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

@login_required
def add(request):
    if request.method == 'GET':
        form = CanvasForm()
    else:
        form = CanvasForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            owner = request.user
            canvas = Canvas.objects.create(
                name = name,
                owner = owner
            )
            return redirect('/')

    return render(request, 'canvas/add.html', {
        'form': form,
    })

@login_required
def addItem(request, canvas_id, box):
    if request.method == 'GET':
        form = ItemForm()
    else:
        form = ItemForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            canvas = Canvas.objects.get(id=canvas_id)
            item = Item.objects.create(
                title = title,
                canvas = canvas,
                box = box,
                bundle = form.cleaned_data['bundle']
            )
            return redirect('/' + canvas_id)

    return render(request, 'canvas/add.html', {
        'form': form,
    })

@login_required
def editItem(request, canvas_id, item_id):
    if request.method == 'GET':
        form = ExtendedItemForm()
    else:
        form = ExtendedItemForm(request.POST)
        if form.is_valid():
            canvas = Canvas.objects.get(id=canvas_id)
            item = Item.objects.get(id=item_id).edit(
                title = form.cleaned_data['title'],
                canvas = canvas,
                box = form.cleaned_data['box'],
                bundle = form.cleaned_data['bundle']
            )
            return redirect('/' + canvas_id)

    return render(request, 'canvas/add.html', {
        'form': form,
    })

@login_required
def deleteItem(request, canvas_id, item_id):
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

@login_required
def index(request):
    canvas_list = Canvas.objects.all().filter(owner=request.user).order_by('name')
    context = {'canvas_list': canvas_list}
    return render(request, 'canvas/index.html', context)

@login_required
def canvas(request, canvas_id):
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
    
