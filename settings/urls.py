from django.contrib import admin
from django.urls import path
from main.views import index, show
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path("<int:id>/", show, name='show'),
]
