# Generated by Django 4.1.7 on 2023-05-24 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_comment_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='img',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='comment_imgs'),
        ),
    ]