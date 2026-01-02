from django.shortcuts import render

def home_view(request):
    return render(request, 'home/home.html', {'message': 'Hello, World! Welcome to my Django home page.'})