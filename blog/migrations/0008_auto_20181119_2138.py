# Generated by Django 2.1.3 on 2018-11-19 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20181119_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tag',
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='blog.Tag'),
        ),
    ]