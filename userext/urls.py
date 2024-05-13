from django.urls import path
from . import views
from .views import CreateUserView

urlpatterns = [
    path('', views.user_list, name='user-list'),
    path('add-user/', CreateUserView.as_view(), name='add-user'),
]
