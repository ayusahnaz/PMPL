from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item, List

# Create your views here.
def home_page(request):
    #if request.method == 'POST':
    #    Item.objects.create(text=request.POST['item_text'])
    #    return redirect('/lists/the-only-list-in-the-world/')

    #items = Item.objects.all()
    #countsItem = Item.objects.count()
    #comment = 'yey, waktunya berlibur'

    #return render(request, 'index.html')
    countsItem = Item.objects.count()
    comment = 'yey, waktunya berlibur'

    return render(request, 'home.html', {'comment': comment})

def todo_list(request):
    #if request.method == 'POST':
    #    Item.objects.create(text=request.POST['item_text'])
    #    return redirect('/lists/the-only-list-in-the-world/')

    #items = Item.objects.all()
    #countsItem = Item.objects.count()
    #comment = 'yey, waktunya berlibur'

    #return render(request, 'index.html')
    countsItem = Item.objects.count()
    comment = 'yey, waktunya berlibur'

    return render(request, 'home.html', {'comment': comment})

def blog(request):
    # countsItem = Item.objects.count()
    # comment = 'yey, waktunya berlibur'

    # return render(request, 'home.html', {'comment': comment})
    return render(request, 'index.html')

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = None

    comment = ''
    countList = Item.objects.filter(list_id=list_.id).count()
    if countList == 0:
        comment = 'yey, waktunya berlibur'
    elif (countList > 0) and (countList < 5):
        comment = 'sibuk tapi santai'
    else:
        comment = 'oh tidak'

    if request.method == 'POST':
        try:
            item = Item(text=request.POST['item_text'], list=list_)
            item.full_clean()
            item.save()
            return redirect(list_)
        except ValidationError:
            error = "You can't have an empty list item"
    return render(request, 'list.html', {'list': list_, 'error': error, 'comment': comment})

def new_list(request):
    list_ = List.objects.create()
    item = Item(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})
    return redirect(list_)
