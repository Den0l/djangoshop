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
    photo = models.ImageField(verbose_name = "Фото", upload_to='image/')

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
    type = models.CharField(verbose_name = "Тип карты", max_length=20,  default='Кредитная', choices=[('credit', 'Кредитная'), ('debit', 'Дебетовая'), ('kid', 'Детская'), ('gold', 'Золотая')])
    price = models.DecimalField(verbose_name = "Цена", default=0, max_digits=10, decimal_places=2)
    photo = models.ImageField(verbose_name = "Фото", default="Non", upload_to='cards/')

    def __str__(self):
        return self.card_number

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'


class Order(models.Model):
    SHOP = "SH"
    COURIER = "CR"
    PICKPOINT = "PP"
    TYPE_DELIVERY = [
        {SHOP, "Вывоз из магазина"},
        {COURIER, "Доставка  курьером"},
        {PICKPOINT, "Пункт выдачи заказов"}

    ]

    buyer_firstname = models.CharField(max_length=MAX_LENGTH, verbose_name="Фамилия покупателя")
    buyer_name = models.CharField(max_length=MAX_LENGTH, verbose_name="Имя покупателя")
    buyer_surname = models.CharField(max_length=MAX_LENGTH, blank=True, null=True, verbose_name="Отчество покупателя")
    comment = models.TextField(max_length=MAX_LENGTH, blank=True, null=True, verbose_name="Комментарий")
    delivery_address = models.CharField(max_length=MAX_LENGTH, verbose_name="Адрес доставки")
    delivery_type = models.CharField(max_length=MAX_LENGTH, choices=TYPE_DELIVERY, default=SHOP, verbose_name="Тип доставки")
    date_create = models.DateTimeField(auto_now_add=True, verbose_name = "Дата создания заказа")
    date_finish = models.DateTimeField(blank=True, null=True, verbose_name = "Дата завершения заказа")

    cards = models.ManyToManyField('Card', through='Pos_order', verbose_name='Карты')

    def __str__(self):
        return f'#{self.pk} - {self.buyer_firstname} {self.buyer_name} ({self.date_create})'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Pos_order(models.Model):
    cards = models.ForeignKey(Card, on_delete=models.CASCADE, verbose_name="Карта")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ")
    count = models.PositiveIntegerField(default=1, verbose_name="Количесвто карт")
    discount = models.PositiveIntegerField(default=0, verbose_name="Скидка  на поизицию")

    def __str__(self):
        return f'{self.order.pk} {self.cards.card_number} ({self.order.buyer_firstname} {self.order.buyer_name})'
    
    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказы'