
# Generated by Django 2.1 on 2018-08-26 18:08

# Generated by Django 2.1 on 2018-08-26 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=7)),
                ('date_of_birth', models.DateField(default='1990-09-09')),
                ('avatar', models.ImageField(upload_to='')),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('email_verified', models.BooleanField(default=False)),
                ('joined_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('admin', models.BooleanField(default=False)),
                ('staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
