# Generated by Django 3.2.9 on 2021-11-10 21:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-creation_date']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='commenter',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created',
            new_name='creation_date',
        ),
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.TextField(default='yada'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]