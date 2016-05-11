from shylux_bot import Bot
import random


class JoshBot(Bot):
    opponent_id = -1

    def make_turn(self):
        self.opponent_id = 1 if self.id() == 2 else 2

        self.place_disc(self.find_best_move())

    def find_best_move(self):
        # Always go for the middle on the first turn
        if self.round == 0:
            return 5

        # Search for own winning move
        move = self.find_winning_moves(self.id())

        if move:
            return move

        # Search for opponent's winning move
        move = self.find_winning_moves(self.opponent_id)

        if move:
            return move

        # Pick randomly otherwise
        return random.randrange(7)

    def find_winning_moves(self, player):
        moves = []

        for x in xrange(self.rows()):
            for y in xrange(self.cols()):
                move = self.check_line(player, x, y, 1, 0)
                if move: return move

                move = self.check_line(player, x, y, 0, 1)
                if move: return move

                move = self.check_line(player, x, y, 1, 1)
                if move: return move

                move = self.check_line(player, x, y, -1, 0)
                if move: return move

                move = self.check_line(player, x, y, 0, -1)
                if move: return move

                move = self.check_line(player, x, y, -1, -1)
                if move: return move


    def check_line(self, player, x, y, x_skip, y_skip):
        for l in xrange(5):
            check_x = x + (x_skip * l)
            check_y = y + (x_skip * l)

            try:
                # 4 in a row, winning move here maybe
                if l == 4:
                    if self.board[check_x][check_y] == 0:
                        return (check_x, check_y)

            if self.board[check_x][check_y] != player:
                return
            except IndexError as ex:
                return
