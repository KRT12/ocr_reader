#!/usr/bin/env python

import sys
import re
import pytesseract


def extract_pan_details(path):
    print(path)
    try:
        from PIL import Image
    except:
        print("please install PIL package")
        sys.exit()
    img = Image.open(path)
    img = img.convert('RGB')
    pix = img.load()

    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if pix[x, y][0] < 102 or pix[x, y][1] < 102 or pix[x, y][2] < 102:
                pix[x, y] = (0, 0, 0, 255)
            else:
                pix[x, y] = (255, 255, 255, 255)

    img.save('temp.jpg')

    # extracting text from image using tesseract
    text_in = pytesseract.image_to_string(Image.open('temp.jpg'))
    text = list(filter(lambda x: ord(x) < 128, text_in))
    # print(text_in)
    # print(text)

    text_output = open('outputbase.txt', 'w')
    text_output.write(text_in)
    text_output.close()

    file = open('outputbase.txt', 'r')
    text = file.read()

    text0 = []
    text1 = []
    govRE_str = '(GOVERNMENT|OVERNMENT|VERNMENT|DEPARTMENT|EPARTMENT\
                 |PARTMENT|ARTMENT|INDIA|NDIA)$'
    numRE_str = '(Number|umber|Account|ccount|count|Permanent|\
                 ermanent|manent)$'


    lines = text.split('\n')
    for lin in lines:
        s = lin.strip()
        s = s.rstrip()
        s = s.lstrip()
        text1.append(s)

    text1 = list(filter(None, text1))
    print(text1)
    lineno = 0

    for wordline in text1:
        xx = wordline.split()
        if ([w for w in xx if re.search(govRE_str, w)]):
            text1 = list(text1)
            lineno = text1.index(wordline)
            break

    text0 = text1[lineno + 1:]
    print('*' * 10, 'printing text0', '*' * 10)
    print(text0)
    pan_details = {}
    try:
        pan_details['name'] = text0[0]
        pan_details['fname'] = text0[1]
        pan_details['dob'] = text0[2]
        pan_details['pan'] = text0[4]
    except Exception as ex:
        pass
    print(pan_details)
    return pan_details
