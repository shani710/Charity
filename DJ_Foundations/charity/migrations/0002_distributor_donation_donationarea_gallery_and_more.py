# Generated by Django 4.2.5 on 2024-01-20 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('charity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=15, null=True)),
                ('address', models.CharField(max_length=300, null=True)),
                ('userpic', models.FileField(null=True, upload_to='')),
                ('idpic', models.FileField(null=True, upload_to='')),
                ('aboutme', models.CharField(max_length=300, null=True)),
                ('status', models.CharField(max_length=20, null=True)),
                ('regdate', models.DateTimeField(auto_now_add=True)),
                ('adminremarks', models.CharField(max_length=200, null=True)),
                ('updationdate', models.DateField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donationname', models.CharField(max_length=100, null=True)),
                ('donationpic', models.FileField(null=True, upload_to='')),
                ('collectionlocation', models.CharField(max_length=300, null=True)),
                ('description', models.CharField(max_length=300, null=True)),
                ('status', models.CharField(max_length=50, null=True)),
                ('donationdate', models.DateField(auto_now_add=True)),
                ('adminremarks', models.CharField(max_length=200, null=True)),
                ('distributorremarks', models.CharField(max_length=200, null=True)),
                ('updationdate', models.DateField(null=True)),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charity.distributor')),
            ],
        ),
        migrations.CreateModel(
            name='DonationArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100, null=True)),
                ('discription', models.CharField(max_length=300, null=True)),
                ('creationdate', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivarynpic', models.FileField(null=True, upload_to='')),
                ('creationdate', models.DateField(auto_now_add=True)),
                ('donotion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charity.donation')),
            ],
        ),
        migrations.AddField(
            model_name='donation',
            name='donationarea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charity.donationarea'),
        ),
        migrations.AddField(
            model_name='donation',
            name='donor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charity.donor'),
        ),
    ]
