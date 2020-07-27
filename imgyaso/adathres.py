import numpy as np
from scipy import signal
import cv2
import re
import os
from os import path
import sys

def adathres_bts(img, win=9, beta=0.9):
    img = np.frombuffer(img, np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_GRAYSCALE)
    if img is None: return None
    img = adathres(img, win, beta).astype(np.uint8)
    img = cv2.imencode(
        '.png', img, 
        [cv2.IMWRITE_PNG_BILEVEL, 1]
    )[1]
    return bytes(img)

def adathres(img, win=9, beta=0.9):
    if win % 2 == 0: win = win - 1
    # 边界的均值有点麻烦
    # 这里分别计算和和邻居数再相除
    kern = np.ones([win, win])
    sums = signal.correlate2d(img, kern, 'same')
    cnts = signal.correlate2d(np.ones_like(img), kern, 'same')
    means = sums // cnts
    # 如果直接采用均值作为阈值，背景会变花
    # 但是相邻背景颜色相差不大
    # 所以乘个系数把它们过滤掉
    img = np.where(img < means * beta, 0, 255)
    return img
    
def main():
    fname = sys.argv[1]
    img = open(fname, 'rb').read()
    img = adathres_bts(img)
    with open(fname, 'wb') as f:
        f.write(img)

if __name__ == '__main__': main()