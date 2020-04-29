import subprocess as subp
import tempfile
import uuid
import os
from os import path
import sys
from .util import *

def pngquant(img, ncolors=8):
    img = bytes(cv2.imencode('.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 9])[1])
    img = pngquant_bts(img, ncolors)
    return cv2.imdecode(np.frombuffer(img, np.uint8), cv2.IMREAD_UNCHANGED)

def pngquant_bts(img, ncolors=8):
    img = conv2png(img)
    fname = path.join(
        tempfile.gettempdir(), 
        uuid.uuid4().hex + '.png'
    )
    with open(fname, 'wb') as f:
        f.write(img)
    subp.Popen(
        ['pngquant', str(ncolors), fname, '-o', fname, '-f'],
        stdout=subp.PIPE,
        stderr=subp.PIPE,
    ).communicate()
    with open(fname, 'rb') as f:
        img = f.read()
    os.unlink(fname)
    return img
    
def main():
    fname = sys.argv[1]
    img = open(fname, 'rb').read()
    img = pngquant_bts(img)
    with open(fname, 'wb') as f:
        f.write(img)
    
if __name__ == '__main__': main()