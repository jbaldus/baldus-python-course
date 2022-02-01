import unittest

from task import season_episode
import task

seasons = [0, 32, 21, 18, 17, 24, 31, 8, 24, 21, 26]

class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertListEqual(task.seasons, seasons, msg=f"Use {seasons} for seasons.")
        self.assertEqual(season_episode(42, seasons), (2, 10), msg="Episode 42 is Season 2, Episode 10")
        self.assertEqual(season_episode(66, seasons), (3, 13), msg="Episode 66 is Season 3, Episode 13")
        self.assertEqual(season_episode(182, seasons), (9, 7), msg="Episode 182 is Season 9, Episode 7")
        self.assertEqual(season_episode(26, seasons), (1, 26), msg="Episode 26 is Season 1, Episode 26")
        self.assertEqual(season_episode(482, seasons), (10, 260), msg="Episode 482 is Season 10, Episode 260")

