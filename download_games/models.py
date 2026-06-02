from django.db import models

# Create your models here.
class Games(models.Model):
    title = models.CharField(max_length=100, verbose_name="Введите название игры")
    photo = models.ImageField(verbose_name="Добавьте фото игры", upload_to='games/')
    description = models.TextField(blank=True, verbose_name="Укажите описание игры")
    url = models.URLField(verbose_name="Укажите ссылку для скачивания")
