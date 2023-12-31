# Generated by Django 4.2.7 on 2023-12-02 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SMSJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipients', models.TextField()),
                ('template', models.TextField()),
                ('context', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sent_at', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(default='Pending', max_length=20)),
            ],
        ),
    ]
