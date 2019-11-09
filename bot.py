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
  await ctx.send('This bot has been started')

@client.command()
async def hi(ctx):
  await ctx.send(f'Hello {ctx.author}!')
  
@client.command()
async def presence(ctx, *, status):
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(status))
    await ctx.send("Status Changed!")
  
client.run(os.getenv('TOKEN'))
