# Generated by Django 4.2.6 on 2023-11-04 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workoutHome', '0002_setvolume_exercise_alter_setvolume_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setvolume',
            name='exercise',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='workoutHome.workout'),
        ),
    ]
