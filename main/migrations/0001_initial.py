# Generated by Django 3.0.14 on 2022-05-12 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('author_name', models.CharField(max_length=20)),
                ('pdf', models.FileField(upload_to='book/pdf')),
            ],
        ),
    ]
