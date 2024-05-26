from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Classes import Tools

class CookiePoppupWindow:
    def __init__(self, wait):
        try:
            self.main_window = Tools.object("Cookies Pop-up > [Main Window]","")
            self.main_window.obj = wait.until(EC.element_to_be_clickable((By.ID, "qc-cmp2-container")))
            print("The " + self.main_window.name + " loaded successfully.")
        except TimeoutException:
            assert False, "The " + self.main_window.name + " has not loaded. Check if the ID is correct or if the element is present on the page."

        try:
            self.agree_button = Tools.button( "Cookies Pop-up > Main Window > [Agree Button]", wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/button[3]"))) )
            print("The " + self.agree_button.name + " loaded successfully.")
        except TimeoutException:
            assert False, "The " + self.agree_button.name + " has not loaded. Check if the XPath is correct or if the element is present on the page."

