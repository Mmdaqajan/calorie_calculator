from django.shortcuts import render

# Create your views here.


def calculate_calorie(request):
    context = {}

    if request.method == "POST":
        return context

    return render(request, 'calorie_calculator/calorie_calculator_page.html', context)
