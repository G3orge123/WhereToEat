from django.urls import path
from . import views

urlpatterns = [
    path('get-data/', views.get_data, name='get_data'),
    path('post-data/', views.post_data, name='post_data'),
]

