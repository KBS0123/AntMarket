# kakaopay/models.py
from django.db import models
from django.contrib.auth.models import User

class KakaoPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tid = models.CharField(max_length=100, unique=True)  # Transaction ID
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    item_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user} - {self.amount} - {self.status} - {self.tid}'