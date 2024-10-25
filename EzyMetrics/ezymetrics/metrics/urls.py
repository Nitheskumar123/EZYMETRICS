from django.urls import path
from . import views

urlpatterns = [
    path('leads/', views.leadlistcreate.as_view(), name='lead_list_create'),  
    path('leads/<int:pk>/', views.leadretrieveupdatedestroy.as_view(), name='lead_retrieve_update_destroy'),  
    path('campaigns/', views.campaignlistcreate.as_view(), name='campaign_list_create'), 
    path('campaigns/<int:pk>/', views.campaignretrieveupdatedestroy.as_view(), name='campaign_retrieve_update_destroy'), 
    path('generate-report/', views.generate_report, name='generate_report'),
    path('generate-csv/', views.generate_csv, name='generate_csv'), 
    path('some_view/', views.some_view, name='send_email'), 
]