"""Модуль с функциями страниц: index, about и т.д."""
from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Category

from .constant import TEXT_IN_ABOUT, TEXT_IN_HOME


def index(request) -> HttpResponse:
    """Функция главной страницы."""
    context = {
        'title': TEXT_IN_HOME['title'],
        'content': TEXT_IN_HOME['content'],
        'categories': Category.objects.all()
    }
    return render(request, 'index.html', context)


def about(request) -> HttpResponse:
    """Функция страницы 'О нас'."""
    context = {
        'title': TEXT_IN_ABOUT['title'],
        'content': TEXT_IN_ABOUT['content']
    }
    return render(request, 'about.html', context)
