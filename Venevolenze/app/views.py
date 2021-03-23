from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from .models import ReadBook, Category
from .forms import ReadBookForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model


@login_required(login_url='/login/')
def index(request):
    users = get_user_model().objects.all()
    books = ReadBook.objects.filter(user=request.user).order_by('-id')
    return render(request, 'app/index.html', {'books': books, 'users': users})


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            input_email = form.cleaned_data['email']
            input_password = form.cleaned_data['password1']
            new_user = authenticate(email=input_email, password=input_password)
            if new_user is not None:
                login(request, new_user)
                return redirect('app:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'app/signup.html', {'form': form})


def sample(request):
    return render(request, 'app/sample.html')


def sample_new(request):
    return render(request, 'app/sample_new.html')


@login_required(login_url='/login/')
def consideration(request, book_id):
    login_user = get_user_model().id
    book = get_object_or_404(ReadBook, pk=book_id)
    if request.user == book.user:
        context = {
            'book': book,
        }
        return render(request, 'app/consideration.html', context)
    return redirect('app:index')


@login_required(login_url='/login/')
def new_book_consider(request):
    if request.method == "POST":
        form = ReadBookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            messages.success(request, "新しく追加できました。")
        return redirect('app:index')
    else:
        form = ReadBookForm
    return render(request, 'app/new_book_consider.html', {'form': form})


@login_required(login_url='/login/')
@require_POST
def delete(request, book_id):
    book = get_object_or_404(ReadBook, id=book_id)
    book.delete()
    return redirect('app:index')


@login_required(login_url='/login/')
def edit(request, book_id):
    book = get_object_or_404(ReadBook, id=book_id)

    if request.user == book.user:
        if request.method == "POST":
            form = ReadBookForm(request.POST, instance=book)
            if form.is_valid():
                form.save()
                return redirect('app:consideration', book_id=book_id)
        else:
            form = ReadBookForm(instance=book)
        return render(request, 'app/edit.html', {'form': form, 'book': book})
    else:
        return redirect('app:index')


@login_required(login_url='/login/')
def books_category(request, category):
    category = Category.objects.get(title=category)
    books = ReadBook.objects.filter(category=category, user=request.user).order_by('-created_at')
    return render(request, 'app/index.html', {'books': books, 'category': category})
