from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    # Class constructor
    def __init__(self, driver):
        self.driver = driver

    # Page Locators
    NAVIGATION_BAR = (By.ID, "navbarNavDropdown")

    def click_element(self, by_locator):
        try:
            WebDriverWait(self.driver, 10) \
                .until(EC.element_to_be_clickable(by_locator)) \
                .click()
        except:
            raise Exception("Button: ", by_locator, " was NOT found in page!")

    def send_keys(self, by_locator, text):
        try:
            WebDriverWait(self.driver, 10) \
                .until(EC.visibility_of_element_located(by_locator)) \
                .clear()
            self.driver.find_element(*by_locator).send_keys(text)
        except:
            raise Exception("Locator: ", by_locator, " was NOT found in page!")

    def get_element_text(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return element.text
        except:
            raise Exception("Could NOT get Element Text. Locator: ", by_locator, " NOT found!")

    def is_enabled(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
            return bool(element)
        except:
            raise Exception("Could NOT check if element is Enabled. Locator: ", by_locator, " NOT found!")

    def is_element_visible(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return bool(element)
        except:
            raise Exception("Could NOT check if element is Visible. Locator: ", by_locator, " NOT found!")
