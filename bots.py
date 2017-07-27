import discord
import asyncio
import discord
from discord.ext import commands
import sys
import os


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)
bot = commands.Bot(command_prefix='?', description="Bot fait par l'équipe Qode")


@bot.event
async def on_message(message):
    await bot.process_commands(message)

@bot.command(pass_context=True)
async def rank(ctx, member: discord.Member = None):
    """Savoir le rang d\'un utilisateur. """
    if member is None:
        commander_name = ctx.message.author
        embed=discord.Embed(title="Grade de %s"%(commander_name), color=0x0080c0)
        embed.add_field(name=" - Développeur confirmé : ", value=" x", inline=True)
        embed.add_field(name=" - Développeur débutant : ", value=" x", inline=False)
        await bot.say(embed=embed)
    else:
        mb_role = discord.Object(id=member.id).roles
        embed=discord.Embed(title="Grade de %s"%(member), color=0x0080c0)
        embed.add_field(name=" - Développeur confirmé : ", value=" x", inline=True)
        embed.add_field(name=" - Développeur débutant : ", value=" x", inline=False)
        embed.add_field(name=" - Roles : ", value=" {0}".format(mb_role), inline=False)
        await bot.say(embed=embed)


@bot.command()
async def restart():
    await bot.say("Je m\'éteins")
    restart_program()

bot.run('')
