# bot.py
import os
import random
import discord
from dotenv import load_dotenv

import utils
import asyncio
import tictactoe
import rps

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# CONVERSATION
NAMES = ["002", " 02", "darling", "dino", "dinosaur", "waifu", "zerotwo", "o2", "oxygen", "003"]
NAMES_RESPONSES = os.listdir('zerotwo/')
MEGUMIN_RESPONSES = os.listdir('megumin/')
THINGS_TO_RESPOND_TO = {
    "rpg miniboss": "fight",
    "rpg arena": "join",
    "stfu": "don't be mean, darling!",
    "rpg stfu": "no! 😠",
    "lol": "🤣",
    "lmao": "🤣",
    "haha": "aHHHaahhHAaahA so funny SO FUNNY i'm dyyyyyying 💀",
    "rip": "press 'F' to pay respects",
    "❤️": "listen to the beat, beat, beat",
    "what?": "nani the fuck??",
    "yummy": "i'm hungry",
    "ohh": "THAT MAKES SENSE",
    "congrats": "yaaaaay great job 🥳",
    "!np": "i think... i like this song",
    "rpg buy edgy lootbox": "damn darling! you gotta lotta money",
    "darling": "I think you mean DAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARLING",
    "hmm": "I wonder if...",
    "bro": "yeah?",
    "ily": "ily too"
}

# TICTACTO
TICTACTO_INITIATOR = "!2 tt"
X = ' X '
O = ' O '
EMPTY = '     '
VALID_MOVES = ['tl', 'tc', 'tr', 'cl', 'cc', 'cr', 'bl', 'bc', 'br']
RPS_MOVES = ['🤘', '📝', '✂️']


class ZeroTwoBot(discord.Client):
    async def on_ready(self):
        print(f'{client.user} has connected to Discord!')
        await self.change_presence(activity=discord.Game('outside'))

    async def on_message(self, message):
        if message.author == self.user:
            return
        msg = message.content.lower()
        # respond to name
        if utils.msg_contains(msg, NAMES):
            await utils.send_random_response(message, NAMES_RESPONSES, img_dir="zerotwo/")
        # respond to megumin
        if "megumin" in msg:
            await utils.send_random_response(message, MEGUMIN_RESPONSES, img_dir="megumin/")
        # respond to misc things
        if msg in THINGS_TO_RESPOND_TO.keys():
            await message.channel.send(THINGS_TO_RESPOND_TO[msg])

        # play ROCK PAPER SCISSORS
        if message.content.startswith('!2 rps'):
            channel = message.channel
            game_msg = await channel.send('10 seconds to choose, darling')

            # add reacts to msg
            for move in RPS_MOVES:
                await game_msg.add_reaction(move)
            # await user response
            try:
                reaction, user = await client.wait_for(
                    'reaction_add',
                    timeout=20.0,
                    check=lambda r, u: str(r.emoji) in RPS_MOVES and u == message.author
                )
            except asyncio.TimeoutError:
                await channel.send('too slow darling -_-')
            else:
                res, cpu_choice = rps.simulate_game(user_choice=str(reaction.emoji))
                await channel.send(res + " I chose: " + cpu_choice)


client = ZeroTwoBot()
client.run(TOKEN)
