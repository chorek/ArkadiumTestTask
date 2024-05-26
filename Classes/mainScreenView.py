from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MainScreenWindow:
    def __init__(self, wait, driver):
        self.load_game(wait)
        self.day_tiles = ''
        self.day_tiles_init(wait, driver)

    def load_game(self, wait):
        try:
            wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "#game-canvas > iframe")))
            print("GAME 1/3 loading. Please wait...")
        except TimeoutException:
            assert False, "The GAME HAS NOT LOADED loaded. Check if the CSS Selector is correct or if the element is present on the page."

        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gameContainer"]/article/section/section/section/ul/li[23]/div[2]')))
            print("GAME 2/3 loading. Please wait...")
        except TimeoutException:
            assert False, "The GAME has not loaded. Check if the XPath is correct or if the element is present on the page."

        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gameContainer"]/article/section/section/section/ul')))
            print("GAME 3/3 loading. Please wait...")
        except TimeoutException:
            assert False, "The GAME has not loaded. Check if the XPath is correct or if the element is present on the page."

    def day_tiles_init(self, wait, driver):
        self.day_tiles = driver.find_elements(By.CLASS_NAME, "gameStart_wrapper__3lViH")
        assert self.day_tiles, "Loading DAY tiles failed! No game to play on the page. Check if the CLASS NAME is correct or if the page layout has changed."

        print("Day tiles loaded successfully.")
        return self.day_tiles