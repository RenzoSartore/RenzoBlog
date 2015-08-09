# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150807_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('celu', models.CharField(max_length=100, verbose_name='Telefono')),
                ('mail', models.CharField(max_length=100, verbose_name='Mail')),
                ('mensaje', models.TextField(verbose_name='Mensaje')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha del Post')),
            ],
        ),
    ]
