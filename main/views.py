from curses.ascii import HT
import html
from multiprocessing import context
from django.http import HttpResponse
from main.models import Todo

def index(request):
    todos = Todo.objects.all().first()
    context = f"""
        <h1>Todo's</h1>
        <ul>
           <li>
                {todos}
           </li>
        </ul>
        """
    return HttpResponse(context)
def show(request, id):
    todos = Todo.objects.filter(id=id)
    items = []
    if todos:
        for todo in todos:
            for item in todo.items.all():
                items.append(item)
    return HttpResponse(f"""
    <ul>
        <li>
            {items[0].text}
        </li>
    </ul>"""
    )
    