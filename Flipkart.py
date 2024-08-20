from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.chrome.options import Options
chrome_options=Options()
chrome_options.add_experimental_option(name="detach",value=True)
driver=Chrome(chrome_options)
driver.maximize_window()
driver.get("https://github.com")
driver.save_screenshot("git.png")
driver.get_screenshot_as_file("github.jpg")