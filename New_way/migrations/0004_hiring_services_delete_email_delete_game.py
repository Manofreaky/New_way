# Generated by Django 4.1.6 on 2023-05-03 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('New_way', '0003_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='hiring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=1000)),
                ('contactno', models.CharField(max_length=10)),
                ('mail', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=1000)),
                ('jobrole', models.CharField(max_length=1000)),
                ('experience', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_required_on', models.CharField(max_length=100)),
                ('service_required_at', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=100)),
                ('information', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='email',
        ),
        migrations.DeleteModel(
            name='game',
        ),
    ]
