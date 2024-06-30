# Generated by Django 5.0.6 on 2024-06-22 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookReader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('readers', models.ManyToManyField(to='bookstore.reader')),
            ],
        ),
    ]
