import sys, os

sys.path.append(os.getcwd())
from base.base_driver import init_driver
from page.dispaly_page import DisplayPage


class TestDisplay:

    def setup(self):
        self.driver = init_driver()
        self.display_page = DisplayPage(self.driver)

    def test_mobile_display_input(self):
        self.display_page.click_search()
        self.display_page.input_text("hello")
        self.display_page.click_back()

    def teardown(self):
        self.driver.quit()
