from django.shortcuts import render
from django.http import HttpResponse
import os


def fileUpload(req):
    if req.method == "POST":
        file = req.FILES["file"]
        print(file)

        with open(os.path.join("files", str(file)), "wb") as file_writer:
            for chunk in file.chunks():
                file_writer.write(chunk)

        return HttpResponse("Success")

    return render(req, "upload_file.html")
