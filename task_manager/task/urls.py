from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views  

urlpatterns=[
    path("",views.home,name="Home"),
    path("create_task/",views.create_post,name="Create Task"),
    path("edit_task/",views.edit_post,name="Edit Task"),
    path("see_more/",views.see_more,name="See More"),
]