from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
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

# Scroll to element using ActionChains
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