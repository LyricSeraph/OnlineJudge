# Generated by Django 3.2.9 on 2022-06-17 04:13

from django.db import migrations, models
import problem.models
import utils.models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0014_problem_share_submission'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='answer',
            field=utils.models.RichTextField(null=True),
        )
    ]
