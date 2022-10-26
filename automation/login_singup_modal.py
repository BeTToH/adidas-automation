from selenium.webdriver import Chrome as WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from adidas_automation.automation.basepage import BasePage
from adidas_automation.automation.welcome_panel import WelcomePanel


class LoginSignUpModal(BasePage):
    def __init__(self, driver: WebDriver):
        """
            Page Object Model for the Login/Sign Up component
        """
        super().__init__(driver)
        self.email_id = "login-register-auto-flow-input"
        self.continue_xpath = "//button[@data-auto-id='login-auto-flow-form"\
                              "-button']"
        self.registration_passw_id = "registration-password-field"
        self.over_13_cb_id = "autoFlowRegistration-registration-"\
                             "ageconfirmation-field"
        self.terms_cb_id = "registration-terms-field autoFlowRegistration"
        self.register_btn_xpath = "//button[@data-auto-id='registration"\
                                  "-submit-button']"
        self.loader_xpath = "//*[contains(@class, 'loader') or "\
                            "contains(., 'loading-spinner')]"
        self._default_timeout = 15

    def input_email(self, email: str):
        WebDriverWait(self.driver, self._default_timeout)\
            .until(EC.visibility_of_element_located((By.ID, self.email_id)))
        email_input = self.driver.find_element(By.ID, self.email_id)
        email_input.send_keys(email)
        sleep(1)

    def click_on_continue(self):
        self.driver.find_element(By.XPATH, self.continue_xpath).click()

    def input_password(self, password: str):
        passw_input_locator = (By.ID, self.registration_passw_id)
        WebDriverWait(self.driver, self._default_timeout)\
            .until(EC.visibility_of_element_located(passw_input_locator))
        passw_input = self.driver.find_element(*passw_input_locator)
        passw_input.send_keys(password)

    def toggle_over_13_checkbox(self, should_be_marked: bool):
        over_13_cb = self.driver.find_element(By.ID, self.over_13_cb_id)
        self._toggle_input_checkbox(over_13_cb, should_be_marked)

    def toggle_terms(self, should_be_marked: bool):
        terms_cb = self.driver.find_element(By.ID, self.terms_cb_id)
        self._toggle_input_checkbox(terms_cb, should_be_marked)

    def click_on_register_button(self) -> WelcomePanel:
        register_btn = self.driver.find_element(
            By.XPATH, self.register_btn_xpath)
        register_btn.click()
        sleep(3)
        try:
            register_btn.click()
        except Exception:
            pass
        welcome_panel = WelcomePanel(self.driver)
        welcome_panel.wait_loading()
        return welcome_panel
