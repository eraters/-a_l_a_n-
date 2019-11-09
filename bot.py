import discord
import os
import asyncio
import random
from discord.ext import commands, tasks
from discord.ext.commands import when_mentioned_or
from itertools import cycle

client = commands.Bot(command_prefix = 'a!')

@client.event
async def on_ready():
  print('Bot is ready')
  
@client.command()
async def start(ctx):
  ctx.send('This bot has been staerted')

client.run(os.getenv('TOKEN'))
