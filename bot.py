import rps
import conversation
import TicTacToeHandler

import discord
import redis

redis_server = redis.Redis()
AUTH_TOKEN = str(redis_server.get('AUTH_TOKEN').decode('utf-8'))

TICTACTOE_PROMPT = "!2 tt"


class ZeroTwoBot(discord.Client):
    async def on_ready(self):
        print(f'{client.user} has connected to Discord!')
        await self.change_presence(activity=discord.Game('xylophone'))

    async def on_message(self, message):
        if message.author == self.user:
            return
        msg_content = message.content.lower()

        # if someone says something we care about
        await conversation.respond_to_name(message, msg_content)
        await conversation.respond_to_certain_things(message, msg_content)
        await conversation.respond_to_math(message, msg_content)
        await conversation.respond_to_google(message, msg_content)

        # user wants to play Rock Paper Scissors
        await rps.play_rps(client, message, msg_content)
        # a user has requested a TicTacToe game
        if message.content.startswith(TICTACTOE_PROMPT):
            await TicTacToeHandler.start_game(client, message.channel, message.author)


client = ZeroTwoBot()
client.run(AUTH_TOKEN)
