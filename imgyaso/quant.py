import sys
import cv2
import libimagequant as liq
from PIL import Image
from io import BytesIO
from .util import *

def pngquant(img, ncolors=8):
    img = cv2.imencode(
        '.png', img, 
        [cv2.IMWRITE_PNG_COMPRESSION, 9]
    )[1]
    img = bytes(img)
    img = pngquant_bts(img, ncolors)
    img = np.frombuffer(img, np.uint8)
    return cv2.imdecode(img, cv2.IMREAD_UNCHANGED)

def pngquant_bts(img, ncolors=8):
    img = conv2png(img)
    img = Image.open(BytesIO(img)).convert('RGBA')
    w, h = img.width, img.height
    bytes = img.tobytes()
    
    attr = liq.Attr()
    attr.max_colors = ncolors
    img = attr.create_rgba(bytes, w, h, 0)
    res = img.quantize(attr)
    res.dithering_level = 1.0
    bytes = res.remap_image(img)
    palette = res.get_palette()
    
    img = Image.frombytes('P', (w, h), bytes)
    
    palette_data = []
    for color in palette:
        palette_data.append(color.r)
        palette_data.append(color.g)
        palette_data.append(color.b)
    img.putpalette(palette_data)
    
    bio = BytesIO()
    img.save(bio, 'PNG', optimize=True)
    return bio.getvalue()

def main():
    fname = sys.argv[1]
    img = open(fname, 'rb').read()
    img = pngquant_bts(img)
    with open(fname, 'wb') as f:
        f.write(img)
    
if __name__ == '__main__': main()