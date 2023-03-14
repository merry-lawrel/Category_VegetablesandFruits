from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/', views.category, name='category'),
    path('cattable/', views.cattable, name='cattable'),
    path('getdata/', views.getdata, name='getdata'),
    path('editcat/<int:id>/', views.editcat, name='editcat'),
    path('update/<int:id>/', views.update, name='update'),
    path('deletecat/<int:id>/', views.deletecat, name='deletecat'),
    path('product/', views.product, name='product'),
    path('gdata/', views.gdata, name='gdata'),
    path('prdtable/', views.prdtable, name='prdtable'),
    path('editprd/<int:id>/', views.editprd, name='editprd'),
    path('updateprd/<int:id>/', views.updateprd, name='updateprd'),
    path('deleteprd/<int:id>/', views.deleteprd, name='deleteprd'),
    path('table/<str:catname>/', views.table, name='table'),
]