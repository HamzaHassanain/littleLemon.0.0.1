from django.urls import path

from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('about', views.About.as_view(), name='about'),
    path('booking', views.Booking.as_view(), name='booking'),
    path('menu', views.Menu.as_view(), name='menu'),
    path('menu_item/<id>', views.MenuItem.as_view(), name='menu_item'),
]
