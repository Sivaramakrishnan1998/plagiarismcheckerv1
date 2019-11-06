# -*- coding: utf-8 -*-
# @Author: SyedAli
# @Date:   2019-02-05 10:01:57
# @Last Modified by:   SyedAli
# @Last Modified time: 2019-02-05 10:05:57



from django.core.urlresolvers import reverse
import PyPDF2
from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required
from random import randint
import difflib
import datetime
from .forms import DataForm,DocumentForm
from urllib.parse import urlencode, urlparse, parse_qs
import re
from django.core.files.storage import FileSystemStorage
from lxml.html import fromstring
from requests import get
import requests
from bs4 import BeautifulSoup
import io
from os.path import splitext
import random
import re, math
from collections import Counter
from django.http import HttpResponseRedirect
from .models import Document,Data,randomid,Apidocument
from django.views import View
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import DataSerializer
from rest_framework import viewsets
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import docx
from django.http import FileResponse, Http404
import fitz
