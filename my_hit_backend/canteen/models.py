from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create your models here.
class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_meals = models.PositiveIntegerField(default=0)
    total_cost = models.PositiveIntegerField(default=0)
    paid = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.student_number

    class Meta:
        ordering = ["-timestamp", ]

    # @property
    # def cost_of_all_meals(self):
    #     total_cost = self.number_of_meals * 20
    #     return total_cost
