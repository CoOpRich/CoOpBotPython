import discord
from discord.ext import commands

class SuperUserModule(commands.Cog):
    """Module for su commands"""

    # Use this init method for all modules
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def say(self, ctx, guild: discord.Guild, *text: str):
        """Makes the discord say the given text in the given channel"""
        message = " ".join(text)
        await ctx.message.channel.send(f"{message}")
        #await self.bot.send_message(channel, f"{message}")
        

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def update(self, ctx):
        await ctx.message.channel.send(f"**Update bot using lastest Git commits?**")
        #await self.bot.say(f"**Update bot using lastest Git commits?**")
        response = await self.bot.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
        #if response is None:
            #await self.bot.say("You took too long. I'm impatient, don't make me wait")
            #return
        if response.content == "yes":
            """updates and reboots bot"""
            from subprocess import call
            call(["sudo git -C /var/CoOpBotPython/ pull"])
            await ctx.message.channel.send("Update started")
            #await self.bot.say("Update started")
            # Restart program

# The setup fucntion below is necessary. Remember we give bot.add_cog() the name of the class in this case SuperUserModule.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(SuperUserModule(bot))

