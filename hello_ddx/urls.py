from django.urls import path
from .views import BtDdxView

urlpatterns = [
  path('',BtDdxView.as_view(),name='index')
]