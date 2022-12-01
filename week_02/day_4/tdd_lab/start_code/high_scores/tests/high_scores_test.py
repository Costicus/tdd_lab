import unittest

from src.high_scores import latest, personal_best, personal_top_three

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    def setUp(self):
        scores = [1000, 1, 500, 233, 7]
        self.high_scores = HighScoresTest(scores)

    def test_latest_score(self): 
        self.assertEqual (4)

    

    # Tests

    # Test latest score (the last thing in the list)

    # Test personal best (the highest score in the list)

    # Test top three from list of scores

    # Test ordered from highest tp lowest

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
    
# Your task is to write methods that return the 
# 
# highest score from the list, 
# the last added score 
# and the three highest scores. 