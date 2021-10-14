import sys
import traceback

import discord

from discord.ext import commands

import settings as config

intents = discord.Intents.default()
intents.members = True
intents.presences = True

async def get_prefix(client, message):
    prefixes = config.prefixes

    return commands.when_mentioned_or(*prefixes)(client, message)


bot = commands.Bot(command_prefix=get_prefix, intents=intents, case_insensitive=True)

extensions = [
    "cogs.statuschecker",
    "cogs.info"
]

for extension in extensions:
    try:
        bot.load_extension(extension)
    except Exception as e:
        print(f"Failed to load extension {extension}", file=sys.stderr)
        traceback.print_exc()


@bot.event
async def on_ready():
    print(f"{'-' * 10}Alerter started!{'-' * 10}\nlogged in as - {bot.user}\nWatching {len(config.ids)} bots! \n{'-' * 36}")

if __name__ == "__main__":
    bot.run(config.token)
