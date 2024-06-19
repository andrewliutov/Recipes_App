from django.shortcuts import render


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # рецепты добавляются сюда
}


def calculate_recipe_view(request, dish):
    servings = int(request.GET.get('servings', 1))
    recipe = {}
    recipe_from_data = DATA.get(dish)
    for key, value in recipe_from_data.items():
        recipe[key] = float(value) * servings
    context = {'recipe': recipe}
    return render(request, 'calculator/index.html', context)
