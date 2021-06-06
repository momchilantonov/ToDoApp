# Generated by Django 3.2.4 on 2021-06-06 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20210606_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=['home', 'work', 'school', 'shopping', 'training'], max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='todo',
            name='category',
            field=models.ManyToManyField(to='todo.Category'),
        ),
    ]