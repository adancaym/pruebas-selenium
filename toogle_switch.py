import unittest
from selenium import webdriver
import time


class case_use_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r".\drivers\chromedriver.exe")

    def test_search_in_tabs(self):
        driver = self.driver
        driver.get('https://www.w3schools.com/howto/howto_css_switch.asp')
        time.sleep(1)
        toggle = driver.find_element_by_xpath('//*[@id="main"]/label[3]/div')
        toggle.click()
        time.sleep(1)
        toggle.click()
        time.sleep(1)


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    case_use_unittest.main()