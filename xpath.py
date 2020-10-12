import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class case_use_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r".\drivers\chromedriver.exe")

    def test_search_by_path(self):
        driver = self.driver
        driver.get('http://www.google.com')
        time.sleep(3)
        search_by_xpath = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
        time.sleep(3)
        search_by_xpath.send_keys('selenium')
        time.sleep(3)
        search_by_xpath.send_keys(Keys.ARROW_DOWN)
        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    case_use_unittest.main()