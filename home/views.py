from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home(request):
    peoples = [
        {'name': 'Raj', 'age':25},
        {'name': 'Raj', 'age':25},
        {'name': 'Raj', 'age':25}
    ]
    return render(request, "home/index.html", context = {'peoples': peoples}) #context is used to send data from bacjend to html template in frontend

def success_page(request):
    print("*"*10)
    return HttpResponse("<h1>Hey this is a success page</h1>")