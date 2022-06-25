from django.db import models

# Create your models here.
class Category2(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория")
    description = models.CharField(max_length=255)
    img = models.ImageField("Изображение", upload_to='upload/categories')


    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(verbose_name="Название товара", max_length=255)
    price = models.IntegerField(verbose_name="Цена", default=0)
    description = models.CharField(verbose_name="Описание", max_length=255, default='', blank=True, null=True)
    image = models.ImageField(verbose_name="Изображение", upload_to='upload/products')
    category = models.ForeignKey(Category2, verbose_name="Категория", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class OrderData(models.Model):
    name = models.CharField('ФИО', max_length=255)
    number = models.CharField('Номер Телефона', max_length=255)
    email = models.EmailField('Email')
    address = models.CharField('Адрес', max_length=255)
    message = models.TextField('Сообщение')

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.CharField('Товар', max_length=255)
    price = models.IntegerField('Цена')
    count = models.IntegerField('Количество')
    total_sum = models.IntegerField('Общая сумма')
    customer = models.ForeignKey(OrderData, on_delete=models.CASCADE, verbose_name='Получатель')
    sent_at = models.DateTimeField('Время отправки', auto_now_add=True)


class Contact(models.Model):
    name = models.CharField('name', max_length=255)
    email = models.EmailField('Email почта', max_length=255)
    message = models.TextField('Сообщение')
    sent_at = models.DateTimeField(auto_now_add=True)


class Contact2(models.Model):
    email = models.EmailField('Email почта', max_length=255)
    sent_at = models.DateTimeField(auto_now_add=True)