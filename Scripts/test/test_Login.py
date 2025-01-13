from Scripts.POM.HomePage import HomePage
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from pytest import mark

headers="email,password"
data=[
    ("abc@gmail.com","123456789"),
    ("def@gmail.com","123456789")
]

@mark.parametrize(headers,data)
def test_login(pages,email,password):
    pages.homepage.click_login()
    pages.loginpage.login_process(email,password)
