# -*- coding: utf-8 -*-
# @Author: SyedAli
# @Date:   2019-02-01 03:25:33
# @Last Modified by:   SyedAli
# @Last Modified time: 2019-02-01 03:27:30
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'plagiarismchecker.settings')

app = Celery('plagiarismchecker')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()