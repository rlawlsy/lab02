from django.db import models
import random

class Lottery(models.Model):
    draw_date = models.DateField(auto_now_add=True)
    numbers = models.CharField(max_length=100)

    @staticmethod
    def generate_numbers():
        return ', '.join(map(str, sorted(random.sample(range(1, 46), 6))))

    def __str__(self):
        return f"Draw Date: {self.draw_date} | Numbers: {self.numbers}"