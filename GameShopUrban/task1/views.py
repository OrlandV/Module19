from django.shortcuts import render
from django.core.paginator import Paginator
from .forms import *
from .models import *


def platform(request):
    context = {
        'title': 'Главная страница',
    }
    return render(request, 'platform.html', context)


def games(request):
    if not (per_page := request.POST.get('per_page')):
        per_page = request.GET.get('per_page')
    per_page = int(per_page) if per_page is not None and per_page.isdigit() else 3
    paginator = Paginator(Game.objects.all(), per_page)
    page_number = request.GET.get('page')
    context = {
        'title': 'Игры',
        'page_games': paginator.get_page(page_number)
    }
    return render(request, 'games.html', context)


def cart(request):
    context = {
        'title': 'Корзина',
    }
    return render(request, 'cart.html', context)


def sign_up_by_django(request):
    users = Buyer.objects.all()
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password == repeat_password and age >= 18:
                for user in users:
                    if user.name != username:
                        Buyer.objects.create(name=username, age=age)
                        info['successful'] = username
                        break
                if 'successful' not in info:
                    info['error'] = 'Пользователь уже существует.'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают.'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18.'
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {'info': info, 'form': form})
