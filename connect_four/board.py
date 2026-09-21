"""The Connect Four board and the Game rules.

  1. How is the board stored in memory?
  2. Which columns can a player drop a piece into?
  3. What happens when a piece is dropped?
  4. Did that drop win the game, or fill the board?

"""

ROWS = 6
COLS = 7
WIN_LENGTH = 4

EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2
DRAW = 0

# Representation of each player on the board.
SYMBOLS = {
    EMPTY: ".",
    PLAYER_X: "X",
    PLAYER_O: "O",
}

class Board:
    """A 6x7 Connect Four grid.

    Row 0 - TOP of the board, Row 5 - BOTTOM of the board
    Each cell can hold EMPTY (0), PLAYER_X (1), or PLAYER_O (2).
    """

    def __init__(self):
        # A list of 6 rows, each row a list of 7 cells.
        self.grid = []
        for _ in range(ROWS):
            row = []
            for _ in range(COLS):
                row.append(EMPTY)
            self.grid.append(row)

    def copy(self):
        """Return a new board with the same pieces.

        Phase 2's minimax will copy the board, try a move, then throw
        the copy away. The real game board stays untouched.
        """
        clone = Board()
        clone.grid = []
        for row in self.grid:
            clone.grid.append(row[:])  # copy the row
        return clone

    def legal_moves(self):
        """Return the list of columns (0-6) that still have space.

        A column is legal if its TOP cell is still empty. 
        """
        moves = []
        for col in range(COLS):
            if self.grid[0][col] == EMPTY:
                moves.append(col)
        return moves

    def is_full(self):
        """Return True when no column has room left.
        """
        return len(self.legal_moves()) == 0

    def piece_count(self, player):
        """Return the number of cells held by this player.
        """
        count = 0
        for row in self.grid:
            for cell in row:
                if cell == player:
                    count += 1
        return count

    def whose_turn(self):
        """Return which player's turn it is. First move is by X, then O.
        """
        if self.piece_count(PLAYER_X) == self.piece_count(PLAYER_O):
            return PLAYER_X
        return PLAYER_O

    def drop(self, col, player):
        """Drop `player`'s piece into `col`. Return the row it landed in.
        """
        if col < 0 or col >= COLS:
            raise ValueError(f"Column {col} is off the board")

        # Start at the bottom row and walk up until we find an empty cell.
        for row in range(ROWS - 1, -1, -1):
            if self.grid[row][col] == EMPTY:
                self.grid[row][col] = player
                return row

        raise ValueError(f"Column {col} is full")

    def has_winner_at(self, row, col):
        """Return True if the piece at (row, col) completes four in a row.
        Only look around the piece that just landed.
        """
        player = self.grid[row][col]
        if player == EMPTY:
            return False

        # Four directions. Each is checked both ways (forward and back).
        # direction = (d_row, d_col), whether row changes or column changes in a step.
        directions = [
            (0, 1),   # horizontal
            (1, 0),   # vertical
            (1, 1),   # diagonal
            (1, -1),  # diagonal
        ]
        for d_row, d_col in directions:
            total = 1
            total += self._count_in_direction(row, col, d_row, d_col, player)
            total += self._count_in_direction(row, col, -d_row, -d_col, player)
            if total >= WIN_LENGTH:
                return True
        return False

    def _count_in_direction(self, row, col, d_row, d_col, player):
        """Return the number of same-player pieces starting one step from (row, col) 
        in that direction.
        """
        count = 0
        r = row + d_row
        c = col + d_col
        while 0 <= r < ROWS and 0 <= c < COLS and self.grid[r][c] == player:
            count += 1
            r += d_row
            c += d_col
        return count

    def render(self):
        """Return a printable view of the board as a string.
        """
        lines = []
        lines.append("  1 2 3 4 5 6 7")
        lines.append("  -------------")
        for row in self.grid:
            cells = []
            for cell in row:
                cells.append(SYMBOLS[cell])
            lines.append("| " + " ".join(cells) + " |")
        lines.append("  -------------")
        return "\n".join(lines)
