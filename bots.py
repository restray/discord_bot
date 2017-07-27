import discord
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix='?', description="Bot fait par l'équipe Qode")

@bot.event
async def on_message(message):
    # do some extra stuff here

    await bot.process_commands(message)

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

bot.run('')
