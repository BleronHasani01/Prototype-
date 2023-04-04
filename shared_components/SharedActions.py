from selenium.common import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class MainPage:
    # Class constructor
    def __init__(self, driver):
        self.driver = driver

    # Page Locators
    def click_element(self, by_locator):
        try:
            WebDriverWait(self.driver, 50) \
                .until(EC.element_to_be_clickable(by_locator)) \
                .click()
        except WebDriverException as wd_exc:
            raise Exception(str("message")+ 'Button: ', str(by_locator),'was Not found in page!') from wd_exc

    def send_keys(self, by_locator, text):
        try:
            WebDriverWait(self.driver, 50) \
                .until(EC.visibility_of_element_located(by_locator)) \
                .clear()
            self.driver.find_element(*by_locator).send_keys(text)
        except TimeoutException as timeout:
            raise Exception(str("message")+'Locator'+str(by_locator)+'was NOT found in page') from timeout

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(by_locator))
        return element.text

    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(by_locator))
        return bool(element)

    def is_element_visible(self, by_locator):
        element = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def is_element_visible_special_wait(self, by_locator):
        element = WebDriverWait(self.driver, 70).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def is_element_invisible(self, by_locator):
        element = WebDriverWait(self.driver, 100).until(EC.invisibility_of_element_located(by_locator))
        return bool(element)

    def clear_input(self, by_locator):
        element = self.driver.find_element(*by_locator).clear_field()
        return bool(element)

    def hover_mouse(self, by_locator):
        element = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def js_click(self, by_locator):
        element = self.driver.find_element(*by_locator)
        self.driver.execute_script("arguments[0].click();", element)


