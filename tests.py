import unittest
import numpy
from joshbot import JoshBot

class TestBot(unittest.TestCase):
    def setUp(self):
        self.bot = JoshBot()
        self.bot.settings['field_rows'] = 6
        self.bot.settings['field_columns'] = 7
        self.bot.settings['your_botid'] = 1

    def test_find_player_win_right(self):
        self.bot.board = numpy.array([
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [1,1,1,0,0,0,0]
        ])

        move = self.bot.find_winning_moves(self.bot.settings['your_botid'])
        self.assertEqual(move, 3)

    def test_find_player_win_left(self):
        self.bot.board = numpy.array([
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,1,1,1]
        ])

        move = self.bot.find_winning_moves(self.bot.settings['your_botid'])
        self.assertEqual(move, 3)

    def test_find_player_win_top(self):
        self.bot.board = numpy.array([
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,1,0,0,0],
          [0,0,0,1,0,0,0],
          [0,0,0,1,0,0,0]
        ])

        move = self.bot.find_winning_moves(self.bot.settings['your_botid'])
        self.assertEqual(move, 3)

    def test_find_player_win_first_col(self):
        self.bot = JoshBot()
        self.bot.board = numpy.array([
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,1,1,1,2,0,0]
        ])

        move = self.bot.find_winning_moves(self.bot.settings['your_botid'])
        self.assertEqual(move, 0)

if __name__ == '__main__':
    unittest.main()
