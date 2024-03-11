from django.shortcuts import render

# Create your views here.



def index(request):
    return render(request,"website/index.html")
def about(request):
    return render(request,"website/about.html")
def contact(request):
    return render(request,"website/contact.html")
def service(request):
    return render(request,"website/service.html")
def price(request):
    return render(request,"website/price.html")

def viewpage(request):
    return render(request,"website/viewpage.html")