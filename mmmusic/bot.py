# bot.py
import discord
from discord.ext import commands,tasks
import os
from dotenv import load_dotenv
import youtube_dl

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# client = discord.Client()

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='s!',intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
