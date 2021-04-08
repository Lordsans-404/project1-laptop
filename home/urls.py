from django.urls import path,include
from.views import *

app_name = 'homey'
urlpatterns = [
    path('',HomeView.as_view(template_name='home/indexhome.html',paginate_by=4),name='index'),
    path('product/',HomeView.as_view(template_name='home/producthome.html'),name='product'),
    path('product/<slug:slug>',ProductHome.as_view(),name='detail'),
    path('cart/',HomeView.as_view(template_name='home/cart.html'),name="cart"),
    path('checkout/',ShippingView,name='checkout'),
    # path('user/login',FormSignUp.as_view(),name='login'),
    # path('user/signup',FormSignUp.as_view(),name='signup'),
    # path('checkout/<int:pk>',FormShipping.as_view(),name='checkout'),
    path('update-item/',updateItem, name='update-item'),
]
