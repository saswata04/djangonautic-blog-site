# Generated by Django 3.1.1 on 2020-11-13 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='id',
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(primary_key=True, serialize=False),
        ),
    ]