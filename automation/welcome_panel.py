from time import sleep
from selenium.webdriver import Chrome as WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from adidas_automation.automation.basepage import BasePage


class WelcomePanel(BasePage):
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.visit_account_btn_xpath = "//button/span[normalize-space(text())"\
                                       "='Visit your account']"

    def wait_loading(self):
        TIMEOUT = 30
        WebDriverWait(self.driver, TIMEOUT)\
            .until(EC.visibility_of_element_located(
                (By.XPATH, self.visit_account_btn_xpath)))

    def visit_account(self):
        self.driver.find_element(
            By.XPATH, self.visit_account_btn_xpath).click()
        sleep(8)
