from django.shortcuts import render

# Create your views here.
def CDN_Bootstrap(request):
    return render(request,'CDN_Bootstrap.html')

def card_bootstrap(request):
    return render(request,'card_bootstrap')

