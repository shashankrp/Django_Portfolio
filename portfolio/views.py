from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def say_hello(request):
    if request.method == 'GET':
        val = ""
    if request.method == 'POST':
        email = request.POST["email"]
        print(email)
        val = "Thank you for Subscribing"
    return render(request, "index.html", {'val':val})
