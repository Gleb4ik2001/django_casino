"""MODELS AUTHS"""
# import uuid
# import base64

import datetime

from django.core.validators import MinValueValidator, RegexValidator
from django.forms import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.query import QuerySet


class MyUserManager(BaseUserManager):
    """ClientManager."""

    def create_user(
        self,
        email: str,
        password: str
    ) -> 'MyUser':

        if not email:
            raise ValidationError('Email required')

        custom_user: 'MyUser' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        custom_user.set_password(password)
        custom_user.save(using=self._db)
        return custom_user

    def create_superuser(
        self,
        email: str,
        password: str
    ) -> 'MyUser':

        custom_user: 'MyUser' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        custom_user.is_superuser = True
        custom_user.is_active = True
        custom_user.is_staff = True
        custom_user.set_password(password)
        custom_user.save(using=self._db)
        return


class MyUser(AbstractBaseUser, PermissionsMixin):

    class Currencies(models.TextChoices):
        TENGE = 'KZT', 'Tenge'
        RUBLI = 'RUB', 'Rubli'
        EURO = 'EUR', 'Euro'
        DOLLAR = 'USD', 'Dollar'

    email = models.EmailField(
        verbose_name='почта/логин',
        unique=True,
        max_length=200
    )
    nickname = models.CharField(
        verbose_name='ник',
        max_length=120
    )
    currency = models.CharField(
        verbose_name='валюта',
        max_length=4,
        choices=Currencies.choices,
        default=Currencies.TENGE
    )
    
    is_staff = models.BooleanField(
        default=False
    )
    objects = MyUserManager()

    @property
    def balance(self) -> float:
        transactions: QuerySet[Transaction] = Transaction.objects.filter(user=self.pk)
        result: float = 0
        for trans in transactions:
            if trans.is_filled:
                result += trans.amout
            else:
                result -= trans.amout
        return result


    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    class Meta:
        ordering = ['-id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class ActivationCode(models.Model):
    """Код, который приходит на почту."""

    user = models.OneToOneField(
        verbose_name='пользователь',
        related_name='code',
        to=MyUser,
        on_delete=models.CASCADE
    )
    code = models.CharField(
        verbose_name='код',
        unique=True,
        max_length=200
    )
    is_active = models.BooleanField(
        verbose_name='активный?',
        default=True
    )
    datetime_created = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True,
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Код'
        verbose_name_plural = 'Коды активации'

class BankCard(models.Model):
    number = models.CharField(
        verbose_name='номер',
        max_length=16,
        validators=[
            RegexValidator(regex=r'^\d{16}$', message='Number не верный формат')
        ]
    )
    owner = models.OneToOneField(
        verbose_name='пользователь',
        related_name='card',
        to=MyUser,
        on_delete=models.CASCADE
    )
    cvv = models.CharField(
        verbose_name='номер',
        max_length=3,
        validators=[
            RegexValidator(regex=r'^\d{3}$', message='CVV не верный формат')
        ]
    )
    experation_time = models.DateField(
        verbose_name='срок действия'
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Банковская карта'
        verbose_name_plural = 'Банковская карты'


class Transaction(models.Model):
    user = models.ForeignKey(
        verbose_name='пользователь',
        related_name='transaction',
        to=MyUser,
        on_delete=models.PROTECT

    )
    amout = models.DecimalField(
        verbose_name='сумма',
        max_digits=11,
        decimal_places=2
    )
    datetime_created = models.DateTimeField(
        verbose_name='дата транзакции',
        auto_now_add=True,
    )
    is_filled = models.BooleanField(
        verbose_name='пополнение',
        default=False
    )

    class Meta:
        ordering = ('-datetime_created',)
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'