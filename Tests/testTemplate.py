import sys
import os
import time
import re
import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Classes import welcomeAdvertisementView, cookiePoppupView, mainScreenView, gameView, Tools


class Test(unittest.TestCase):
    site_address = 'no_site'

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def test_win_the_game(self):
        driver = self.driver

        driver.get(self.site_address)
        actions = ActionChains(driver)
        wait = WebDriverWait(driver, 15)


        
    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()