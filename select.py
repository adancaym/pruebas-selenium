import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


class case_use_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r".\drivers\chromedriver.exe")

    def test_search_in_tabs(self):
        driver = self.driver
        driver.get('https://www.w3schools.com/howto/howto_custom_select.asp')
        time.sleep(1)
        select = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[1]/select')
        options = select.find_elements_by_tag_name('option')
        for option in options:
            print('Los valores son {}'.format(option.get_attribute('value')))
            option.click()
            time.sleep(1)
        seleccionar = Select(select)
        seleccionar.select_by_value("10")
        time.sleep(1)


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    case_use_unittest.main()