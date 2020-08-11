from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name="index"),
    path('my_index', views.my_index, name="my_index"),
    path('create/', views.create, name="create"),
    path('detail/<int:jss_id>', views.detail, name="detail"),
    path('delete/<int:jss_id>', views.delete, name="delete"),
    path('update/<int:jss_id>', views.update, name="update"),
    path('create_comment/<int:jss_id>', views.create_comment, name="create_comment"),
]


