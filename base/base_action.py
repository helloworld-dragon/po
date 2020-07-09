from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def click(self, loc):

        self.find_element(loc).click()

    def input(self, loc, text):

        self.find_element(loc).send_keys(text)

    def find_element(self, loc, time=10, poll=1):
        return WebDriverWait(self.driver, time, poll).until(lambda x: x.find_element(loc[0], loc[1]))

    def find_elements(self, loc, time=10, poll=1):
        return WebDriverWait(self.driver, time, poll).until(lambda x: x.find_elements(loc[0], loc[1]))