import discord
from discord.ext import commands
import time
from globals import startTime
from datetime import datetime, timedelta

class Misc:
    """Module for commands that don't fit into the other categories"""

    # Use this init method for all modules
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def uptime(self, ctx):
        """Returns how long the bot has been running"""
        d = datetime(1,1,1) + timedelta(seconds = int(time.time() - startTime))

        timestring = ("%dd %02dh %02dm %02ds" % (d.day-1, d.hour, d.minute, d.second))
        await self.bot.say(f"**Uptime:** {timestring}")
        
# The setup fucntion below is necessary. Remember we give bot.add_cog() the name of the class in this case Misc.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(Misc(bot))

