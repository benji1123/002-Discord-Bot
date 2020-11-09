import os
import discord
from dotenv import load_dotenv

# functionality
import tictactoe
import rps
import conversation

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


class ZeroTwoBot(discord.Client):
    async def on_ready(self):
        print(f'{client.user} has connected to Discord!')
        await self.change_presence(activity=discord.Game('outside'))

    async def on_message(self, message):
        if message.author == self.user:
            return
        msg_content = message.content.lower()

        # if someone says something we care about
        await conversation.respond_to_name(message, msg_content)
        await conversation.respond_to_certain_things(message, msg_content)
        await conversation.respond_to_math(message, msg_content)
        await conversation.respond_to_google(message, msg_content)

        # if someone wants to play a game
        await rps.play_rps(client, message, msg_content)
        await tictactoe.play_ttt(client, message, msg_content)


client = ZeroTwoBot()
client.run(TOKEN)
