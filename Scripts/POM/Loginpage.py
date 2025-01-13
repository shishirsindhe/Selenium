from Scripts.Library.Lib import Wrapper
from Scripts.POM.HomePage import HomePage


class LoginPage(HomePage):
    email_txtfld = ("xpath", "//input[@class='email']")
    pwd_txtfld = ("xpath", "//input[@id='Password']")
    login_btn = ("xpath", "//input[@class='button-1 login-button']")

    def login_process(self,email,password):
        wrapper=Wrapper(self.driver)
        wrapper.enter_text(self.email_txtfld,value=email)
        wrapper.enter_text(self.pwd_txtfld,value=password)
        wrapper.click_item(self.login_btn)