# Generated by Django 4.0.2 on 2022-05-06 08:28

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0014_remove_blogmodel_slug_blogmodel_title_tag_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
