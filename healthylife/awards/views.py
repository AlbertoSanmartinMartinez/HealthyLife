from django.shortcuts import render


# Create your views here.
def awards(request):
    return render(request, "awards.html", {})
