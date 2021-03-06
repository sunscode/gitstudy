# Generated by Django 3.0.6 on 2020-08-09 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_remove_article_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='delete_status',
        ),
        migrations.AddField(
            model_name='article',
            name='publish_status',
            field=models.BooleanField(choices=[(False, '未发布'), (True, '发布')], default=False, verbose_name='发布状态'),
        ),
    ]
