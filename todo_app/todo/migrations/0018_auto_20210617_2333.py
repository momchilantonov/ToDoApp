# Generated by Django 3.2.4 on 2021-06-17 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0017_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='priority',
            name='name',
            field=models.CharField(choices=[('Low', 'Low'), ('Normal', 'Normal'), ('High', 'High')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]