from django.urls import path
from .views import myName, myLast

urlpatterns = [
    path('', myName.as_view(), name='name'),
    path('last/', myLast.as_view(), name='last')
    
]