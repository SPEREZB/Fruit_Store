# Generated by Django 3.2.8 on 2022-11-13 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fruits',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30, verbose_name='Titulo')),
                ('imagen', models.ImageField(null=True, upload_to='Images', verbose_name='Imagen')),
            ],
        ),
    ]
