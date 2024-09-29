# Generated by Django 5.1.1 on 2024-09-29 22:46

import django.db.models.deletion
import markdownx.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('prep', models.CharField(max_length=255)),
                ('cook', models.CharField(max_length=255)),
                ('servings', models.IntegerField(blank=True, default=1, null=True)),
                ('image', models.ImageField(upload_to='media/')),
                ('ingredients', markdownx.models.MarkdownxField()),
                ('directions', markdownx.models.MarkdownxField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
