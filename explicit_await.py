import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec


class case_use_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r".\drivers\chromedriver.exe")

    def test_search_in_tabs(self):
        driver = self.driver
        driver.get('http://www.google.com')
        try:
            element = WebDriverWait(driver, 10).until(
                Ec.presence_of_element_located((By.NAME, "q"))
            )
        finally:
            driver.quit()


if __name__ == '__main__':
    case_use_unittest.main()
