# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_mensajes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajes',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Publicado?'),
        ),
    ]
