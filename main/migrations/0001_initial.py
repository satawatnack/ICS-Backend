# Generated by Django 2.1.7 on 2019-05-01 02:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('extra_id', models.AutoField(primary_key=True, serialize=False)),
                ('extra_description', models.TextField()),
                ('extra_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_id', models.AutoField(primary_key=True, serialize=False)),
                ('menu_name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('prepare_time', models.CharField(blank=True, max_length=255, null=True)),
                ('image_path', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('not_sell', 'not_sell'), ('sell', 'sell')], default='sell', max_length=8)),
                ('rating', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('create_datetime', models.DateTimeField()),
                ('receive_datetime', models.DateTimeField()),
                ('comment', models.TextField()),
                ('total_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('report_id', models.AutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('report_type', models.CharField(choices=[('canteen', 'canteen'), ('restaurant', 'restaurant'), ('other', 'other')], default='canteen', max_length=10)),
                ('detail', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('res_id', models.AutoField(primary_key=True, serialize=False)),
                ('res_name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('close', 'close'), ('open', 'open')], default='open', max_length=5)),
                ('image_path', models.CharField(max_length=255)),
                ('rating', models.IntegerField()),
                ('open_time', models.CharField(max_length=255)),
                ('close_time', models.CharField(max_length=255)),
                ('Sunday', models.BooleanField(blank=True, default=False, null=True)),
                ('Monday', models.BooleanField(blank=True, default=False, null=True)),
                ('Tuesday', models.BooleanField(blank=True, default=False, null=True)),
                ('Wednesday', models.BooleanField(blank=True, default=False, null=True)),
                ('Thursday', models.BooleanField(blank=True, default=False, null=True)),
                ('Friday', models.BooleanField(blank=True, default=False, null=True)),
                ('Saturday', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('res_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='User_menu',
            fields=[
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('date', models.DateTimeField()),
                ('menu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='User_restaurant',
            fields=[
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('date', models.DateTimeField()),
                ('res_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Order_menu',
            fields=[
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.Order')),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(choices=[('preparing', 'preparing'), ('finished', 'finished')], default='preparing', max_length=9)),
            ],
        ),
        migrations.AddField(
            model_name='restaurant',
            name='user_id',
            field=models.ForeignKey(on_delete=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='report',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='menu',
            name='res_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Restaurant'),
        ),
        migrations.AddField(
            model_name='extra',
            name='menu_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Menu'),
        ),
        migrations.AlterUniqueTogether(
            name='user_restaurant',
            unique_together={('user_id', 'res_id')},
        ),
        migrations.AlterUniqueTogether(
            name='user_menu',
            unique_together={('user_id', 'menu_id')},
        ),
        migrations.AddField(
            model_name='order_menu',
            name='menu_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Menu'),
        ),
        migrations.AlterUniqueTogether(
            name='extra',
            unique_together={('extra_id', 'menu_id')},
        ),
        migrations.AlterUniqueTogether(
            name='order_menu',
            unique_together={('order_id', 'menu_id')},
        ),
    ]
