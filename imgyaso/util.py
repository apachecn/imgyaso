import subprocess as subp
import tempfile
import uuid
import os
from os import path
from PIL import Image
from io import BytesIO

def conv2png(img):
    if img[:4] == b'\x89PNG':
        return img
    img = Image.open(BytesIO(img))
    bio = BytesIO()
    img.save(bio, 'png')
    return bio.getvalue()
