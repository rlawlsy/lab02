from django.shortcuts import render
from .models import Lottery

def home(request):
    if request.method == "POST":
        numbers = Lottery.generate_numbers()
        Lottery.objects.create(numbers=numbers)
    recent_draws = Lottery.objects.order_by('-draw_date')[:5]
    return render(request, 'lotto/home.html', {'recent_draws': recent_draws})