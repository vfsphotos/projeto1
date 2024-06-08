from django.contrib import admin
from django.urls import path
from main.views import index, show, store, destroy, destroy_item, put, contato
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path("<int:id>/", show, name='show'),
    path('nova/tarefa/', store, name='store'),
    path('<int:todo_id>/novo/item/', store, name='store-item'),
    path('<int:todo_id>/excluir/tarefa/', destroy, name='destroy'),
    path('<int:todo_id>/<int:item_id>/excluir/item/', destroy_item, name='destroy-item'),
    path('item/<int:item_id>/edit/', put, name='put-item'),
    path('contato/', contato, name='contato'),
]
