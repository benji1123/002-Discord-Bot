import asyncio
import discord
import random
import time

GAME_PIECES = {
    'X': '❎',
    'O': '🅾️',
}
EMPTY = '⬜'
X = ' X '
O = ' O '
EMPTY = '     '
VALID_MOVES = ['tl', 'tc', 'tr', 'cl', 'cc', 'cr', 'bl', 'bc', 'br']
TTT_MOVES = ['↖️', '⬆️', '↗️', '⬅️', '⚫', '➡️', '↙️', '⬇️', '↘️']
MAX_MOVES = 3


async def play_ttt(client, message, msg_content):
    if message.content.startswith('!2 tt'):
        game = TicTacToe()
        # send board as msg_content
        game_msg = await message.channel.send('ttt\n' + game.board2str())
        # add reacts to msg_content
        for move in TTT_MOVES:
            await game_msg.add_reaction(move)
        # await user response
        await wait_for_player(client, game, message, game_msg)


# abstract below to tictactoe.py
async def wait_for_player(client, game, message, game_msg):
    try:
        reaction, user = await client.wait_for(
            'reaction_add',
            timeout=40.0,
            check=lambda r, u: str(r.emoji) in TTT_MOVES and u == message.author
        )
    except asyncio.TimeoutError:
        await message.channel.send('too slow darling -_-')
    else:
        if game.is_over():
            await message.channel.send('game over')
        else:
            user_choice = str(reaction.emoji)
            await update_ttt_board(client, game, user_choice, message, game_msg)


async def update_ttt_board(client, game, user_choice, message, game_msg):
    game.make_move('O', user_choice)
    await game_msg.edit(content='ttt\n' + game.board2str())
    time.sleep(1)
    game.cpu_make_move('X')
    await game_msg.edit(content='ttt\n' + game.board2str())
    await wait_for_player(client, game, message, game_msg)


class TicTacToe:
    board = None
    moves = 0
    game_over = False

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
        self.moves += 1
        if self.moves >= 3:
            self.game_over = True
            return

    def cpu_make_move(self, symbol="X"):
        position = random.choice(list(self.board))
        while self.board[position] != EMPTY and not self.game_over:
            position = random.choice(list(self.board))
        self.make_move(symbol, position)

    def board2str(self):
        b = self.board
        top = f"[{b['↖️']}|{b['⬆️']}|{b['↗️']}]"
        middle = f"[{b['⬅️']}|{b['⚫']}|{b['➡️']}]"
        bottom = f"[{b['↙️']}|{b['⬇️']}|{b['↘️']}]"

        board_str = top + '\n' + middle + "\n" + bottom
        return board_str

    def is_over(self):
        return self.game_over


