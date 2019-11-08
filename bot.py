import discord
from discord.ext import commands

TOKEN = os.environ.get("TOKEN")

client = commands.Bot(command_prefix = 'a!')

@client.event
async def on_ready():
  print('Bot is ready')

client.run(TOKEN)
