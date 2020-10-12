import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options;
import time

options_chrome = Options()
options_chrome.add_argument('--headless')


class case_use_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(chrome_options=options_chrome, executable_path=r".\drivers\chromedriver.exe")

    def test_search_in_tabs(self):
        driver = self.driver
        driver.get('https://google.com')
        time.sleep(2)
        search_word = 'Hola Mundo'
        search_input = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
        search_input.send_keys(search_word)
        time.sleep(2)
        list = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/ul')
        elements = list.find_elements_by_tag_name('li')
        for element in elements:
            print(element.find_element_by_class_name('sbl1').text)
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    case_use_unittest.main()
