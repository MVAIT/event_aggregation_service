from django.urls import path, include
from . import views
from .views import EventListView, EventCreateView, EventDetailView, EventUpdateView, EventDeleteView




urlpatterns = [
    path('', EventListView.as_view(), name='event_list'),
    path('about/', views.about, name='event_about'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('event/new/', EventCreateView.as_view(), name='event_new'),
    path('event/<int:pk>/edit/', EventUpdateView.as_view(), name='event_edit'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
    path('event/<int:pk>/comment/', views.add_comment_to_event, name='add_comment_to_event'),
]