# Generated by Django 4.0.2 on 2022-02-15 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MenuIntem',
            new_name='MenuItem',
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('items', models.ManyToManyField(blank=True, related_name='order', to='customer.MenuItem')),
            ],
        ),
    ]
