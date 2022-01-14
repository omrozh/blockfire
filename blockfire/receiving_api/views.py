from django.shortcuts import render
from django.http import HttpResponse
import os
from string import ascii_letters
from .models import File, FileRef
from random import choice


def generateID(length=16):
    gen_str = ""
    for i in range(length):
        gen_str += choice(ascii_letters)
    return gen_str


def fileUpload(req):
    if req.method == "POST":
        file = req.FILES["file"]
        f_id = generateID()
        secured_filename = f_id + str(file)

        with open(os.path.join("files", secured_filename), "wb") as file_writer:
            for chunk in file.chunks():
                file_writer.write(chunk)

        new_file = File(id_name=secured_filename)

        return HttpResponse("Success")

    return render(req, "upload_file.html")
