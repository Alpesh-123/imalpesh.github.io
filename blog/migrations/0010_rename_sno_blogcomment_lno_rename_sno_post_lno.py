# Generated by Django 4.2.2 on 2023-07-14 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_blogcomment_sno_alter_post_sno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcomment',
            old_name='sno',
            new_name='lno',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='sno',
            new_name='lno',
        ),
    ]
