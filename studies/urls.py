#urls.py studies
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_study, name='add_study'),
    path('edit/<int:study_id>/', views.edit_study, name='edit_study'),
    path('delete/<int:study_id>/', views.delete_study, name='delete_study'),
    path('', views.view_all_studies, name='view_all_studies'),
    path('selected_view/<int:study_id>/', views.selected_view, name='selected_view'),

]
