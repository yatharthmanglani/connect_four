"""Play Connect Four: human (X) against a computer that chooses random moves.

"""

from connect_four.game import play_game
from connect_four.players import HumanPlayer, RandomPlayer


def main():
    print("Connect Four - Phase 1")
    print("You are X. The computer is O and picks a random legal column.")
    print("Type a column number from 1 to 7, then press Enter.")
    print()

    you = HumanPlayer(name="You")
    computer = RandomPlayer(name="Computer")
    play_game(you, computer, show=True)


if __name__ == "__main__":
    main()
