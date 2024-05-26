import sys
import os
import time
import re
import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from PIL import Image

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Classes import welcomeAdvertisementView, cookiePoppupView, mainScreenView, gameView
from Answers import answers

# driver = webdriver.Chrome()


class TestWinTheGame(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def test_win_the_game(self):
        driver = self.driver

        driver.get('https://www.gamelab.com/games/daily-quick-crossword')
        actions = ActionChains(driver)

        wait = WebDriverWait(driver, 15)


        cookiePoppupView_ints = cookiePoppupView.MainScreen(wait)
        cookiePoppupView_ints.agree_button.click()

        welcomeAdvertisementView_ints = welcomeAdvertisementView.MainScreen(wait)
        time.sleep(5)

        welcomeAdvertisementView_ints.close_button.click()

        mainScreenView_ints = mainScreenView.MainScreen(wait, driver)
        mainScreenView_ints.day_tiles[20].click()

        gameView_ints = gameView.MainScreen(wait)
        gameView_ints.hamburger_button.click()

        gameView_ints.menu.load(wait)
        gameView_ints.scroll_to_element(gameView_ints.menu.skip_pver_filled_squares_button, driver)
        gameView_ints.menu.skip_pver_filled_squares_button.click()

        gameView_ints.scroll_to_element(gameView_ints.menu.puzzle_info_button, driver)
        gameView_ints.menu.puzzle_info_button.click()

        gameView_ints.menu.puzzle_pupup.load(wait)
        assert gameView_ints.menu.puzzle_pupup.header.text == "Daily Quick Crossword: 21 May 2024"

        gameView_ints.scroll_to_element(gameView_ints.menu.puzzle_pupup.close_button, driver)
        gameView_ints.menu.puzzle_pupup.close_button.click()

        gameView_ints.top_game_bar.load(wait)
        gameView_ints.scroll_to_element(gameView_ints.hamburger_button, driver)

        gameView_ints.clues.load(driver)

        answers_ints = answers.Table(wait)
        answers_ints.load()


        gameView_ints.clues.clue_buttons[0].click()
        for clue in gameView_ints.clues.clue_buttons:
            tekst = re.sub('[^A-Za-z ]+', '', clue.text).strip()
            if tekst in answers_ints.dictionary:
                actions.send_keys(answers_ints.dictionary[tekst]).perform()
            actions.send_keys(Keys.ENTER)
            time.sleep(0.05)

        gameView_ints.end_game_window.load(wait)

        driver.save_screenshot('test_win_the_game.png')

    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()
# menu_puzzle_pupup_close_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '_1-15SEKlxr-2aGzogZRMjr')))
# print(driver.find_element(By.XPATH, '//*[@id="gameContainer"]/article/section/section/section[2]/div/article/section/section/div/h3').text)

# menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gameContainer"]/article/section/section/section[1]/button[1]')))
# menu_button.click()
#
# menu_puzzle_info_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gameContainer"]/article/section/section/section[3]/article/button[3]')))
# # menu_puzzle_info_button.click()
# js_code = "arguments[0].scrollIntoView();"
# driver.execute_script(js_code, menu_puzzle_info_button)
#
#
# menu_puzzle_info_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gameContainer"]/article/section/section/section[3]/article/button[3]')))
# menu_puzzle_info_button.click()
#
# # assert 0 == 1, "My custom message test"
# menu_puzzle_pupup_close_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '_1-15SEKlxr-2aGzogZRMjr')))
# print(driver.find_element(By.XPATH, '//*[@id="gameContainer"]/article/section/section/section[2]/div/article/section/section/div/h3').text)
#
# # menu_puzzle_pupup_close_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '_1-15SEKlxr-2aGzogZRMjr')))
# driver.execute_script(js_code, menu_puzzle_pupup_close_button)
# menu_puzzle_pupup_close_button.click()
# #
# # menu_close_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '_1nGHHNch1WYjKm6o-mNMNs')))
# # # time.sleep(1)
# # menu_close_button.click()
#
#
#
#
# element_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gameContainer"]/article/section/section/section[2]/section[2]/section[1]/ul/li[1]')))
# driver.execute_script(js_code, element_button)
# clue_buttons = driver.find_elements(By.CLASS_NAME, 'connectedCluePanel_clueNum3Digits__2SmdZ')
# clue_buttons[3].click()
#
#
#
#
# actions.send_keys("cascade").perform()
#
#
#
# check_menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gameContainer"]/article/section/section/section[1]/button[2]')))
# driver.execute_script(js_code, check_menu_button)
# check_menu_button.click()
#
#
# check_puzzle_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gameContainer"]/article/section/section/section[1]/button[2]/ul/li[3]')))
# # driver.execute_script(js_code, check_puzzle_button)
# check_puzzle_button.click()
#
# driver.save_screenshot('ss.png')
# screenshot = Image.open('ss.png')
# screenshot.show()
#
# # actions.send_keys(Keys.CONTROL,'m').perform()
# # driver.quit()
