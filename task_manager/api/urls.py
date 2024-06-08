from django.urls import path 
from . import views

urlpatterns=[
    path('',views.getData),
    path('add/',views.addItem),
    path('delete/',views.deleteItem), 
    path("edit/",views.editItem)
]