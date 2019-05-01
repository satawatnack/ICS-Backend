from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     fname = models.CharField(max_length=255, null=True, blank=True)
#     lname = models.CharField(max_length=255, null=True, blank=True)
#     email = models.CharField(max_length=255)
#     TYPES = (
#         ('user', 'user'),
#         ('admin', 'admin'),
#         ('staff', 'staff')
#     )
#     user_type = models.CharField(max_length=5, choices=TYPES, default='user')
#     password = models.CharField(max_length=255)
#     dob = models.DateField()

class Report(models.Model):
    report_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField(null=True, blank=True)
    TYPE = (
        ('canteen', 'canteen'),
        ('restaurant', 'restaurant'),
        ('other', 'other')
    )
    report_type = models.CharField(max_length=10, choices=TYPE, default='canteen')
    detail = models.TextField()


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    create_datetime = models.DateTimeField()
    receive_datetime = models.DateTimeField()
    comment = models.TextField()
    total_price = models.FloatField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Restaurant(models.Model):
    res_id = models.AutoField(primary_key=True)
    res_name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    TYPE = (
        ('close', 'close'),
        ('open', 'open')
    )
    status = models.CharField(max_length=5, choices=TYPE, default='open')
    image_path = models.CharField(max_length=255)
    rating = models.IntegerField()
    open_time = models.CharField(max_length=255)
    close_time = models.CharField(max_length=255)
    Sunday = models.BooleanField(default=False, null=True, blank=True)
    Monday = models.BooleanField(default=False, null=True, blank=True)
    Tuesday = models.BooleanField(default=False, null=True, blank=True)
    Wednesday = models.BooleanField(default=False, null=True, blank=True)
    Thursday = models.BooleanField(default=False, null=True, blank=True)
    Friday = models.BooleanField(default=False, null=True, blank=True)
    Saturday = models.BooleanField(default=False, null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=False)

class Staff(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    res_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class User_restaurant(models.Model):
    class Meta:
        unique_together = (('user_id', 'res_id'),)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    res_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateTimeField()

class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    res_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    prepare_time = models.CharField(max_length=255, null=True, blank=True)
    image_path = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    TYPE = (
        ('not_sell', 'not_sell'),
        ('sell', 'sell')
    )
    status = models.CharField(max_length=8, choices=TYPE, default='sell')
    rating = models.IntegerField(null=True, blank=True)


class Extra(models.Model):
    class Meta:
        unique_together = (('extra_id', 'menu_id'),)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    extra_id = models.AutoField(primary_key=True)
    extra_description = models.TextField()
    extra_price = models.FloatField()

class User_menu(models.Model):
    class Meta:
        unique_together = (('user_id', 'menu_id'),)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    date = models.DateTimeField()

class Order_menu(models.Model):
    class Meta:
        unique_together = (('order_id', 'menu_id'),)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, primary_key=True)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    TYPE = (
        ('preparing', 'preparing'),
        ('finished', 'finished')
    )
    status = models.CharField(max_length=9, choices=TYPE, default='preparing')

