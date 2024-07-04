"""Модуль с функциями страниц: index, about и т.д."""
from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse:
    """Функция главной страницы."""
    return render(request, 'main/index.html')


def about(request) -> HttpResponse:
    """Функция страницы 'О нас'."""
    return render(request, 'main/about.html')
