from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return HttpResponse('<html><title>To-Do lists</title><head>Ayu Sahnaz Ovariyanti</head><body>1206208580</body></html>')
