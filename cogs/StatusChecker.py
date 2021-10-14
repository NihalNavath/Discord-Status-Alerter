import datetime

import discord
from discord.ext import commands

from utils import errors, bot_utils
import settings as config

class Statuschecker(commands.Cog):
    """The main cog that handles status checking."""
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = config.embed_color

        self.offline = {}

    async def alert(self, member_info, offline: bool):
        """Main function that handles alerting the owner(s), sends a message in all the 
        channels specified under "channels" array in settings.py"""
        if offline:
            down_time = datetime.datetime.now()
            self.offline[member_info.id] = down_time
                    
            title = f"{member_info} is now **DOWN**"
            description = f"time noticed:- {discord.utils.format_dt(down_time, style='F')}"  
            message = config.alert_message
            color = 0xff0004      
        else:
            difference = datetime.datetime.now() - self.offline[member_info.id]    
            downtime = bot_utils.timedelta_to_humanreadable(difference)
            title = f"{member_info} is now back up"
            description = f"offline for {downtime}"
            message = config.up_message
            color = 0x13ff24

            self.offline.pop(member_info.id)

        #Attempt to send a message to all channels 
        for channel_id in config.channelsIds:
            channel = self.bot.get_channel(channel_id)
            if not channel:
                raise errors.ChannelNotFound(f"Channel with id `{channel_id}` could not be fetched! Are you sure it exists and and I can see it?")

            embed = discord.Embed(title=title,description=description, color=self.embed_color or color)
            await channel.send(content=message or None, embed=embed)

    @commands.Cog.listener()
    async def on_presence_update(self, before, after):
        if before.id in config.ids:
            if after.status is discord.Status.offline and after.id not in self.offline:
                await self.alert(after, True)
            elif before.status is discord.Status.offline and after.id in self.offline:
                await self.alert(after, False)

def setup(bot):
    cog = Statuschecker(bot)
    bot.add_cog(cog)
    
    print(f"Extension {cog.qualified_name} is loaded")
