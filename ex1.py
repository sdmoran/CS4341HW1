class ConnectFour:

    def __init__(self, board, w, h):
        """Class constructor"""
        # Board data
        self.board = board
        # Board width
        self.w = w
        # Board height
        self.h = h

    def isLineAt(self, x, y, dx, dy):
        """Return True if a line of identical tokens exists starting at (x,y)
           in direction (dx,dy)"""
        # Checks for a line of ANY length (not just 4) exists at target point along direction (dx, dy)
        return self.board[y][x] != 0 and self.board[y][x] == self.board[y - dy][x + dx]
        """^^^has to be minus in order for diagonal up and down calls in
         isAnyLineAt to behave as expected because board is flipped^^^"""

    def isAnyLineAt(self, x, y):
        """Return True if a line of identical symbols exists starting at (x,y)
           in any direction"""
        return (self.isLineAt(x, y, 1, 0) or # Horizontal
                self.isLineAt(x, y, 0, 1) or # Vertical
                self.isLineAt(x, y, 1, 1) or # Diagonal up
                self.isLineAt(x, y, 1, -1)) # Diagonal down

    def getLineLength(self, x, y, dx, dy):
        """Returns the length (assuming min 1, max 4) of the line at target point (x, y) in direction (dx, dy)"""
        length = 1
        for i in range(1, 4):
            totdx = i * dx # Increments dx as loop executes
            totdy = i * dy # Increments dy as loop executes
            # Keeps track of how many identical characters there are in a row
            if self.board[y][x] != 0 and self.board[y][x] == self.board[y - totdy][x + totdx]:
                length += 1
            else:
                return length
        return length

    def getMaxLine(self, x, y):
        """Returns the length of the longest line originating at target point in every direction"""
        return max(self.getLineLength(x, y, 1, 0), # Horizontal
                    self.getLineLength(x, y, 0, 1), # Vertical
                    self.getLineLength(x, y, 1, 1), # Diagonal up
                    self.getLineLength(x, y, 1, -1)) # Diagonal down)

    def getOutcome(self):
        """Returns the winner of the game: 1 for Player 1, 2 for Player 2, and
           0 for no winner"""
        for i in range(0, self.w - 1):
            for j in range(0, self.h - 1):
                if self.isAnyLineAt(i, j): # We only need to check max line length if any line exists
                    if self.getMaxLine(i, j) >= 4: # If a line of length 4 (or more) exists at point, that player wins
                        return self.board[j][i]
        return 0

    def printOutcome(self):
        """Prints the winner of the game"""
        o = self.getOutcome()
        if o == 0:
            print("No winner")
        else:
            print("Player", o, " won")
