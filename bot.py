import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = 'a!')

@client.event
async def on_ready():
  print('Bot is ready')
  
@client.command()
async def start(ctx):
  ctx.send('This bot has been staerted')

client.run(os.getenv('TOKEN'))
