

MAX_DEPTH = 4
START_STATE = "-"

s_map = {}

COL_TO_IDX = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}
IDX_TO_COL = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G"}

class GameState:
    def __init__(self, board_pgn):
        self.board_pgn = board_pgn
        self.board = [[""]*7 for _ in range(6)]
        self.setup_board()

    def setup_board(self):
        for move in self.board_pgn.split("-"):
            if move == "":
                continue 

            self.make_move(move)

    def make_move(self, move):
        color = move[0].lower()
        col = COL_TO_IDX[move[1].upper()]
        row = int(move[2]) - 1
        self.board[row][col] = color

    def legal_moves(self, color):
        moves = []
        for col in range(7):
            i = 0
            while (i < 6) and (self.board[i][col] != ""):
                i += 1

            if i < 6:
                moves.append(f"{color.lower()}{IDX_TO_COL[col]}{i+1}")

        return moves  

    def winner(self):
        pass


def solve(board_pgn, last_move=None):
    pass
