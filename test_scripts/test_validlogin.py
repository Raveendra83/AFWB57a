import time

from generic.base_test import BaseTest
from generic.utility import Excel
from pages.login_page import LoginPage
class TestValidLogin(BaseTest):

    def test_validlogin(self):
        loginpage = LoginPage(self.driver)
        # 1. Enter valid username
        loginpage.set_username("admin")
        # 2. Enter valid password
        loginpage.set_password("manager")
        # 3. click on login button
        loginpage.click_loginbutton()
        # 4. verify that home page is displayed
        time.sleep(5)


