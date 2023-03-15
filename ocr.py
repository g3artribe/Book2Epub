#!/usr/local/bin/python3
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
from pdf2image import convert_from_path
import argparse
import os
import pandas
import cv2
import numpy as np

parser = argparse.ArgumentParser(prog='ocr.py', allow_abbrev=True,description='This script will ocr texts')
parser.add_argument('-p', help='Project name',default=None,required=True)
parser.add_argument('--skip', help='skip',type=int,default=0)
parser.add_argument('-s', help='startpage',type=int,default=1)
parser.add_argument('-e', help='endpage',type=int,default=1500)
parser.add_argument('-w', help='watermark',type=bool,default=False)
args = parser.parse_args()
pdf=args.p
skip=args.skip
stpg=args.s
wm=args.w
if (os.path.exists(f"{pdf}-bbox.csv")):
    # reading the CSV file
    bounding_box = [tuple(x) for x in pandas.read_csv(f"{pdf}-bbox.csv", header=None).values.tolist()][0]
    print(f"BBOX: {bounding_box}")
else:
    print(f"No BBOX")
#bounding_box=(295,	292,	4671,	6941)
for page in range(stpg,args.e):
    if(page < stpg+skip):
        continue
    image_name = f"tiffs/{pdf}-" + str(page) + ".png" 
    if (not os.path.exists(image_name)): 
        continue
    #page.save(image_name, "JPEG")
    print(f"Page {page}")
    im = Image.open(image_name) # the second one
    im = im.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(2)

    #im = im.convert('1')
    kernel = np.ones((1, 1), np.uint8)
    im=np.array(im)
    im=cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    try:
        im=cv2.adaptiveThreshold(im.astype(np.uint8), 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 41,3)
    except:
        pass
    if(wm):
        print('WMR')
        watermark = cv2.medianBlur(im, 15)
        im = cv2.subtract(watermark, im)
        im = cv2.bitwise_not(im)
    im = cv2.dilate(im, kernel, iterations=1)
    im = cv2.erode(im, kernel, iterations=1)
    try:
        im=im.crop(bounding_box)
    except:
        pass
        #print('BBOX absent')
    #im.save('temp2.png')
    #pytesseract.pytesseract.tesseract_cmd = '/usr/local/Cellar/tesseract/5.3.0_1/share/tessdata/'
    text = pytesseract.image_to_string(im,lang="ben")
    with open(f"txt/{pdf}-{page}.txt", 'w') as f:
        f.write(text)  
    #i = i+1      


