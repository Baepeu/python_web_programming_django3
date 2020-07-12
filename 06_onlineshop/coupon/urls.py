from django.urls import path

from .views import add_coupon
app_name = 'coupon'

urlpatterns = [
    path('add/', add_coupon, name='add'),
]