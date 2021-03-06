# Generated by Django 3.2.3 on 2021-11-18 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MergedPDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_session_id', models.TextField(blank=True, null=True)),
                ('file', models.FileField(default='default.pdf', upload_to='merged_pdf/')),
            ],
            options={
                'verbose_name_plural': 'MergedPDF',
            },
        ),
        migrations.CreateModel(
            name='PasswordedPDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_session_id', models.TextField(blank=True, null=True)),
                ('file', models.FileField(default='default.pdf', upload_to='passworded_pdf/')),
            ],
            options={
                'verbose_name_plural': 'PasswordedPDF',
            },
        ),
    ]
