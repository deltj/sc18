# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
import pytesseract

from simpleeval import simple_eval

# OCR ain't perfect
def fix(str):
    fixed = ""
    for c in str:
        if   c == 'B': fixed += '3'
        elif c == 'E': fixed += '6'
        elif c == 'F': fixed += '7'
        elif c == 'S': fixed += '5'
        elif c == '=': fixed += '-'
        elif c == '-': fixed += '-'
        elif c == '~': fixed += '-'
        elif c == u'¥': fixed += '7'
        elif c == u'«': fixed += '*'
        else:
            fixed += c

    # this is a thing
    fixed = fixed.replace("C5", "5")
    fixed = fixed.replace("CG", "6")
    fixed = fixed.replace("CC5", "5")
    fixed = fixed.replace("C3", "3")

    return fixed

if __name__ == "__main__":
    # use selenium to screen grab the page
    url = "https://hidden-island-93990.squarectf.com/ea6c95c6d0ff24545cad"
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-extensions")
    options.add_argument("--force-device-scale-factor=2.0")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    screenshot = driver.save_screenshot("ss.png")
    driver.quit();

    # crop it
    img = Image.open("ss.png")
    # these coordinates are probably specific to my computer lolmfaorofl
    #cropped_img = img.crop((0, 57, 1040, 108)) # scale factor=1.0
    cropped_img = img.crop((0, 129, 1467, 256)) # scale factor = 2.0
    cropped_img.save("foo.png", "PNG")

    # use tesseract
    expression = pytesseract.image_to_string(cropped_img)
    print(expression)
    print(fix(expression))
