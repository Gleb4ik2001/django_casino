from django.db import models
from django.db.models import Manager

import os

from auths.models import MyUser

def rename_banner_file(instance, filename):
    base_path = 'main/'
    extension = filename.split('.')[-1]
    new_filename = f'{instance.name}.{extension}'
    return os.path.join(base_path, new_filename)

# Create your models here.

class Banner(models.Model):
    """banner for Reclama"""
    name = models.CharField(
        verbose_name='баннер',
        max_length=20,
    )
    banner_file = models.ImageField(
        verbose_name='файл баннера',
        upload_to=rename_banner_file,
        default='main/unknown.jpeg')
    
    is_active = models.BooleanField(
        verbose_name='активный',
        default=False,
    )
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'баннер'
        verbose_name_plural = 'баннеры'

    def __str__(self) -> str:
        return self.name

class BetManager(Manager):
    """
    Model bet's manager
    """
    def create(self, **kwargs: dict) -> 'Bet':
        print('HELLO MetodNewCreate')
        return super().create



class Bet(models.Model):
    """
    Bet for game!
    """

    class Games(models.TextChoices):
        WHEEL = (0, 'Колесо фартуны')
        SLOT = (1, 'Игровой Автомат')

    game: str = models.CharField(
        verbose_name='игра',
        max_length=200,
        choices=Games.choices
    )
    amout: float = models.DecimalField(
        verbose_name='сумма',
        max_digits=11,
        decimal_places=2
    )
    who: MyUser = models.ForeignKey(
        verbose_name='кто поставил',
        to=MyUser,
        on_delete=models.CASCADE
    )
    coef: float = models.DecimalField(
        verbose_name='коефицент',
        max_digits=3,
        decimal_places=1
    )

    objects = BetManager()

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Ставка'
        verbose_name_plural = 'Ставки'


# X = Bet.objects.create(game=0, amout=100, who=1, coef=2) создаем объект (ставку) через нашего переназначенного манагера


def win(self) -> None:
    ...

def lose(self) -> None:
    ...

