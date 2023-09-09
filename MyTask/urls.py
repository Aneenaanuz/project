"""
URL configuration for MyTask project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.IndexView.as_view(),name='index'),
    path('todo/add/',views.TodoCreateView.as_view(),name='todo_create'),
    path('todo/list/',views.TodoListView.as_view(),name="todo_list"),
    path('todo/<int:pk>/',views.TodoDetailView.as_view(),name='todo_detail'),
    path('todo/<int:pk>/',views.TodoDeleteView.as_view(),name='todo_delete'),
    path('todo/<int:pk>/update/',views.TodoEditView.as_view(),name='todo_update'),
      

    path('weather/',views.WeatherIndexView.as_view(),name='weather'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
