# Generated by Django 3.2.3 on 2021-11-18 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_tools', '0006_auto_20211118_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='mergedpdf',
            name='pdf_file6',
            field=models.FileField(blank=True, default='default.pdf', null=True, upload_to='pdf_files_for_merging/'),
        ),
    ]