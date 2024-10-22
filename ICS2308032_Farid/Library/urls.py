from django.urls import path
from . import views

urlpatterns=[
    path("newmentor/",views.newmentor,name="newmentor"),
    path("course",views.course,name="course"),
    path("update_course/<str:code>",views.update_course,name="update_course"),
    path("update_course/save_update_course/<str:code>",views.save_update_course,name ="save_update_course"),
    path("delete_course/<str:code>", views.delete_course, name='delete_course'),
    path("search_course/", views.search_course, name='search_course'),
    path("search_course/<str:code>", views.update_course, name='search_course'),
]