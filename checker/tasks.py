# -*- coding: utf-8 -*-
# @Author: SyedAli
# @Date:   2019-02-01 03:28:40
# @Last Modified by:   SyedAli
# @Last Modified time: 2019-02-01 05:52:26
import string

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import shared_task

@shared_task
def getsimilarsentences(total):
    # pass