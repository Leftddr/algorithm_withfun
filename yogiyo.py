from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import urllib.request
import time
import os

wait_time = 2

driver = webdriver.PhantomJS(executable_path = "/home/kernel/Desktop/phantomjs-2.1.1-linux-x86_64/bin/phantomjs")
driver.get("https://www.yogiyo.co.kr/mobile/#/")

My_pos = '단대동'

search = driver.find_element_by_xpath("//input[@name='address_input']")
search_button = driver.find_element_by_xpath("//button[@class='btn btn-default ico-pick']")
search.send_keys(My_pos)
search_button.click()

time.sleep(wait_time)

Pos_list = driver.find_elements_by_xpath("//a[@role='menuitem']")

tmp = 1
for pos in Pos_list:
    print(str(tmp) + ' .' + pos.text)
    tmp += 1

user_num = int(input())
if(user_num >= len(Pos_list)):
    global user_num
    print('Wrong Number')
    user_num = int(input())

Pos_list[user_num].click()

time.sleep(wait_time)

Restaurant_List = driver.find_elements_by_xpath("//div[@class='item clearfix']")
ImageList = driver.find_elements_by_xpath("//div[@class='logo']")
Restaurant_Name = driver.find_elements_by_xpath("//div[@ng-bind='restaurant.name']")
Review_avg = driver.find_elements_by_xpath("//span[@ng-show='restaurant.review_avg > 0']")
Review_count = driver.find_elements_by_xpath("//span[@ng-show='restaurant.review_count > 0']")
Owner_reply = driver.find_elements_by_xpath("//span[@ng-show='restaurant.owner_reply_count > 0']")

tmp = 1
for i in range(len(Restaurant_Name)):
    print(str(tmp) + ' .' + Restaurant_Name[i].text)
    print(Review_avg[i].text)
    print(Review_count[i].text)
    print(Owner_reply[i].text)
    print('\n')
    tmp += 1

user_num = int(input())
if(user_num >= len(Restaurant_List)):
    global user_num
    print('Wrong Number')
    user_num = int(input())

Restaurant_List[user_num].click()
time.sleep(wait_time)

element_to_click = driver.find_elements_by_xpath("//div[@class='panel-heading']")

next_height = 53
prev_height = 0

for i in range(7):
    tmp_str = 'window.scrollTo( ' + str(prev_height) + ',' + str(next_height) + ');'
    print(tmp_str)
    driver.execute_script(tmp_str)
    time.sleep(1)
    element_to_click[i].click()
    prev_height = next_height
    next_height += 53

time.sleep(wait_time)

MenuList = driver.find_elements_by_xpath("//div[@ng-bind-html='item.name|strip_html']")
print(2)
MenuListPrice = driver.find_elements_by_xpath("//span[@ng-bind='item.price|krw']")

for i in range(len(MenuList)):
    print(str(i) + ' .' + MenuList[i].text)
    print(MenuListPrice[i].text)
    




