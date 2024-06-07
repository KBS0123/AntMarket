from .models import Category, MiniCategory

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def minicategories(request):
    return {
        'minicategories': MiniCategory.objects.all()
    }
