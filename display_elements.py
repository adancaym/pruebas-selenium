import unittest
from selenium import webdriver
import time


class case_use_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r".\drivers\chromedriver.exe")

    def test_search_in_tabs(self):
        driver = self.driver
        driver.get('https://google.com')
        time.sleep(3)

        element = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[2]')

        print(element.is_displayed())
        print(element.is_enabled())
        print(element.is_selected())

        time.sleep(2)


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    case_use_unittest.main()