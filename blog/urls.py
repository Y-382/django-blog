from django.urls import path
from .views import Homeview, PostDetailView

urlpatterns = [
    path('', Homeview.as_view(), name='home'),
    path('<slug:slug>', PostDetailView.as_view(), name='post-detail')
]
