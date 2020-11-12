import discord
from discord.ext.commands import Bot
from discord.ext import commands
import json
from datetime import datetime
from random import randint
from time import sleep
import asyncio
from itertools import cycle
import discord
from discord.ext import commands
from time import sleep
from discord.ext.commands import has_permissions, CheckFailure
import discord.ext
import os

botIsOnline = True
bot = discord.Client()
bot_prefix = "$"
bot = commands.Bot(command_prefix=bot_prefix)
status = ["Selam ben hyper davet etmek için $davetet komudunu kullanabilirsin!","veya $yardım komutunu kullanarak yardım alabilirsin!"]


token = "null"
with open("token.txt") as file:
    token = file.readline()


@bot.event
async def on_ready():
    bot.remove_command('help')
    print("İsim : {}".format(bot.user.name))
    print("ID : {}".format(bot.user.id))
    bot.loop.create_task(change_status())


async def change_status():
    while True:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Selam ben hyper davet etmek için $davetet komudunu kullanabilirsin!"))
        await asyncio.sleep(3)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="veya $yardım komutunu kullanarak yardım alabilirsin!"))
        await asyncio.sleep(3)
        







@bot.command()
async def logout():
    await bot.logout()



try:
    bot.run(token)
except:
    print("Error while trying to start bot.")

