import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import cv2
import time


class case_use_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r".\drivers\chromedriver.exe")

    def test_open_cv(self):
        self.driver.get('https://google.com')
        self.driver.save_screenshot('./statics/screenshot.png')
        time.sleep(3)

    def test_img_comapre(self):
        img1 = cv2.imread('./statics/imagen_google_cuadro.png')
        img2 = cv2.imread('./statics/screenshot.png')

        diferencia = cv2.absdiff(img1, img2)
        img_gray_scale = cv2.cvtColor(diferencia, cv2.COLOR_BGR2GRAY)
        contours, _ = cv2.findContours(img_gray_scale, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            if cv2.contourArea(c) >= 20:
                pos_x, pos_y, w, h = cv2.boundingRect(c)
                cv2.rectangle(img1, (pos_x, pos_y), (pos_x + w, pos_y + h), (0, 0, 255), 2)
        while (1):
            cv2.imshow('imagen1 ', img1)
            cv2.imshow('imagen2 ', img2)
            cv2.imshow('Diferencias ', diferencia)
            teclado = cv2.waitKey(5) & 0xFF
            if teclado == 27:
                break
        cv2.destroyAllWindows()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    case_use_unittest.main()
