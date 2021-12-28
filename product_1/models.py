from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name




class Tag(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name




class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name




class Order(models.Model):
    STATUS = (
        ('Обрaбатывается', 'Обрaбатывается' ),
        ('Выехал', 'Выехал'),
        ('Доставлен', 'Доставлен')
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,
                                related_name='customer_in_order')

    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='product_in_order')

    date_created = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=STATUS, default='Обрабатывается')


    def __str__(self):
        return self.product.name
        






