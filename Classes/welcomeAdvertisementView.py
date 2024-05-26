from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainScreen:
    def __init__(self, wait):
        self.main_window = wait.until(EC.element_to_be_clickable((By.ID, "qc-cmp2-container")))
        self.agree_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/button[3]")))
    def test(self):
        print("welcome Advertisement View Test successful")