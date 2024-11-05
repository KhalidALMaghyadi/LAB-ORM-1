# Generated by Django 5.0.6 on 2024-11-05 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_blog_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='kind',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='published_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
