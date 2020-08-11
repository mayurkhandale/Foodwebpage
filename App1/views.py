from django.shortcuts import render
from django.contrib import messages
# Create your views here.
def display(request):
    return render(request,"index.html")
def show(request):
     if request.method=="POST":
          t1=int(request._post["price"])
          t2=int(request._post["price"])
          t3 = int(request._post["price"])
          total=t1+t2+t3
          return render(request,"bill.html",{"t1":total})

     else:
         message="please select atleast one item"
         return render(request,"index.html",{"ms":message})
