from main.models import Todo, Item
from django.shortcuts import render, redirect
from .forms import ContatoForm

def index(request):
    todos = Todo.objects.all()
    return render(request, 'main/index.html', {'todos':todos})

def show(request, id):
   todo = Todo.objects.filter(id=id).first()
   itens = todo.items.all()
   return render(request, 'main/show.html', {'name':todo.name, 'items':itens, 'todo_id':todo.id})

def store(request, todo_id=None):
    if request.method == 'POST':
        if not todo_id:
            name = request.POST.get('todo_name')
            todo = Todo.objects.create(name=name)
            return redirect('index')
        else:
            todo = Todo.objects.get(id=todo_id)
            text = request.POST.get('text')
            todo.items.create(text=text)
            return redirect('show', id=todo_id)
        
def destroy(request, todo_id):
    if request.method == 'POST':
        todo = Todo.objects.filter(id=todo_id).delete()
        return redirect('index')
    
def destroy_item(request, todo_id, item_id):
    if request.method == 'POST':
        todo = Todo.objects.get(id=todo_id)
        todo.items.filter(id=item_id).delete()
        return redirect('show', id=todo_id)
    
def put(request, item_id):
    if request.method == 'POST':
        item = Item.objects.get(id=item_id)
        item.complete = not item.complete
        item.save()
        return redirect('show', id=item.todo.id)
    
def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']
            email = form.cleaned_data['email']
            me_copiar = form.cleaned_data['mne_copiar']
            return redirect('index')
    else:
        form = ContatoForm()
        return render(request, 'main/contato.html', {'form': form})