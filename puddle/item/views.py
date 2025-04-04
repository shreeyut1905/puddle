from django.shortcuts import render,get_object_or_404

# Create your views here.
from .models import Item 

def detail(request,pk):
    item = get_object_or_404(Item,pk=pk)
    related_items = Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:3]
    return render(request,'item/detail.html',{
        'item':item,
        'realated_items':related_items
    })