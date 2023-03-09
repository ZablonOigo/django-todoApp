from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('update/<int:pk>/',views.updatetask,name='update'),
    path('delete/<int:pk>/',views.deletetask,name='delete'),

]