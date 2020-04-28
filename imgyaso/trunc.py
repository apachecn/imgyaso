import sys
import cv2
import numpy as np

def trunc_bts(img, l=4):
    img = cv2.imdecode(np.frombuffer(img, np.uint8), cv2.IMREAD_GRAYSCALE)
    img = trunc(img, l).astype(np.uint8)
    img = bytes(cv2.imencode('.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 9])[1])
    return img


def trunc(img, l=4):
    assert img.ndim == 2
    
    colors = np.linspace(0, 255, l).astype(int)
    
    img_3d = np.expand_dims(img, 2)
    dist = np.abs(img_3d - colors)
    idx = np.argmin(dist, axis=2)
    img = colors[idx]
    
    return img

def main():
    fname = sys.argv[1]
    img = open(fname, 'rb').read()
    img = trunc_bts(img)
    with open(fname, 'wb') as f:
        f.write(img)
    
if __name__ == '__main__': main()