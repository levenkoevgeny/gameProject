# Generated by Django 5.0.4 on 2024-04-17 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_gameresult_game_alter_answer_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameresult',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='gameresult',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Фамилия'),
        ),
    ]
