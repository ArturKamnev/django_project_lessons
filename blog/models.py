from django.db import models

# Create your models here.
class Fighter(models.Model):
    title = models.CharField(max_length=100, verbose_name="Укажите имя бойца")
    photo = models.ImageField(upload_to='fighters/', verbose_name="Загрузите фото бойца")
    KINDOM = (
        ('Земное царство', 'Земное царство'),
        ("Внешний мир", "Внешний мир"),
        ('Преисподняя', 'Преисподняя'),
        ('Эдения', 'Эдения')
    )
    kindom = models.CharField(max_length=100, choices=KINDOM, verbose_name="Укажите царство")
    description = models.TextField(verbose_name='Укажите описание бойца', null=True)
    weapon = models.CharField(max_length=100, verbose_name="Укажите оружие бойца", default='Кунаи')
    fatality = models.URLField(verbose_name="Укажите ссылку на фаталити", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Бойца'
        verbose_name_plural = 'Бойцы МК'

    def __str__(self):
        return self.title
    
class FactsMk(models.Model):
    facts = models.CharField(max_length=100, verbose_name="Укажите факт")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.facts} - {self.created_at}'