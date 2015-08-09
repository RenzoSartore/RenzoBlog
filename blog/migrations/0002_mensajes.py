# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensajes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('mensaje', models.TextField(verbose_name='Mensaje')),
                ('published', models.BooleanField(default=False, verbose_name='Publicado?')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha del Mensaje')),
                ('published_in', models.ForeignKey(to='blog.Entrada')),
            ],
            options={
                'ordering': ['-fecha'],
                'verbose_name': 'Mensaje',
                'verbose_name_plural': 'Todos los mensajes',
            },
        ),
    ]
