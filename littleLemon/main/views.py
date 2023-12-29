import random
from django.shortcuts import render
from django.views import View
from .forms import BookingItemForm

from . import models

class Index(View):
    def get(self, request):
        # get all menu items
        menu_items = models.MenuItemModel.objects.all()
        menu_items = menu_items[:3]
        context = {
            'menu_items':menu_items
            , 'title':'Home'
        }
        return render(request, 'index.html' , context)


class About(View):
    def get(self, request):
        context = {
            'title':'About'
        }
        return render(request, 'about.html' , context)
    
class Booking(View):
    def get(self, request):
        context = {
            'form':BookingItemForm(),
            'title':'Booking'
        }
        return render(request, 'booking.html' , context)
    def post(self, request):
        form = BookingItemForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'title':'Thanks',
                'name':form.cleaned_data['name'],
            }
            return render(request, 'thanks.html' , context)
        else:
            context = {
                'form':form,
                'title':'Booking'
            }
            return render(request, 'booking.html' , context)
class Menu(View):
    def get(self, request):
        menu_items = models.MenuItemModel.objects.all().order_by('price')
        context = {
            'menu_items':menu_items
            , 'title':'Menu'
        }
        return render(request, 'menu.html' , context)
    
class MenuItem(View):
    def get(self, request , id):

        menu_item = models.MenuItemModel.objects.get(id=id)
        if not menu_item:
            return render(request, '404.html' , {})
        
        context = {
            'menu_item':menu_item,
            'title':'Menu Item'
        }
        return render(request, 'menu_item.html' , context)
    



def handler404(request, exception):
    return render(request, '404.html', status=404)
def handler500(request):
    return render(request, '500.html', status=500)


