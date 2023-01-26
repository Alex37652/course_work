from . import views
from django.urls import path, include

from .views import *

app_name = 'calender'
urlpatterns = [
    # path(r'index/', views.index, name='index'),
    path(r'', views.CalendarView.as_view(), name='calendar'),
    path(r'register/', RegisterUser.as_view(), name='register'),
    path(r'login/', LoginUser.as_view(), name='login'),
    path(r'logout/', logout_user, name='logout'),
    path(r'event/new/', views.event, name='event_new'),
    path(r'event/edit/(?P<event_id>\d+)/', views.event, name='event_edit'),
]
