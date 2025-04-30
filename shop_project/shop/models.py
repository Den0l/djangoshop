from django.db import models

# Create your models here.

MAX_LENGTH = 255

class Client(models.Model):
    name = models.CharField(verbose_name = "Имя", max_length=MAX_LENGTH)
    surname = models.CharField(verbose_name = "Фамилия", max_length=MAX_LENGTH)
    photo = models.ImageField(verbose_name = "Фото", upload_to='clients/')
    email = models.EmailField(verbose_name = "Email")
    phone = models.CharField(verbose_name = "Телефон", max_length=20)

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Account(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    account_number = models.CharField(verbose_name = "Номер счета", max_length=20)
    balance = models.DecimalField(verbose_name = "Баланс", max_digits=10, decimal_places=2)

    def __str__(self):
        return self.account_number

    class Meta:
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'


class Credit(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.DecimalField(verbose_name = "Сумма кредита", max_digits=10, decimal_places=2)
    interest_rate = models.FloatField(verbose_name = "Процентная ставка")

    def __str__(self):
        return f"{self.amount} руб."

    class Meta:
        verbose_name = 'Кредит'
        verbose_name_plural = 'Кредиты'


class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(verbose_name = "Сумма", max_digits=10, decimal_places=2)
    date = models.DateTimeField(verbose_name = "Дата")

    def __str__(self):
        return f"{self.amount} руб."

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'


class LoanApplication(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(verbose_name = "Статус", max_length=20, choices=[('pending', 'Ожидает'), ('approved', 'Одобрено')])
    applied_at = models.DateTimeField(verbose_name = "Дата заявки", auto_now_add=True)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Заявка на кредит'
        verbose_name_plural = 'Заявки на кредиты'


class Branch(models.Model):
    name = models.CharField(verbose_name = "Название филиала", max_length=MAX_LENGTH)
    address = models.TextField(verbose_name = "Адрес")
    photo = models.ImageField(verbose_name = "Фото", upload_to='branches/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'


class Employee(models.Model):
    name = models.CharField(verbose_name = "Имя сотрудника", max_length=MAX_LENGTH)
    position = models.CharField(verbose_name = "Должность", max_length=MAX_LENGTH)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Card(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    card_number = models.CharField(verbose_name = "Номер карты", max_length=16)
    expiration_date = models.DateField(verbose_name = "Срок действия")

    def __str__(self):
        return self.card_number

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'