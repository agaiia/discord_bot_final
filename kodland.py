import discord
from discord.ext import commands

#$sarikutu

import random

from cod import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')


@bot.command()
async def mem(ctx):
    await ctx.send(memer1())

#$sarikutu

bot.run('TOKENİ BURAYA YAZ')
