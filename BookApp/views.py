from django.shortcuts import render,HttpResponse,redirect
from .models import BookStore,UserDetails
from django.db.models import Q
# Create your views here.
def home(request):
    data=BookStore.objects.all()
    if request.method=="POST":
        search=request.POST.get('search')
        data=BookStore.objects.filter(Q(book_name_icontains=search) | Q(author_name_icontains=search))
        return render(request,'home.html',{'value':data})
    return render(request,'home.html',{'value':data})

def buy(request,id):
    data=BookStore.objects.filter(id=id)
    return render(request,'buy.html',{'value':data})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('user_password')
        username1 = 'sneha'
        password1 = '1234'

        if username == username1 and password == password1:
            request.session['username'] = 'sneha'
            return HttpResponse('LOGIN SUCCESSFULLY')
        else:

            return HttpResponse('INVALID USER')

    return render(request,'login.html')