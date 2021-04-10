from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return HttpResponse('This is About page')


def form(request):
    return render(request,'form.html',{'name':'Vladimir'})


def main(request):
    return render(request,'home.html',{'greeting':'Hello!'})

def reverse(request):
    message_text = request.GET['message']
    reverse_text = message_text[::-1]
    return render(request,'reverse.html',{'message': reverse_text})
