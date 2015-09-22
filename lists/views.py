from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item, List

# Create your views here.
def home_page(request):
    #if request.method == 'POST':
    #    Item.objects.create(text=request.POST['item_text'])
    #    return redirect('/lists/the-only-list-in-the-world/')

    #items = Item.objects.all()
    countsItem = Item.objects.count()
    comment = 'yey, waktunya berlibur'

    if countsItem > 0:
    	comment = 'sibuk tapi santai'
    if countsItem >= 5:
    	comment = 'oh tidak'
    return render(request, 'home.html', {'comment': comment})

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/the-only-list-in-the-world/')