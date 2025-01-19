from django.urls import path
from .views import columns, labels, pencode_list, nencode_list, pdecode_value

urlpatterns = [
    path('columns/', columns, name='columns'),
    path('labels/', labels, name='labels'),
    path('pencode/', pencode_list, name='pencode'),
    path('nencode/', nencode_list, name='nencode'),
    path('pdecode/', pdecode_value, name='pdecode'),
]