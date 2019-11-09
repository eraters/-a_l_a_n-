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
  await client.change_presence(status=discord.Status.Online, activity=discord.Game("~A_L_A_N~'S Discord bot (coded by ImLazyWithAZ#8327 "))

@client.command()
async def start(ctx):
  await ctx.send('This bot has been started')

@client.command()
async def hi(ctx):
  await ctx.send(f'Hello {ctx.author}!')
  
client.run(os.getenv('TOKEN'))
