import json
import datetime

import discord
import utils.errors as errors

import config.settings as config

from discord.ext import tasks
from discord.ext import commands

class StatusChecker(commands.Cog):
    """The main cog that handles status checking."""


    def __init__(self, bot):
        self.bot = bot
        self.embed_color = config.embed_color

        self.check_status.start()

    async def alert(self, member_info):
        """Main function that handles alerting the owner(s), sends a message in all the 
        channels specified under "channels" array in settings.json"""
        for channel_id in config.channelsIds:
            channel = self.bot.get_channel(channel_id)
            if not channel:
                raise errors.ChannelNotFound(f"Channel with id `{channel_id}` could not be fetched! Are you sure it exists and and I can see it?")
                
            title = f"{member_info.name} is now **DOWN**"
            descp = f"time noticed - {datetime.datetime.utcnow()}"
            embed = discord.Embed(title=title,description=descp , timestamp=datetime.datetime.utcnow(), color=self.embed_color or 0xff0004)
                
            await channel.send(content=config.alert_mes_cont if config.alert_mes_cont else None, embed=embed)


    async def online_alert(self, member_info):
        """sends a embed if bot is online to all log channels"""
        for channel_id in config.channelsIds:
            channel = self.bot.get_channel(channel_id)
            if not channel:
                raise errors.ChannelNotFound(f"Channel with id `{channel_id}` could not be fetched! Are you sure it exists and and I can see it?")

            title = f"{member_info.name} is currently up"
            descp = f"time - {datetime.datetime.utcnow()}"
            embed = discord.Embed(title=title,description=descp , timestamp=datetime.datetime.utcnow(), color=self.embed_color or 0x13ff24)
                
            await channel.send(content=config.up_mes_cont if config.up_mes_cont else None, embed=embed)

    @tasks.loop(minutes=5)
    async def check_status(self):
        await self.bot.wait_until_ready()
        print('Main checking started.')

        for i in range(0, len(config.ids)):
            ids = config.ids
            for guild in self.bot.guilds:
                user_list = await guild.query_members(user_ids=ids,presences=True)

        for i in range(0, len(user_list)):
            user_info = user_list[i]
            if str(user_info.status) == "offline":
                await self.alert(user_info)
            elif config.online_alert:
                await self.online_alert(user_info)
    


def setup(bot):
    bot.add_cog(StatusChecker(bot))
    print("Extension StatusChecker is loaded")
