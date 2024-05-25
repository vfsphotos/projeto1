from django.http import HttpResponse
from main.models import Todo
from django.shortcuts import render

def index(request):
    todos = Todo.objects.all()
    return render(request, 'main/index.html', {'todos':todos})

def show(request, id):
   todo = Todo.objects.filter(id=id).first()
   itens = todo.items.all()
   return render(request, 'main/show.html', {'items':itens})
