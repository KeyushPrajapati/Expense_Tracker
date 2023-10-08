
from django.urls import path
from .views import dashbord, edit, delete,index
app_name = "myapp"
urlpatterns = [
    path('',index, name="index"),
    path('edit/<int:id>', edit, name="edit"),
    path('delete/<int:id>', delete, name="delete"),
    path('dashbord/',dashbord.as_view(),name='dashbord')
]
