# Generated by Django 3.2.9 on 2022-06-30 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0017_problem_public_cases'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='tags',
            field=models.ManyToManyField(blank=True, to='problem.ProblemTag'),
        ),
    ]