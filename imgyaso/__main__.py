import argparse
import re
from os import path
from . import __version__
from .adathres import adathres_bts
from .dither import grid_bts, noise_bts
from .quant import pngquant_bts
from .trunc import trunc_bts
from .util import *

modes = ['quant', 'grid', 'noise', 'trunc', 'thres']

is_img = lambda s: re.search(r'\.(jpg|jpeg|gif|png|bmp|webp|tiff)$', s)

def process_file(args):
    if not is_img(args.fname):
        return
    print(args.fname)
    
    with open(args.fname, 'rb') as f:
        img = f.read()
    img = conv2png(img)
    
    if args.mode == 'grid':
        img = grid_bts(img)
    elif args.mode == 'noise':
        img = noise_bts(img)
    elif args.mode == 'trunc':
        img = trunc_bts(img, args.colors)
    elif args.mode == 'quant':
        img = pngquant_bts(img, args.colors)
    elif args.mode == 'thres':
        img = adathres_bts(img)
    if not img:
        print('fail to process')
        return
    
    fname = args.ofname or args.fname
    with open(fname, 'wb') as f:
        f.write(img)

def process_dir(args):
    dname = args.fname
    files = os.listdir(dname)
    
    for f in files:
        f = path.join(dname, f)
        args.fname = f
        process_file(args)

def main():
    parser = argparse.ArgumentParser(prog="ImgYaso", description="provide various image compression methods", formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument("-v", "--version", action="version", version=f"ImgYaso version: {__version__}")
    parser.add_argument('fname', help='file name to be processed')
    parser.add_argument('-c', '--colors', type=int, default=8, help='num of colors')
    parser.add_argument('-m', '--mode', default=modes[0], choices=modes, help='processing mode')
    parser.add_argument('-o', '--ofname', help='output file name')
    args = parser.parse_args()

    if not path.exists(args.fname):
        print('file not found')
        return
        
    if path.isdir(args.fname):
        process_dir(args)
    else:
        process_file(args)
        
    
if __name__ == '__main__': main()