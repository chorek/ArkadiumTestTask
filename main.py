from Tests import testWinTheGame
import unittest

test_parameters = [
    ("21_05_2024", "Daily Quick Crossword: 21 May 2024", "enter"),
    ("21_05_2024", "Daily Quick Crossword: 21 May 2024", "click"),
    ("04_05_2024", "Daily Quick Crossword: 4 May 2024", "enter"),
    ("04_05_2024", "Daily Quick Crossword: 4 May 2024", "click")
]

suite = unittest.TestSuite()
testWinTheGame.Test.site_address = "https://www.gamelab.com/games/daily-quick-crossword"

for answers_date, text_to_check_date, clue_change_method in test_parameters:
    test_case = testWinTheGame.Test('test_win_the_game')
    test_case.answers_date = answers_date
    test_case.text_to_check_date = text_to_check_date
    test_case.clue_change_method = clue_change_method
    suite.addTest(test_case)

unittest.TextTestRunner(verbosity=2).run(suite)
