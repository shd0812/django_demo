# Generated by Django 2.1 on 2020-08-22 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('publisher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appone.Publisher')),
            ],
        ),
    ]
