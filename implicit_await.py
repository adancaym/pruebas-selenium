import unittest
from selenium import webdriver


class case_use_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"./drivers/chromedriver.exe")

    def test_implicit_await(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get('http://www.google.com')
        my_dinamyc_element = driver.find_element_by_name("q")


if __name__ == '__main__':
    case_use_unittest.main()
