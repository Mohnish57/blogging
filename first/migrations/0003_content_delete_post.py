# Generated by Django 4.1 on 2022-10-29 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]