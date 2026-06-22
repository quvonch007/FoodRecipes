from django.shortcuts import render, redirect
from products.models import Recipe, Category

from products.services.decorators import login_decorator






# @login_decorator - login decorator uni shunchaki kigizilsa bo'ldi login qilish majburiy bo'lib qoladi


def home_view(request):
    categories = Category.objects.all()
    latest_recipes = Recipe.objects.select_related('subcategory__category').order_by('-id')[:8]

    ctx = {
        'categories': categories,
        'latest_recipes': latest_recipes,
    }

    return render(request, 'home.html', ctx)