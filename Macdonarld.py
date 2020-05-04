from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request
import time
import os

def waitForLoad(driver):
    elem = driver.find_element_by_tag_name("html")
    count = 0
    while True:
        count += 1
        if count > 20:
            print("Timing out after 10 seconds and returning")
            return
        time.sleep(.5)

driver = webdriver.PhantomJS(executable_path = "/home/kernel/Desktop/phantomjs-2.1.1-linux-x86_64/bin/phantomjs")
driver.get("https://www.mcdonalds.co.kr/kor/menu/list.do")

#Wait for loading the html
waitForLoad(driver)

Menu = driver.find_elements_by_xpath("//strong[@class='ko']")
MenuImage = driver.find_elements_by_xpath("//div[@class='thum']/img")

for menu in Menu:
    print(menu.text)
tmp = 0
for menuimage in MenuImage:
    print(menuimage.get_attribute("src"))
    urllib.request.urlretrieve(menuimage.get_attribute("src"), "./Macdonarld/" + Menu[tmp].text)
    tmp += 1

element_to_hover_over1 = driver.find_element_by_xpath("//ul[@class='depth1']")
ActionChains(driver).move_to_element(element_to_hover_over1).perform()
element_to_hover_over2 = driver.find_element_by_xpath("//a[@class='dth1 current']")
ActionChains(driver).move_to_element(element_to_hover_over2).perform()
click_elements = driver.find_elements_by_xpath("//ul[@class='depth2']/li/a")

for click_element in click_elements:
    print(click_element.text)



