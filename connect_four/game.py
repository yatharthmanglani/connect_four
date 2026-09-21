"""The game loop: two players take turns until someone wins or the board fills.

This file does not know *how* a player thinks. It only asks each player
for a move, drops the piece, and checks the result. That is why a random
player and (later) a minimax player can both plug in here.
"""

from connect_four.board import DRAW, PLAYER_O, PLAYER_X, Board


def other_player(player):
    """Flip X to O, or O to X."""
    if player == PLAYER_X:
        return PLAYER_O
    return PLAYER_X


def play_game(player_x, player_o, show=True, start_board=None):
    """Play one game. Return (winner, move_count).

    winner is PLAYER_X, PLAYER_O, or DRAW.
    show=False skips printing, which the benchmark uses so games stay fast.
    start_board lets tests begin from a chosen position instead of empty.
    """
    if start_board is None:
        board = Board()
    else:
        board = start_board

    players = {
        PLAYER_X: player_x,
        PLAYER_O: player_o,
    }
    current = board.whose_turn()
    move_count = 0

    if show:
        print(board.render())
        print()

    while True:
        if board.is_full():
            if show:
                print("The board is full. Draw!")
            return DRAW, move_count

        player = players[current]
        col = player.choose_move(board)
        row = board.drop(col, current)
        move_count += 1

        if show:
            print()
            print(f"{player.name} dropped in column {col + 1}.")
            print(board.render())
            print()

        if board.has_winner_at(row, col):
            if show:
                print(f"{player.name} wins!")
            return current, move_count

        current = other_player(current)
