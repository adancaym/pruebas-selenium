import unittest
from selenium import webdriver
import time


class case_use_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r".\drivers\chromedriver.exe")

    def test_search_in_tabs(self):
        driver = self.driver
        driver.get('https://www.w3schools.com/howto/howto_css_custom_checkbox.asp')
        time.sleep(1)
        radio_button = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[2]/label[2]')
        radio_button.click()
        time.sleep(1)
        radio_button.click()
        time.sleep(1)

        radio_button = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[2]/label[4]')
        radio_button.click()
        time.sleep(1)
        radio_button.click()
        time.sleep(1)


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    case_use_unittest.main()