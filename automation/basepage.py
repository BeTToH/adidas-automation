from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import Chrome as WebDriver


class BasePage():
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_url = "https://www.adidas.com/us"

    def go_to_home_by_url(self):
        self.driver.get(self.base_url)

    def _toggle_input_checkbox(self, input_element: WebElement, should_be_marked: bool):
        is_marked = input_element.get_attribute("value")
        if is_marked and not should_be_marked:
            input_element.click()
        elif not is_marked and should_be_marked:
            input_element.click()
