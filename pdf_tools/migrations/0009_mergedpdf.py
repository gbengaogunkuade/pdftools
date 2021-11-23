# Generated by Django 3.2.3 on 2021-11-18 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_tools', '0008_auto_20211118_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='MergedPDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_session_id', models.TextField(blank=True, null=True)),
                ('merged_pdf_file', models.FileField(default='default.pdf', upload_to='merged_pdf/')),
            ],
            options={
                'verbose_name_plural': 'MergedPDF',
            },
        ),
    ]