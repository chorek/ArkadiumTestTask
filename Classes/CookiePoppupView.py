from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainScreen:
    def __init__(self, wait):
        # self.main_window = wait.until(EC.element_to_be_clickable((By.ID,"")))
        self.close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[1]/div[1]")))
    def test(self):
        print("welcome Cookies Popup View Test successful")