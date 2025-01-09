from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
chrome_options=Options()
chrome_options.add_experimental_option(name="detach",value=True)
driver=Chrome(chrome_options)
driver.maximize_window()

# Slider Actions
# driver.get("https://snapdeal.com/")
# driver.find_element("xpath","//input[@class='col-xs-20 searchformInput keyword']").send_keys("mobiles")
# sleep(5)
# driver.find_element("xpath","//span[@class='searchTextSpan']").click()
# element=driver.find_element("xpath","//a[@class='price-slider-scroll right-handle ui-slider-handle ui-state-default ui-corner-all hashAdded']")
# action=ActionChains(driver)
# action.click_and_hold(element).pause(2).move_by_offset(-50,0).perform()

########################################################################################################################

# Script to scroll to element using ActionChains
# driver.find_element("xpath","//input[@class='col-xs-20 searchformInput keyword']").send_keys("Kitchen Product")
# sleep(5)
# driver.find_element("xpath","//span[@class='searchTextSpan']").click()
# element=driver.find_element("xpath","//div[@data-filtername='BodyMaterial_s']")
# action.scroll_to_element(element).perform()

########################################################################################################################

# Script Execution Scroll (without in-built methods)
# loc=element.location
# driver.execute_script(f"window.scrollBy({loc['x']},{loc['y']})")

########################################################################################################################

# Script to click on google search and enter your name and print all your names
# driver.get("https://www.google.com/")
# driver.find_element("xpath","//textarea[@class='gLFyf']").send_keys("Python")
# action=ActionChains(driver)
# action.send_keys(Keys.ENTER).perform()
# items=driver.find_elements("xpath","//*[contains(text(),'Python')]")
# py=[]
# for item in items:
#     py.append(item.text)
# print(py)
# print(len(py))

########################################################################################################################

# Get all Chrome details
# driver.get("https://practice.expandtesting.com/dynamic-table")
# for _ in range(10):
#     details = driver.find_elements("xpath", "//td[.='Chrome']/..//td")
#     for detail in details:
#         print(detail.text)
#     print('*' * 15)
#     driver.refresh()

########################################################################################################################

# Script to get all the python release links
# driver.get("https://www.python.org/downloads/")
# elements=driver.find_elements("xpath","//div[@class='row download-list-widget']//a[contains(.,'Python')]")
# for element in elements:
#     print(element.text)
#     print(element.get_attribute("href"))
#     sleep(2)

########################################################################################################################

# Script to print all the values of nifty 50 from share market
# driver.get("https://www.nseindia.com/market-data/live-equity-market")
# sleep(5)
# stock=driver.find_element("xpath","//td[.='NIFTY 50']/..//td[@class='bold text-right lowHighInd']")
# for _ in range(100):
#     stock = driver.find_element("xpath", "//td[.='NIFTY 50']/..//td[@class='bold text-right lowHighInd']")
#     print(stock.text)

########################################################################################################################

# Script to scroll down and capture every element on amazon
# driver.get("https://www.amazon.in/s?k=mobile&crid=TP7PVIAE1PBB&sprefix=mobile%2Caps%2C254&ref=nb_sb_noss_1")
# elements=driver.find_elements("xpath","//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']")
# for element in elements:
#     print(element.text)
#     print(element.get_attribute("href"))
#     sleep(2)
#     pics=element.screenshot_as_png

########################################################################################################################
# driver.get("https://www.cardekho.com/")
# sleep(10)
# driver.find_element("xpath","//i[.='By Brand']/..//span[@class='gs_control__indicator']").click()
# element=driver.find_element("xpath","//input[@id='bmvBrand']")
# element.click()
# cars=driver.find_elements("xpath","//li[@class='gs_ta_choice']")
# for car in cars:
#     element.send_keys(car.text)
#     action=ActionChains(driver)
#     element1=driver.find_element("xpath","//input[@name='bmvModel']")
#     element1.click()
#     models=driver.find_elements("xpath","//input[@name='bmvModel']/..//li")
#     for model in models:
#         element1.send_keys(model.text)
#         action.send_keys(Keys.ENTER)

