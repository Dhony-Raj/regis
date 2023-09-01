from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'admin/cat.html')
def insert(request):
    cat_name = request.POST.get('cat_name')
    return HttpResponse(cat_name)
