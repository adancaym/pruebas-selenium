import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
import time


class case_use_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r".\drivers\chromedriver.exe")

    def test_search_in_tabs(self):
        driver = self.driver
        driver.get('https://www.google.com')
        element = driver.find_element_by_link_text('Privacidad')
        hover = ActionChains(driver).move_to_element(element)
        hover.perform()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    case_use_unittest.main()