from selenium.webdriver import Chrome as WebDriver
from selenium.webdriver.common.by import By
from adidas_automation.automation.basepage import BasePage


class Header(BasePage):
    def __init__(self, driver: WebDriver):
        """
            Page Object Model for the header component
        """
        super().__init__(driver)
        self.profile_icon_xpath = "//button[@data-auto-id="\
                                  "'profile-icon-header']"

    def click_profile_icon(self):
        profile_icon = self.driver.find_element(
            By.XPATH, self.profile_icon_xpath)
        profile_icon.click()

    def click_home_icon(self):
        pass

    def hover_over_category(self, category: str):
        pass
