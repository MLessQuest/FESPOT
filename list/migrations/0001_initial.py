# Generated by Django 2.1.2 on 2018-11-02 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctitle', models.CharField(max_length=200)),
                ('cplace', models.CharField(max_length=100)),
                ('cdesc', models.TextField(null=True)),
                ('cdatestart', models.DateField(null=True)),
                ('cdateend', models.DateField(null=True)),
                ('clocate', models.CharField(max_length=300)),
                ('cimage', models.ImageField(default='Images/None/No-images.jpg', upload_to='Images/')),
            ],
        ),
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ftitle', models.CharField(max_length=200)),
                ('fhelder', models.CharField(max_length=100)),
                ('fparticipate', models.CharField(max_length=100)),
                ('fgenre', models.CharField(max_length=50)),
                ('fdatestart', models.DateField(null=True)),
                ('fdateend', models.DateField(null=True)),
                ('faward', models.CharField(max_length=20)),
                ('faward1', models.CharField(max_length=20)),
                ('fhomepage', models.TextField()),
                ('fdesc', models.TextField(null=True)),
                ('fimage', models.ImageField(default='Images/None/No-images.jpg', upload_to='Images/')),
                ('fauthor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
