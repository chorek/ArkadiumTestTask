import sys
import os
import time
import re
import unittest
import inspect

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Classes import welcomeAdvertisementView, cookiePoppupView, mainScreenView, gameView, Tools


class Test(unittest.TestCase):
    answers_date = 'no_module'
    text_to_check_date = 'no_text'
    clue_change_method = 'enter'
    site_address = 'no_site'

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        print("TEST PARAMETERS: QUIZ DATE - " + self.answers_date + "  |  CLUE CHANGE METHOD - " + self.clue_change_method)

    def test_win_the_game(self):
        driver = self.driver
        driver.get(self.site_address)
        actions = ActionChains(driver)
        wait = WebDriverWait(driver, 15)

        classes_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Answers'))
        dynamic_importer = Tools.DynamicImporter(classes_directory)
        dynamic_importer.import_modules()
        try:
            AnswersTable = dynamic_importer.get_class("answers" + self.answers_date, "Table")
            print(f"Successfully imported Table with answers from {self.answers_date}")
        except ImportError as e:
            print(e)


        cookiePoppup_inst = cookiePoppupView.CookiePoppupWindow(wait)
        cookiePoppup_inst.agree_button.ATclick()

        welcomeAdvertisement_inst = welcomeAdvertisementView.WelcomeAdvertisementWindow(wait)
        time.sleep(5)

        welcomeAdvertisement_inst.close_button.ATclick()

        mainScreen_inst = mainScreenView.MainScreenWindow(wait, driver)
        mainScreen_inst.day_tiles[int(self.answers_date[:2])-1].click()

        game_inst = gameView.GameWindow(wait)
        game_inst.hamburger_button.ATclick()

        game_inst.menu.load(wait)
        Tools.scroll_to_element(game_inst.menu.skip_over_filled_squares_button, driver)
        game_inst.menu.skip_over_filled_squares_button.ATclick()

        Tools.scroll_to_element(game_inst.menu.puzzle_info_button, driver)
        game_inst.menu.puzzle_info_button.ATclick()

        game_inst.menu.puzzle_pupup.load(wait)
        assert game_inst.menu.puzzle_pupup.header.obj.text == self.text_to_check_date, "Puzzle Date not matching!"
        print("Puzzle date is correct and matching: " + game_inst.menu.puzzle_pupup.header.obj.text)

        Tools.scroll_to_element(game_inst.menu.puzzle_pupup.close_button, driver)
        game_inst.menu.puzzle_pupup.close_button.ATclick()

        game_inst.top_game_bar.load(wait)
        Tools.scroll_to_element(game_inst.hamburger_button, driver)

        game_inst.clues.load(driver)

        answers_inst = AnswersTable(wait)
        answers_inst.load()

        game_inst.finish_puzzle(self.clue_change_method, answers_inst, actions)
        game_inst.end_game_window.load(wait)
        
    def tearDown(self):
        Tools.take_screenshot("TestWinTheGame", "test_win_the_game_" + self.answers_date +"__" + self.clue_change_method, self.driver)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

