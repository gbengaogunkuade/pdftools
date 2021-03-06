# Generated by Django 3.2.3 on 2021-11-19 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_tools', '0014_alter_mergedpdf_pdf_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDFToPassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_session_id', models.TextField(blank=True, null=True)),
                ('pdf_file', models.FileField(default='default.pdf', upload_to='pdf_files_for_merging/')),
                ('pdf_password', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'PDFToPassword',
            },
        ),
        migrations.DeleteModel(
            name='PasswordedPDF',
        ),
    ]
