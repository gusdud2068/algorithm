from django.shortcuts import redirect, render
from django.views.decorators.http import require_safe,require_POST,require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm

# Create your views here.

@require_safe
def index(request):
    todos= Todo.objects.all()
    context = {
        'todos' : todos,
    }
    return render(request, 'todos/index.html',context)

@require_http_methods(["GET","POST"])
def create(request):
    if not request.user.is_authenticated:
        return redirect("account:login")
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            return redirect('todos:index')
    
    else:
        form = TodoForm()
    context = {
        'form' : form,
    }
    return render(request, 'todos/create.html',context)
            
            
