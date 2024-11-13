from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def blog(request):
    return render(request,'blog.html')
def booking(request):
    return render(request,'booking.html')
def price(request):
    return render(request,'price.html')
def services(request):
    return render(request,'service.html')
def single(request):
    return render(request,'single.html')