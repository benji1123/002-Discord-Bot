import random
import os
import discord

IMAGE_FILE_EXTENSIONS = [".jpg", ".png", ".gif"]
IMAGE_DIR = "zerotwo/"


def msg_contains(msg, triggers):
    return any(t in msg for t in triggers)


async def send_random(message, responses, img_dir=""):
    response = random.choice(responses)
    img_name = img_dir + response
    if is_image(img_name):
        await message.channel.send(file=discord.File(img_name))
    else:
        await message.channel.send("dats me")
    return


def is_image(path):
    return path[-4:].lower() in IMAGE_FILE_EXTENSIONS \
           and os.path.exists(path) and "DS_Store" not in path


def get_eqn_and_ans(msg):
    """Parse str-equation and return answer"""
    msg = msg.split("!2 math")
    if len(msg) == 2:
        eqn = msg[1]
        ans = eval(eqn)
        return eqn, ans
    ValueError("bad message for !2 math")