# Generated by Django 4.2.17 on 2024-12-09 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_game_user_remove_trainingsession_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingsession',
            name='activity_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='trainingsession',
            name='rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='trainingsession',
            name='session_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]