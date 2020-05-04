from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import subprocess
import requests
from PIL import Image
from PIL import ImageOps

def cleanImage(imagepath):
    image = Image.open(imagepath)
    image = image.point(lambda x : 0 if x < 143 else 255)
    borderImage = ImageOps.expand(image, border = 20, fill = 'white')
    borderImage.save(imagepath)

html = urlopen("http://www.pythonscraping.com/humans-only")
bsObj = BeautifulSoup(html, "html.parser")

imageLocation = bsObj.find("img", {"title" : "Image CAPTCHA"})["src"]
formBuildId = bsObj.find("input", {"name" : "form_build_id"})["value"]
captchaSid = bsObj.find("input", {"name" : "captcha_sid"})["value"]
captchaToken = bsObj.find("input", {"name" : "captcha_token"})["value"]

captchaUrl = "http://pythonscraping.com" + imageLocation
urlretrieve(captchaUrl, "captcha.jpg")
cleanImage("captcha.jpg")
p = subprocess.Popen(["tesseract", "captcha.jpg", "captcha"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
f = open("captcha.txt", "r")

captchaResponse = f.read().replace(" ", "").replace("\n", "")
print(captchaResponse)
