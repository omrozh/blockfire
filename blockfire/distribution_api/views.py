from django.shortcuts import render
from django.http import HttpResponse
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def distribute(req):
    files = os.listdir(os.path.join(BASE_DIR, 'files'))

    with open(os.path.join(BASE_DIR, 'files'), "rb").read() as data:
        info = [data[i:i + 2] for i in range(0, len(data), 1024)]
