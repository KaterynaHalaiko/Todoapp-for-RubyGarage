# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='task_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u0413\u0440\u0443\u043f\u0430', to='students.Group', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task_group',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='project.Task', verbose_name='\u0421\u0442\u0430\u0440\u043e\u0441\u0442\u0430'),
            preserve_default=True,
        ),
    ]
