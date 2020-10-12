import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class case_use_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r".\drivers\chromedriver.exe")

    def test_search_in_tabs(self):
        driver = self.driver
        driver.get('http://www.gmail.com')
        time.sleep(1)

        driver.get('http://www.google.com')
        time.sleep(1)

        driver.get('http://www.youtube.com')
        time.sleep(1)

        driver.back()
        time.sleep(1)

        driver.back()
        time.sleep(1)

        driver.forward();
        time.sleep(1)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    case_use_unittest.main()
