from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):  # нова база даних в адмінці сайту:
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  #  вторинний ключ
    title = models.CharField(max_length=200)  # рядок до 200 символів
    description = models.TextField(null=True, blank=True)  # рдок тексту
    complete = models.BooleanField(default=False)  # перемикач так/ні
    create = models.DateTimeField(auto_now_add=True)  # ставить час/дату з момету заповнення
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']