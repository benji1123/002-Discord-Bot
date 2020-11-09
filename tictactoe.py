GAME_PIECES = {
    'X': '❎',
    'O': '🅾️',
}
EMPTY = '⬜'


class TicTacToe:
    board = None
    symbols = []

    def __init__(self):
        self.board = {
            '↖️': EMPTY, '⬆️': EMPTY, '↗️': EMPTY,
            '⬅️': EMPTY, '⚫': EMPTY, '➡️': EMPTY,
            '↙️': EMPTY, '⬇️': EMPTY, '↘️': EMPTY
        }
        self.symbols = ["X", "O"]

    def make_move(self, symbol, position):
        # validate args
        if position not in self.board.keys():
            ValueError("invalid position")
        if symbol not in self.symbols:
            ValueError("invalid symbol")
        self.board[position] = GAME_PIECES[symbol]

    def board2str(self):
        b = self.board
        top = f"[{b['↖️']}|{b['⬆️']}|{b['↗️']}]"
        middle = f"[{b['⬅️']}|{b['⚫']}|{b['➡️']}]"
        bottom = f"[{b['↙️']}|{b['⬇️']}|{b['↘️']}]"

        board_str = top + '\n' + middle + "\n" + bottom
        return board_str

