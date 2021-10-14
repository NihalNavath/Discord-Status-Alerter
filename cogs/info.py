from datetime import datetime
from discord.ext import commands

from datetime import datetime

import discord

from utils import bot_utils
import settings as config

class info(commands.Cog):
    """Cog that provides interaction with the bot via commands"""

    def __init__(self, bot):
        self.bot = bot
        self.uptime = datetime.utcnow()

    @commands.command()
    async def info(self , ctx):
        """Shows some information about the bot"""
        alert_channels = bot_utils.mention_channel(config.channelsIds, "\n")
        monitoring_bots = bot_utils.mention_users(config.ids, "\n")

        embed = discord.Embed(title="ℹ️ Information ℹ️")
        embed.add_field(name="Alert channels", value=alert_channels)
        embed.add_field(name="Monitoring bots:-", value=monitoring_bots)

        await ctx.send(embed=embed)

    @commands.command()
    async def uptime(self , ctx):
        """Returns the total uptime of this bot"""
        diff = datetime.utcnow() - self.uptime
        uptime = bot_utils.timedelta_to_humanreadable(diff)

        await ctx.send(f"I have been online for {uptime}")

def setup(bot):
    cog = info(bot)
    bot.add_cog(cog)

    print(f"Extension {cog.qualified_name} is loaded")