from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.chrome.options import Options
chrome_options=Options()
chrome_options.add_experimental_option(name="detach",value=True)
driver=Chrome(chrome_options)
driver.maximize_window()
driver.get("https://github.com")
driver.implicitly_wait(10)
driver.find_element("xpath","(//a[contains(@class,'HeaderMenu-link HeaderMenu-link-')])[1]").click()
driver.find_element("xpath","//input[@name='login']").send_keys("shishirsindhe")
driver.find_element("xpath","//input[@name='password']").send_keys("shishirsindhe_15_11_1999")
driver.find_element("xpath","//input[@name='commit']").click()
driver.find_element("xpath","//img[@class='avatar circle']").click()
driver.find_element("xpath","//span[.='Your repositories']").click()
driver.find_element("xpath","//a[contains(.,' Selenium')]").click()
element=driver.find_element("xpath","(//a[.='Github.py'])[2]")
if element.is_displayed():
    assert True

