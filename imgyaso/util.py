import subprocess as subp
import tempfile
import uuid
import os
from os import path
from PIL import Image
from io import BytesIO

headers = {
    'png': b'\x89PNG',
    # 'svg': b'<?xml',
    'jpg': b'\xff\xd8\xff',
    'gif': b'GIF',
    'tif': b'II\x2a\x00',
    'bmp': b'BM',
    'webp': b'RIFF',
}

def is_img_data(img):
    for _, hdr in headers.items():
        l = len(hdr)
        if img[:l] == hdr:
            return True
    return False

def conv2png(img):
    if img[:4] == headers['png']:
        return img
    img = Image.open(BytesIO(img))
    bio = BytesIO()
    img.save(bio, 'png')
    return bio.getvalue()
