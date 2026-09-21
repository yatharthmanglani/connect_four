"""Players choose a column to drop into.

Every player, human or computer, has the same job:

    choose_move(board) -> a legal column number (0-6)

Phase 1 gives you two players: a human who types a column, and a
computer that picks at random. Phase 2 will add a MinimaxPlayer with
the same choose_move method. The game loop does not need to change.
"""

import random

from connect_four.board import COLS


class RandomPlayer:
    """A computer that picks any legal column with equal chance."""

    def __init__(self, name="Computer"):
        self.name = name

    def choose_move(self, board):
        moves = board.legal_moves()
        return random.choice(moves)


class HumanPlayer:
    """A player who types a column number from 1 to 7."""

    def __init__(self, name="You"):
        self.name = name

    def choose_move(self, board):
        legal = board.legal_moves()
        while True:
            raw = input(f"{self.name} (columns 1-7): ").strip()
            if not raw.isdigit():
                print("Please type a whole number from 1 to 7.")
                continue

            # Humans count columns from 1. The board counts from 0.
            col = int(raw) - 1
            if col < 0 or col >= COLS:
                print("That column is off the board. Try 1 to 7.")
                continue
            if col not in legal:
                print("That column is full. Try another one.")
                continue
            return col
