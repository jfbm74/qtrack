from django.urls import path
from . import views
from .views import list_branches, AddBranchView, list_services, add_servicearea,list_modules, add_module

urlpatterns = [
    path('', views.company_list, name='company-list'),
    path('add-company/', views.add_company, name='add-company'),
    path('delete-company/<int:company_id>/', views.delete_company, name='delete-company'),
    path('update-company/<int:company_id>/', views.update_company, name='update-company'), 
    path('branches/', list_branches, name='list-branches'),
    path('add-branch/', AddBranchView.as_view(), name='add-branch'),
    path('services/', list_services, name='list-services'),
    path('add-service/', add_servicearea, name='add-service-area'),
    path('modules/', list_modules, name='list-modules'),
    path('add-module/', add_module, name='add-module'),
]
