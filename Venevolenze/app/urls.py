from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'app'
urlpatterns = [
    path('', views.index, name="index"),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('sample/', views.sample, name='sample'),
    path('sample_new', views.sample_new, name='sample_new'),
    path('book/<int:book_id>/', views.consideration, name='consideration'),  # detail
    path('book/<str:category>/', views.books_category, name='books_category'),  # category
    path('new_book_consider/', views.new_book_consider, name='new_book_consider'),  # new
    path('delete/<int:book_id>/', views.delete, name='delete'),  # delete
    path('edit/<int:book_id>/', views.edit, name='edit'),  # edit
]