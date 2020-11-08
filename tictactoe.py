X = ' X '
O = ' O '
EMPTY = '     '


class TicTacToe:
    board = None
    symbols = []
    player = None

    def __init__(self, player):
        self.board = {
            'tl': X, 'tc': EMPTY, 'tr': EMPTY,
            'cl': EMPTY, 'cc': EMPTY, 'cr': O,
            'bl': EMPTY, 'bc': EMPTY, 'br': EMPTY
        }
        self.symbols = ["X", "O"]

    def make_move(self, symbol, position):
        # validate args
        if position not in self.board.keys():
            ValueError("invalid position")
        if symbol not in self.symbols:
            ValueError("invalid symbol")
        self.board[position] = symbol

    @staticmethod
    def board2str(b):
        top = f"[{b['tl']}|{b['tc']}|{b['tr']}]"
        middle = f"[{b['cl']}|{b['cc']}|{b['cr']}]"
        bottom = f"[{b['bl']}|{b['bc']}|{b['br']}]"
        board_str = top + '\n' + middle + "\n" + bottom
        return board_str

