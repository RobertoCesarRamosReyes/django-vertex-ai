from django.shortcuts import render

# Create your views here.
def my_view2(request):
    return render(request,'test2.html')