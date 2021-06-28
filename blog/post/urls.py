from .views import HomeView, EntryView, CreateEntryView 
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name= 'home'),
    path('entry/<int:pk>/', EntryView.as_view(), name= 'entry_detail'),
    path('create/', CreateEntryView.as_view(success_url='/'), name= 'create'),
]
