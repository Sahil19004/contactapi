from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
path('admin/', admin.site.urls),
path('api/contact/create/', views.create_contact, name='create_contact'),
]