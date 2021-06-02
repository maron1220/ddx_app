from django.conf.urls import url
from .views import BtDdxView

urlpatterns = [
  url(r'',BtDdxView.as_view(),name='index')
]