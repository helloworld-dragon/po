import time

from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class DisplayPage(BaseAction):
    dispaly_button = By.XPATH, "//*[contains(@text,'显示')]"
    search_button = By.ID, "com.android.settings:id/search"
    search_src_button = By.ID, "android:id/search_src_text"
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    def __init__(self, driver):
        BaseAction.__init__(self, driver)

        self.click_dispaly()

    def click_dispaly(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        # self.find_element(self.dispaly_button).click()
        time.sleep(3)
        self.click(self.dispaly_button)


    def click_search(self):
        # self.driver.find_element_by_id("com.android.settings:id/search").click()
        # self.find_element(self.search_button).click()
        time.sleep(3)
        self.click(self.search_button)


    def input_text(self, text):
        # self.driver.find_element_by_id("android:id/search_src_text").send_keys(text)
        # self.find_element(self.search_src_button).send_keys(text)

        self.input(self.search_src_button, text)


    def click_back(self):
        # self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        # self.find_element(self.back_button).click()
        self.click(self.back_button)
