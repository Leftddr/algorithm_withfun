import time
from urllib.request import urlretrieve
import subprocess
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path = "/home/kernel/Desktop/phantomjs/bin/phantomjs")
#driver = webdriver.chrome()

driver.get("http://www.amazon.com/Alice-Wonderland-Large-Lewis-Carroll/dp/145155558X")
time.sleep(5)

driver.find_element_by_id("sitbLogoImg").click()
time.sleep(5)

imageList = []

while "pointer" in driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute("style"):
    driver.find_element_by_id("sitbReaderRightPageTurner").click()
    time.sleep(4)
    pages = driver.find_element_by_xpath("//div[@class='pageImage']/div/img")
    for page in pages:
        image = page.get_attribute("src")
        imageList.append(image)
driver.quit()

i = 0
for image in sorted(imageList):
    urlretrieve(image, "page" + str(i) + ".jpg")
    p = subprocess.Popen(["tesseract", "page" + str(i) + ".jpg", "page" + str(i)], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    p.wait()
    f = open("page" + str(i) +".txt", "r", encoding = "utf-8")
    print(f.read())
    i += 1

f.close()