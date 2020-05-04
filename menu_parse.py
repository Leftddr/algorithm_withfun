from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request
import pymysql
import time
import os

driver = webdriver.PhantomJS(executable_path = "/home/kernel/Desktop/phantomjs-2.1.1-linux-x86_64/bin/phantomjs")
driver.get("https://www.mcdonalds.co.kr/kor/main.do")
BigMenu = []
folderName = 'Macdonarld'

def initDatabase():
    conn = pymysql.connect(host = 'localhost', user = 'tester', password = 'root', db = 'tester', charset = 'utf8')
    cursor = conn.cursor()
    conn.commit()
    return conn, cursor

def insertDatabase(menuname, menuimage, cursor):
    sql = 'INSERT INTO MENU (MenuName, MenuImage) VALUES (%s, %s)'
    cursor.execute(sql, (menuname, menuimage))

def waitForLoad(driver):
    elem = driver.find_element_by_tag_name('html')
    count = 0
    while True:
        count += 1
        if count > 10:
            print('Timing out after 10 seconds and returning')
            return
        time.sleep(.5)

def parseBigMenu(driver, BigMenu, count, cri, parse_count):
    element_to_hover_over1 = driver.find_element_by_xpath("//ul[@class='depth1']")
    ActionChains(driver).move_to_element(element_to_hover_over1).perform()
    element_to_hover_over2 = None
    if cri:
        element_to_hover_over2 = driver.find_element_by_xpath("//a[@class='dth1 ']")
    #else:
        #element_to_hover_over2 = driver.find_element_by_xpath("//a[@class='dth1 current']")
    #ActionChains(driver).move_to_element(element_to_hover_over2).perform()
    click_elements = driver.find_elements_by_xpath("//ul[@class='depth2']/li/a")

    if cri:
        for tmp in range(count):
            BigMenu.append(click_elements[tmp].text)
        print(BigMenu)
    else:
        click_elements[parse_count].click()

def parseAloneSetMenu(driver):
    setMenu = driver.find_elements_by_xpath("//a[@role='button']")
    setMenu[1].click()
    time.sleep(3)

def parseSmallMenu(driver, count, cri, cursor):
    foldername = ''
    if cri:
        foldername = './' + folderName + '/' + BigMenu[count] + '/' + 'alone/'
    else:
        foldername = './' + folderName + '/' + BigMenu[count] + '/' + 'set/'
        parseAloneSetMenu(driver)

    Menu = driver.find_elements_by_xpath("//strong[@class='ko']")
    MenuImage = driver.find_elements_by_xpath("//div[@class='thum']/img")

    print(foldername)
    if not os.path.exists(foldername):
        os.makedirs(foldername)

    for tmp in range(len(Menu)):
        print(Menu[tmp].text)
        urllib.request.urlretrieve(MenuImage[tmp].get_attribute("src"), foldername + '/' + Menu[tmp].text)
        insertDatabase(Menu[tmp].text, foldername + '/' + Menu[tmp].text, cursor)

if __name__ == "__main__":
    conn, cursor = initDatabase()
    waitForLoad(driver)
    parseBigMenu(driver, BigMenu, 5, True, 0)
    for tmp in range(5):
        parseBigMenu(driver, BigMenu, 5, False, tmp)
        time.sleep(1)
        parseSmallMenu(driver, tmp, True, cursor)
        parseSmallMenu(driver, tmp, False, cursor)
    conn.commit()




