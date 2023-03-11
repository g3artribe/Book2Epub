#!/usr/local/bin/python3
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
from pdf2image import convert_from_path





pdfs = r"mybook.pdf"
pages = convert_from_path(pdfs, 100)

i = 1
for page in pages:
    image_name = "Pages/Page_" + str(i) + ".jpg"  
    page.save(image_name, "JPEG")
    print(f"Page {i}")
    im = Image.open(image_name) # the second one
    im = im.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(2)
    im = im.convert('1')
    im.save('temp2.png')
    #pytesseract.pytesseract.tesseract_cmd = '/usr/local/Cellar/tesseract/5.3.0_1/share/tessdata/'
    text = pytesseract.image_to_string(Image.open('temp2.png'),lang="ben")
    with open("Txt/Page_" + str(i) + ".txt", 'w') as f:
        f.write(text)  
    i = i+1      

