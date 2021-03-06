# Generated by Django 2.0.5 on 2019-10-10 15:33

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='房间名')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('log_record', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='日志')),
            ],
            options={
                'verbose_name': '聊天室',
                'verbose_name_plural': '聊天室',
            },
        ),
    ]
