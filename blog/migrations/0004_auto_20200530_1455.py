# Generated by Django 3.0.6 on 2020-05-30 11:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200530_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='description',
        ),
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
