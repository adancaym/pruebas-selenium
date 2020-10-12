import unittest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time
import os


class case_use_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r".\drivers\chromedriver.exe")

    def test_search_in_tabs(self):
        driver = self.driver
        localPage = 'file:///' + os.path.dirname(__file__) + '/statics/alert.html'
        driver.get(localPage)
        element = driver.find_element_by_css_selector('.my-alert')
        element.click()
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.dismiss()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    case_use_unittest.main()
