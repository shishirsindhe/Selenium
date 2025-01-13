from Scripts.POM.HomePage import HomePage
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome


def test_login():
    driver=Chrome()
    driver.get("https://demowebshop.tricentis.com/")
    page=HomePage(driver)
    page.click_login()