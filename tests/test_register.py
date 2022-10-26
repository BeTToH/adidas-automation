from os import makedirs
from pathlib import Path
import unittest
from time import sleep
from dotenv import dotenv_values
from selenium import webdriver
import undetected_chromedriver as uc

from adidas_automation.automation.header import Header
from adidas_automation.automation.login_singup_modal import LoginSignUpModal
from adidas_automation.utils import get_random_string


class Register(unittest.TestCase):
    def setUp(self):
        config = dotenv_values()
        TEST_RESULTS_PATH = config.get('TEST_RESULTS_PATH')
        self.EMAIL = config["EMAIL"]
        self.PASSWORD = config.get("PASSWORD", get_random_string(10) + "#Aa1")
        self.ARTIFACTS_PATH = f"{TEST_RESULTS_PATH}/{self.__class__.__name__}"
        if not Path(self.ARTIFACTS_PATH).exists():
            makedirs(self.ARTIFACTS_PATH)

        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--incognito")
        self.driver = uc.Chrome(options=options)
        self.driver.implicitly_wait = 3
        self.login_modal = LoginSignUpModal(self.driver)
        self.header = Header(self.driver)

        self.login_modal.go_to_home_by_url()
        sleep(5)

    def test_register(self):
        """Tests Adidas.com register feature."""
        screenshot_path = f"{self.ARTIFACTS_PATH}/test_register.png"
        self.header.click_profile_icon()
        self.login_modal.input_email(self.EMAIL)
        self.login_modal.click_on_continue()
        self.login_modal.input_password(self.PASSWORD)
        self.login_modal.toggle_over_13_checkbox(True)
        self.login_modal.toggle_terms(True)
        welcome_panel = self.login_modal.click_on_register_button()
        welcome_panel.visit_account()
        self.driver.save_screenshot(screenshot_path)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
