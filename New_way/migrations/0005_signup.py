# Generated by Django 4.1.6 on 2023-05-03 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('New_way', '0004_hiring_services_delete_email_delete_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
