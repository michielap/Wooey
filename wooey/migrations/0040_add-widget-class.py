# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-23 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wooey", "0039_wooey_widgets"),
    ]

    operations = [
        migrations.AddField(
            model_name="wooeywidget",
            name="widget_class",
            field=models.CharField(
                blank=True,
                help_text="Widget class to use (e.g. django.forms.TextInput, defaults to Form Field on Script Parameter model if blank).",
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="scriptparameter",
            name="input_type",
            field=models.CharField(
                help_text="The python type expected by the script (e.g. boolean, integer, file).",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="wooeywidget",
            name="input_attributes",
            field=models.TextField(
                blank=True,
                help_text='Extra attributes to the input field. The extra attributes MUST be specified like key="value" (e.g. type="date").',
                null=True,
                verbose_name="Input Widget Extra Attributes",
            ),
        ),
    ]
