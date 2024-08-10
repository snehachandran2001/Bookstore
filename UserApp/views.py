from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from datetime import date


def index(request):
    data = BOOKS.objects.all()
    user_id = request.session.get('userid')
    search_query = request.GET.get('search_query', '')
    sort_by = request.GET.get('sort_by', '')

    if user_id:
        user_data = USERDATA.objects.filter(id=user_id).first()
    else:
        user_data = None

    if search_query:
        data = data.filter(
            Q(bookname__icontains=search_query) |
            Q(authorname__icontains=search_query) |
            Q(categories__icontains=search_query)
        )

    if sort_by == 'oldest':
        data = data.order_by('publication_date')
    elif sort_by == 'latest':
        data = data.order_by('-publication_date')

    return render(request, 'index.html', {'data_key': data, 'search': search_query, 'user_data': user_data})


def login(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            user_email = request.POST.get('user_email')
            user_password = request.POST.get('user_password')

            user = USERDATA.objects.filter(user_email=user_email, user_password=user_password).first()

            if user:
                request.session['userid'] = user.id

                data = BOOKS.objects.all()
                user_id = request.session.get('userid')
                user_data = USERDATA.objects.filter(id=user_id).first()

                return render(request, 'index.html', {'data_key': data, 'user_data': user_data})
            else:

                return render(request, 'login.html')

        elif 'register' in request.POST:
            if request.method == 'POST':
                user_name = request.POST.get('user_name')
                user_email = request.POST.get('user_email')
                user_password = request.POST.get('user_password')

                user_obj = USERDATA()

                user_obj.user_name = user_name
                user_obj.user_email = user_email
                user_obj.user_password = user_password

                user_obj.save()

                redirect('/login')

    return render(request, 'login.html')


def logout(request):
    if 'userid' in request.session:
        del request.session['userid']
    return redirect('/')


def wishlist(request):
    return render(request, 'wishlist.html')


def categories(request):
    return render(request, 'categories.html')


def preview(request, id):
    data = BOOKS.objects.filter(id=id)

    return render(request, 'preview.html', {'data_key': data})


def cart(request, id):
    if 'userid' in request.session:
        user_id = request.session.get('userid')
        user = USERDATA.objects.get(id=user_id)

        if request.method == 'POST':
            item_id = request.POST.get('item_id')
            quantity = int(request.POST.get('quantity'))
            cart_item = CART.objects.get(user_id=user_id, id=item_id)

            cart_item.quantity = quantity
            cart_item.total_price = cart_item.book.price * quantity
            cart_item.save()

        data = CART.objects.filter(user=user_id)
        price_all = sum(item.total_price for item in data)

        return render(request, 'cart.html', {'data_key': data, 'price_all': price_all})
    else:
        return redirect('login')


def cartdis(request):
    if request.method == 'POST':
        user_id = request.session.get('userid')
        item_id = request.POST.get('item_id')
        quantity = int(request.POST.get('quantity'))

        cart_item = CART.objects.get(user_id=user_id, id=item_id)
        cart_item.quantity = quantity
        cart_item.total_price = cart_item.book.price * quantity
        cart_item.save()

        data = CART.objects.filter(user=user_id)
        price_all = sum(item.total_price for item in data)

        return render(request, 'cart.html', {'data_key': data, 'price_all': price_all})
    else:
        user_id = request.session.get('userid')
        data = CART.objects.filter(user=user_id)
        price_all = sum(item.total_price for item in data)
        return render(request, 'cart.html', {'data_key': data, 'price_all': price_all})


def remove(request, id):
    row_remove = CART.objects.get(id=id)
    row_remove.delete()

    return redirect('/cartdis')


def remove_book(request, id):
    row_remove = BOOKS.objects.get(id=id)
    row_remove.delete()

    return redirect('/manage')


def edit(request, id):
    data = BOOKS.objects.filter(id=id)
    userobj = BOOKS.objects.get(id=id)

    if request.method == "POST":
        coverimg = request.FILES.get('coverimg')
        bookname = request.POST.get('bookname')
        authorname = request.POST.get('authorname')
        category = request.POST.get('category')
        price = request.POST.get('price')

        if coverimg:
            userobj.coverimg = coverimg

        userobj.bookname = bookname
        userobj.authorname = authorname
        userobj.categories = category
        userobj.price = price

        userobj.save()
        return redirect('/manage')

    return render(request, 'edit.html', {'data_key': data})


def sell(request):
    if request.method == "POST":
        coverimg = request.FILES.get('coverimg')
        bookname = request.POST.get('bookname')
        authorname = request.POST.get('authorname')
        category = request.POST.get('category')
        price = request.POST.get('price')
        publication_date = date.today()

        userobj = BOOKS()
        userobj.coverimg = coverimg
        userobj.bookname = bookname
        userobj.authorname = authorname
        userobj.availability = 'Available'
        userobj.categories = category
        userobj.price = price
        userobj.publication_date = publication_date

        userobj.save()

        return redirect('/')
    return render(request, 'sell.html')


def category_display(request, categories):
    data = BOOKS.objects.filter(categories=categories)
    data2 = BOOKS.objects.filter(categories=categories)

    return render(request, 'category_display.html', {'data_key': data, 'data_key2': data2})


def manage(request):
    data = BOOKS.objects.all()
    return render(request, 'manage.html', {'data_key': data})


# def filter_books(request):
#     if request.method == "GET":
#         price_order = request.GET.get("price_order")
#         sort_by = request.GET.get("sort_by")
#         search_query = request.GET.get("search_query", "")
#
#         # Apply price filtering
#         if price_order == "ascending":
#             books = BOOKS.objects.filter(
#                 Q(bookname__icontains=search_query) |
#                 Q(authorname__icontains=search_query) |
#                 Q(categories__icontains=search_query)
#             ).order_by("price")
#         elif price_order == "descending":
#             books = BOOKS.objects.filter(
#                 Q(bookname__icontains=search_query) |
#                 Q(authorname__icontains=search_query) |
#                 Q(categories__icontains=search_query)
#             ).order_by("-price")
#         else:
#             books = BOOKS.objects.filter(
#                 Q(bookname__icontains=search_query) |
#                 Q(authorname__icontains=search_query) |
#                 Q(categories__icontains=search_query)
#             )
#
#         # Apply sorting based on the sort_by parameter
#         if sort_by == "oldest":
#             books = books.order_by("publication_date")
#         elif sort_by == "latest":
#             books = books.order_by("-publication_date")
#
#         return render(request, "index.html", {"data_key": books, "search": search_query, "price_order": price_order})


from django.db.models import F


def filter_books(request):
    if request.method == "GET":
        sort_by = request.GET.get("sort_by")
        price_order = request.GET.get("price_order")
        search_query = request.GET.get("search_query", "")

        books = BOOKS.objects.filter(
            Q(bookname__icontains=search_query) |
            Q(authorname__icontains=search_query) |
            Q(categories__icontains=search_query)
        )

        if sort_by == "latest":
            books = books.order_by("-publication_date")

            books = books.annotate(
                latest_price=F("price")
            ).order_by("latest_price")

        if price_order == "ascending":
            books = books.order_by("price")
        elif price_order == "descending":
            books = books.order_by("-price")

        return render(request, "index.html",
                      {"data_key": books, "search": search_query, "sort_by": sort_by, "price_order": price_order})


def show_review(request):
    return render(request, 'show_review.html')
