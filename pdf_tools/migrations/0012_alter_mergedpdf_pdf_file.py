# Generated by Django 3.2.3 on 2021-11-18 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_tools', '0011_alter_mergedpdf_pdf_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mergedpdf',
            name='pdf_file',
            field=models.FilePathField(path='media/merged_pdf/'),
        ),
    ]
