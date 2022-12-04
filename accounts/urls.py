from django.urls import path
from .views import SignUP

urlpatterns = [
    path('signup/', SignUP.as_view(), name='signup')
]