
from django.shortcuts import render, HttpResponse , redirect

def index(request):
    context = {
        "Name": "Noelle",
        "Favorite_color": "Green",
        "pets": ["Bruce", "Jack", "Georgie", "Clownfat", "Backfeet"]
    }
    return render(request, "index.html", context)
def hello_name(request, name):
    context = {
        "htmlname": name,
        
    }
    return render(request, "helloname.html", context)

def new(request):
    return HttpResponse("placeholder to display the new form to create a new blog")


def create(request):
    # return redirect('/')    <---------add file path to redirect to 

def show(request, number):
    return HttpResponse(f"Placeholder to display blog number {number}.")

def edit(request, number):
    return HttpResponse(f"Placeholder to edit blog {number}.")

def destroy(request, number):
    return redirect('/')