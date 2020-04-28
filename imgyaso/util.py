import subprocess as subp
import tempfile
import uuid
import os
from os import path

def conv2png(img):
    if img[:4] == b'\x89PNG':
        return img
    fname = path.join(
        tempfile.gettempdir(), 
        uuid.uuid4().hex + '.png'
    )
    with open(fname, 'wb') as f:
        f.write(img)
    subp.Popen(
        ['convert', fname + '[0]', fname],
        shell=True,
        stdout=subp.PIPE,
        stderr=subp.PIPE,
    ).communicate()
    with open(fname, 'rb') as f:
        img = f.read()
    os.unlink(fname)
    return img
