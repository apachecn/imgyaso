# coding: utf-8

# 四色网格仿色

import sys
import cv2
import numpy as np

pts = [
    [0, 0], # 1/16
    [2, 2],
    [0, 2],
    [2, 0],
    [1, 1],
    [3, 3],
    [3, 1],
    [1, 3],
    [2, 3],
    [0, 1],
    [0, 3],
    [2, 1],
    [1, 0],
    [3, 2],
    [1, 2],
    [3, 1], # 16/16
]

settings = [
    {'fc': 0, 'bc': 0, 'k': 0}, # b
    {'fc': 85, 'bc': 0, 'k': 1}, 
    {'fc': 85, 'bc': 0, 'k': 2}, 
    {'fc': 85, 'bc': 0, 'k': 3}, 
    {'fc': 85, 'bc': 0, 'k': 4}, 
    {'fc': 85, 'bc': 0, 'k': 5}, 
    {'fc': 85, 'bc': 0, 'k': 6}, 
    {'fc': 85, 'bc': 0, 'k': 7}, 
    {'fc': 85, 'bc': 0, 'k': 8}, 
    {'fc': 85, 'bc': 0, 'k': 9}, 
    {'fc': 85, 'bc': 0, 'k': 10}, 
    {'fc': 85, 'bc': 0, 'k': 11}, 
    {'fc': 85, 'bc': 0, 'k': 12}, 
    {'fc': 85, 'bc': 0, 'k': 13}, 
    {'fc': 85, 'bc': 0, 'k': 14}, 
    {'fc': 85, 'bc': 0, 'k': 15}, 
    {'fc': 0, 'bc': 85, 'k': 0}, # c1
    {'fc': 85, 'bc': 170, 'k': 15}, 
    {'fc': 85, 'bc': 170, 'k': 14}, 
    {'fc': 85, 'bc': 170, 'k': 13}, 
    {'fc': 85, 'bc': 170, 'k': 12}, 
    {'fc': 85, 'bc': 170, 'k': 11}, 
    {'fc': 85, 'bc': 170, 'k': 10}, 
    {'fc': 85, 'bc': 170, 'k': 9}, 
    {'fc': 85, 'bc': 170, 'k': 8}, 
    {'fc': 85, 'bc': 170, 'k': 7}, 
    {'fc': 85, 'bc': 170, 'k': 6}, 
    {'fc': 85, 'bc': 170, 'k': 5}, 
    {'fc': 85, 'bc': 170, 'k': 4}, 
    {'fc': 85, 'bc': 170, 'k': 3}, 
    {'fc': 85, 'bc': 170, 'k': 2}, 
    {'fc': 85, 'bc': 170, 'k': 1}, 
    {'fc': 0, 'bc': 170, 'k': 0}, # c2
    {'fc': 255, 'bc': 170, 'k': 1}, 
    {'fc': 255, 'bc': 170, 'k': 2}, 
    {'fc': 255, 'bc': 170, 'k': 3}, 
    {'fc': 255, 'bc': 170, 'k': 4}, 
    {'fc': 255, 'bc': 170, 'k': 5}, 
    {'fc': 255, 'bc': 170, 'k': 6}, 
    {'fc': 255, 'bc': 170, 'k': 7}, 
    {'fc': 255, 'bc': 170, 'k': 8}, 
    {'fc': 255, 'bc': 170, 'k': 9}, 
    {'fc': 255, 'bc': 170, 'k': 10}, 
    {'fc': 255, 'bc': 170, 'k': 11}, 
    {'fc': 255, 'bc': 170, 'k': 12}, 
    {'fc': 255, 'bc': 170, 'k': 13}, 
    {'fc': 255, 'bc': 170, 'k': 14}, 
    {'fc': 255, 'bc': 170, 'k': 15}, 
    {'fc': 0, 'bc': 255, 'k': 0}, # w
]

def make_noise(size, fc=0, bc=255, k=8):
    # P(fc) = k/16, P(bc) = (16-k)/16
    if k == 0: return np.zeros(size) + bc
    idx = np.random.random(size) < k/16
    img = np.where(idx, fc, bc)
    return img

def make_grid(size, fc=0, bc=255, k=8):
    img = np.zeros(size) + bc
    for i in range(k):
        r, c = pts[i]
        img[r::4, c::4] = fc
    return img

def grid(img):
    assert img.ndim == 2

    patterns = [make_grid([4, 4], **kw) for kw in settings]

    clrs = np.linspace(0, 255, len(settings)).astype(int)
    delims = (clrs[1:] + clrs[:-1]) // 2
    delims = np.asarray([0, *delims, 256])
    idcs = [np.where((img >= st) & (img < ed)) for st, ed in zip(delims[:-1], delims[1:])]
    
    img = img.copy()
    for idx, pt in zip(idcs, patterns):
        idxm4 = (idx[0] % 4, idx[1] % 4)
        img[idx] = pt[idxm4]
    
    return img

def grid_bts(img):
    img = np.frombuffer(img, np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_GRAYSCALE)
    if img is None: return None
    img = grid(img).astype(np.uint8)
    img = cv2.imencode(
        '.png', img, 
        [cv2.IMWRITE_PNG_COMPRESSION, 9]
    )[1]
    return bytes(img)

def noise(img):
    assert img.ndim == 2

    clrs = np.linspace(0, 255, len(settings)).astype(int)
    delims = (clrs[1:] + clrs[:-1]) // 2
    delims = np.asarray([0, *delims, 256])
    idcs = [np.where((img >= st) & (img < ed)) for st, ed in zip(delims[:-1], delims[1:])]
    
    img = img.copy()
    for idx, kw in zip(idcs, settings):
        img[idx] = make_noise(len(idx[0]), **kw)
    
    return img

def noise_bts(img):
    img = np.frombuffer(img, np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_GRAYSCALE)
    if img is None: return None
    img = noise(img).astype(np.uint8)
    img = cv2.imencode(
        '.png', img, 
        [cv2.IMWRITE_PNG_COMPRESSION, 9]
    )[1]
    return bytes(img)

def main():
    fname = sys.argv[1]
    img = open(fname, 'rb').read()
    img = grid_bts(img)
    with open(fname, 'wb') as f:
        f.write(img)

if __name__ == '__main__': main()