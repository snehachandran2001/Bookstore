from . import views
from django.urls import path

urlpatterns = [

    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('cartdis/', views.cartdis, name='cartdis'),
    path('cart/<int:id>/', views.cart, name='cart'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('categories/', views.categories, name='categories'),
    path('preview/<int:id>/', views.preview, name='preview'),
    path('logout/', views.logout, name='logout'),
    path('remove/<int:id>/', views.remove),
    path('sell/', views.sell, name='sell'),
    path('category_display/<str:categories>/', views.category_display, name='category_display'),
    path('manage/', views.manage, name='manage'),
    path('remove_book/<int:id>/', views.remove_book),
    path('edit/<int:id>/', views.edit),
    path("filter-books/", views.filter_books, name="filter_books"),
    path('show_review/',views.show_review,name='show_review')


]
