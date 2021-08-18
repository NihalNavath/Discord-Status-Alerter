import json
import sys
import traceback

import discord

import config.settings as config

from colorama import Fore

from discord.ext import commands

intents = discord.Intents.default()
intents.presences = True
intents.guilds = True

async def get_prefix(client, message):
    prefixes = config.prefixes

    return commands.when_mentioned_or(*prefixes)(client, message)


bot = commands.Bot(command_prefix=get_prefix, intents=intents, case_insensitive=True)

initial_extensions = [
    "cogs.StatusChecker"
]

if __name__ == "__main__":
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except:
            print(f"Failed to load extension {extension}", file=sys.stderr)
            traceback.print_exc()


@bot.event
async def on_ready():
    """Fired when the bot is ready"""
    print(Fore.GREEN ,f"{'-' * 10}Alerter started!{'-' * 10}\nlogged in as - {bot.user}\nWatching {len(config.ids)} bots! \n{'-' * 36}")

bot.run(config.token)
