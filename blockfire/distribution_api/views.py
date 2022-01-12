from django.http import HttpResponse
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def distribute(req):
    distribution_file = os.listdir(os.path.join(BASE_DIR, 'files'))[0]
    file_path = os.path.join(os.path.join(BASE_DIR, 'files'), distribution_file)

    file = open(file_path, "rb")

    data = file.read()

    info = [data[i:i + 1024] for i in range(0, len(data), 1024)]
    print(len(info))

    file.close()

    return HttpResponse("End")