######################################################################################################################

# script to print OS and it's versions from demo.html
# driver.get("file:///C:/Users/SHISHIR/Desktop/demo.html")
# versions=driver.find_elements("xpath","//table[@name='os']//td")
# Method 1
# OS=["Android","Linux","Windows","iOS"]
# version=["3.141","3.6.0","3.140","3.141"]
# title=[]
# out={}
# for element in versions:
#     if not element.text=="Download":
#         title.append(element.text)
# for os,ver in zip(OS,version):
#     if os in title or ver in title:
#         out[os]=ver
# print(out)

# Method2
# OS=[]
# version=[]
# for element in versions:
#     if not element.text=="Download":
#         if 'A'<=element.text<='z':
#             OS.append(element.text)
#         else:
#             version.append(element.text)
#
# out={os:ver for os,ver in zip(OS,version)}
# print(out)
#####################################################################################################################

# Script to click on all the checkboxes of the Languages
# driver.get("file:///C:/Users/SHISHIR/Desktop/demo.html")
# boxes=driver.find_elements("xpath","//table[@style='width:50%']//tr//td//input")
# for box in boxes:
#     box.click()

#####################################################################################################################

# Script to demonstrate handeling of listboxes

# driver.get("file:///C:/Users/SHISHIR/Desktop/demo.html")
# list_box=driver.find_element("xpath","//select[@id='multiple_cars']")
# select=Select(list_box)
# select.select_by_visible_text("Audi")
# sleep(2)
# select.select_by_visible_text("Mercedes")
# sleep(2)
# select.select_by_index(2)
# sleep(2)
# select.select_by_value("jgr")

# To print all the options of the listbox
# all_options=select.options
# for opt in all_options:
#     print(opt.text)

# To Select every option one by one
# for opt in all_options:
#     select.select_by_visible_text(opt.text)
#     sleep(2)


# Script to assert if all the elements are selected in the dropdown or not
# def assert_dropdown():
#     drop_options=select.options
#     options=[opt.text for opt in drop_options]
#     for opt in options:
#         select.select_by_visible_text(opt)
#     select.deselect_by_index(3)
#     for ele in drop_options:
#         if not ele.is_selected():
#             return False
#         continue
#     return True

####################################################################################################################

# Script to handel input boxes with same html structure

# driver.get("file:///C:/Users/SHISHIR/OneDrive/Desktop/demo.html")
# first_input_boxes=driver.find_elements("xpath","//input[@class='first_row']")
# cars=["Mercedes","Ferrari","Bugatti"]
# for box,car in zip(first_input_boxes,cars):
#     box.send_keys(car)
# second_input_boxes=driver.find_elements("xpath","//input[@class='second_row']")
# bikes=["kawasaki","Ducati","Yamaha"]
# for box,bike in zip(second_input_boxes,bikes):
#     box.send_keys(bike)
# third_input_boxes=driver.find_elements("xpath","//input[@class='third_row']")
# Airplanes=["Airbus","Boeing","F-16"]
# for box,plane in zip(third_input_boxes,Airplanes):
#     box.send_keys(plane)

#####################################################################################################################

# Script to Click all the checkboxes of OS

# driver.get("file:///C:/Users/SHISHIR/OneDrive/Desktop/demo.html")
# boxes=driver.find_elements("xpath","//input[@name='download']")
# for box in boxes:
#     box.click()
#     sleep(2)

####################################################################################################################

#Script to print all Languages in the column

# driver.get("file:///C:/Users/SHISHIR/OneDrive/Desktop/demo.html")
# languages=driver.find_elements("xpath","//table[@name='selenium']//tr//td")
# output=[]
# for language in languages:
#     out = ""
#     out+=language.text
#     if out.isalpha():
#         output.append(out)
# print(output)

###################################################################################################################