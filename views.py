from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from canvas.models import Canvas, Item

def user_logout(request):
    logout(request)
    return redirect('/')

@login_required
def index(request):
    canvas_list = Canvas.objects.all().order_by('name')
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
    
