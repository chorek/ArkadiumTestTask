from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Classes import Tools

class WelcomeAdvertisementWindow:
    def __init__(self, wait):
        try:
            self.close_button = Tools.button( "Welcome Advertisement > [Close Button]", '')
            self.close_button.obj =  wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/div[1]')))
            print("The " + self.close_button.name + " loaded successfully.")
        except TimeoutException:
            assert False, "The " + self.close_button.name + " has not loaded. Check if the XPath is correct or if the element is present on the page."