import discord
from discord.ext import commands

class SuperUserModule:
    """Module for su commands"""

    # Use this init method for all modules
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def say(self, ctx, channel: discord.Channel, *text: str):
        """Makes the discord say the given text in the given channel"""
        message = " ".join(text)
        await self.bot.send_message(channel, f"{message}")


# The setup fucntion below is necessary. Remember we give bot.add_cog() the name of the class in this case SuperUserModule.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(SuperUserModule(bot))

