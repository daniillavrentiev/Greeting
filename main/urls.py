from django.urls import path
from .views import GreetingView, IndexView, ConnectionView, MeetingView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('greeting/<int:id>', GreetingView.as_view(), name='greeting'),
    path('connection', ConnectionView.as_view(), name='connection'),
    path('meeting/<str:name>', MeetingView.as_view(), name='meeting')

]

