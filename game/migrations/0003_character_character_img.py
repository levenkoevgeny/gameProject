# Generated by Django 5.0.4 on 2024-04-17 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_character_alter_answer_options_alter_game_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='character_img',
            field=models.ImageField(blank=True, null=True, upload_to='characters', verbose_name='Аватар'),
        ),
    ]
