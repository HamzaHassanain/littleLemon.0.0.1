from django.forms import ModelForm

from .models import BookingItemModel

class BookingItemForm(ModelForm):
    class Meta:
        model = BookingItemModel
        fields = "__all__"