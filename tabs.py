import unittest
from selenium import webdriver
import time


class case_use_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r".\drivers\chromedriver.exe")

    def test_search_in_tabs(self):
        driver = self.driver
        driver.get('http://www.google.com')
        time.sleep(3)
        driver.execute_script("window.open('');")
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])
        driver.get('http://stackoverflow.com')
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    case_use_unittest.main()