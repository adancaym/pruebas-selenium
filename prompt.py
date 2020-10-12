import unittest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time
import os
import keyboard

class case_use_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r".\drivers\chromedriver.exe")

    def test_search_in_tabs(self):
        driver = self.driver
        localPage = 'file:///' + os.path.dirname(__file__) + '/statics/prompt.html'
        driver.get(localPage)
        element = driver.find_element_by_css_selector('.my-prompt')

        element.click()
        prompt = driver.switch_to.alert
        time.sleep(2)
        prompt.dismiss()
        time.sleep(2)

        element.click()
        prompt = driver.switch_to.alert
        time.sleep(1)
        keyboard.write('Hola')
        time.sleep(1)
        prompt.accept()
        time.sleep(50)



    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    case_use_unittest.main()
