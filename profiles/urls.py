from django.urls import path
from .views import ProfilesListView, ProfilesDetailView

profiles_patterns = ([
    path('', ProfilesListView.as_view(), name='profiles'),
    path('<username>/', ProfilesDetailView.as_view() , name='detail'),
], 'profiles')