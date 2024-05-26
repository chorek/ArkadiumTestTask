from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
import time
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Classes import Tools

class GameWindow:
    def __init__(self, wait):
        self.menu = self.Menu()
        self.top_game_bar = self.TopGameBar()
        self.clues = self.Clues()
        self.end_game_window = self.EndGameWindow()
        self.hamburger_button = Tools.button("Game > [Hamburger Menu Button]","")
        self.load_hamburger_button(wait)


    def load_hamburger_button(self, wait):
        try:
            self.hamburger_button.obj = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gameContainer"]/article/section/section/section[1]/button[1]')))
            print("The " + self.hamburger_button.name + " loaded successfully.")
        except TimeoutException:
            assert False, "The " + self.hamburger_button.name + " cannot be loaded. Check if the XPath is correct or if the element is present on the page."

    class Clues:
        def __init__(self):
            self.clue_buttons = Tools.button("Game > Clue Buttons","")
            print("Clues Initilization success!")

        def load(self, driver):
            self.clue_buttons.obj = driver.find_elements(By.CSS_SELECTOR,'._3XPL5R2-eusgcizD-KOU2r.connectedCluePanel_clueContainer__sHUi6')
            assert self.clue_buttons, "Loading clues failed! No clues found on the page. Check if the CSS selector is correct or if the page layout has changed."
            print("Clues loaded successfully.")

    def finish_puzzle(self, clue_change_method, answers_inst, actions):
        print("Solving puzzle. Answers entering started.")
        self.clues.clue_buttons.obj[0].click()
        for clue in self.clues.clue_buttons.obj:
            if clue_change_method == "click":
                clue.click()
                time.sleep(1)

            tekst =  re.sub(r'^\d+', '', clue.text)
            tekst = re.sub('[^A-Za-z ()0-9,."";-]+', '', tekst).strip()

            if tekst in answers_inst.dictionary:
                actions.send_keys(answers_inst.dictionary[tekst]).perform()
            else:
                assert False, "Answers not matching choosed day!"
            if clue_change_method == "enter":
                actions.send_keys(Keys.ENTER)
                time.sleep(0.4)
        print("Answers entering finished.")

    class TopGameBar:
        def __init__(self):
            self.bar =  Tools.object("Game > [Top Bar]","")

        def load(self, wait):
            try:
                self.bar.obj = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="gameContainer"]/article/section/section/section[2]/section[2]/section[1]/ul/li[1]')))
                print("The " + self.bar.name + " loaded successfully.")
            except TimeoutException:
                assert False, "The " + self.bar.name + " cannot be loaded. Check if the XPath is correct or if the element is present on the page."

    class Menu:
        def __init__(self):
            self.puzzle_info_button = Tools.button("Hamburger Menu > [Puzzle Info Button]","")
            self.close_button = Tools.button("Hamburger Menu > > [Close Menu Button]","")
            self.skip_over_filled_squares_button = Tools.button("Hamburger Menu > > [Skip Over Filled Squares Button]","")
            self.puzzle_pupup = self.PuzzlePopUp()

        def load(self, wait):
            try:
                self.puzzle_info_button.obj = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gameContainer"]/article/section/section/section[3]/article/button[3]')))
                print("The " + self.puzzle_info_button.name + " loaded successfully.")
            except TimeoutException:
                assert False, "The " + self.puzzle_info_button.name + " has not loaded. Check if the XPath is correct or if the element is present on the page."

            try:
                self.close_button.obj = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '_1nGHHNch1WYjKm6o-mNMNs')))
                print("The " + self.close_button.name + " loaded successfully.")
            except TimeoutException:
                assert False, "The " + self.close_button.name + " has not loaded. Check if the CLASS NAME is correct or if the element is present on the page."

            try:
                self.skip_over_filled_squares_button.obj = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gameContainer"]/article/section/section/section[3]/article/label[3]/span')))
                print("The " + self.skip_over_filled_squares_button.name + " loaded successfully.")
            except TimeoutException:
                assert False, "The " + self.skip_over_filled_squares_button.name + " has not loaded. Check if the XPath is correct or if the element is present on the page."

        class PuzzlePopUp:
            def __init__(self):
                self.close_button = Tools.button("Puzzle Pop-up > [Close Button]","")
                self.header = Tools.object("Puzzle Pop-up > [Header]","")

            def load(self, wait):
                try:
                    self.close_button.obj = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '_1-15SEKlxr-2aGzogZRMjr')))
                    print("The " + self.close_button.name + " loaded successfully.")
                except TimeoutException:
                    assert False, "The " + self.close_button.name + " has not loaded. Check if the CLASS NAME is correct or if the element is present on the page."
                try:
                    self.header.obj = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="gameContainer"]/article/section/section/section[2]/div/article/section/section/div/h3')))
                    print("The " + self.header.name + " loaded successfully.")
                except TimeoutException:
                    assert False, "The " + self.header.name + " has not loaded. Check if the XPath is correct or if the element is present on the page."

    class EndGameWindow:
        def __init__(self):
            self.result =  Tools.object("Game >  [END GAME Window]","")

        def load(self, wait):
            try:
                self.result.obj = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, '_1WOLqIpDmSmsJGpFvS9fPR')))
                print("The " + self.result.name + " loaded successfully.")
            except TimeoutException:
                assert False, "The " + self.result.name + " has not loaded. Check if the CLASS NAME is correct or if the element is present on the page."
