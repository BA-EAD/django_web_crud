# Generated by Django 2.2.3 on 2019-07-17 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_registr_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='registr',
            name='image1',
            field=models.ImageField(blank=True, editable=False, null=True, upload_to='pic_folder'),
        ),
    ]
