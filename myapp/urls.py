from django.urls import path
from .views import *

urlpatterns = [
    path('reply/',replyapplist.as_view(), name='getreply_url'),
    path('reply/<str:query>/',replyapp.as_view(), name='getreply_url2'),
]