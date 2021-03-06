import discord
from discord.ext import commands
import os
import subprocess
import sys
import globals

class SuperUserModule(commands.Cog):
    """Module for su commands"""

    # Use this init method for all modules
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def say(self, ctx, *text: str):
        """Makes the discord say the given text in the given channel"""
        message = " ".join(text)
        await ctx.message.channel.send(f"{message}")
        #await self.bot.send_message(channel, f"{message}")
        

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def suSetSpamTimer(self, ctx, seconds: int):
        """Sets the timer for spam messaging"""
        globals.setSpamTimer(seconds)
        await ctx.message.channel.send(f"Spam timer set to {seconds} seconds")
        #await self.bot.say(f"Spam timer set to {seconds} seconds")


    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def suSetSpamMessageLimit(self, ctx, messages: int):
        """Sets the message limit for spam messaging"""
        globals.setSpamMessageLimit(messages)
        await ctx.message.channel.send(f"Spam message limit set to {messages} messages")
        #await self.bot.say(f"Spam message limit set to {messages} messages")
        
    def restartBot():
        os.execv(__file__, sys.argv)
        #os.execl(" /var/CoOpBotPython/CoOpBot/CoOpBot/CoOpBot.py")

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def restart(self, ctx):
        SuperUserModule.restartBot()

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def update(self, ctx):
        await ctx.message.channel.send(f"**Update bot using lastest Git commits?**")
        #await self.bot.say(f"**Update bot using lastest Git commits?**")
        response = await self.bot.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
        #if response is None:
            #await self.bot.say("You took too long. I'm impatient, don't make me wait")
            #return
        if response.content == "yes" or response.content == "Yes":
            """updates and reboots bot"""
            from subprocess import check_output
            gitResponse = check_output(["sudo git -C /var/CoOpBotPython/ pull"], shell=True)
            #await self.bot.say("Update started")
            await ctx.message.channel.send("Update started")
            #await self.bot.say(gitResponse)
            await ctx.message.channel.send(gitResponse) # Should show results from pull
            globals.getVersion() # gets github commit log
            await ctx.message.channel.send(globals.version)
            #await self.bot.say(globals.version)
            # Restart program
            SuperUserModule.restartBot()

# The setup fucntion below is necessary. Remember we give bot.add_cog() the name of the class in this case SuperUserModule.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(SuperUserModule(bot))

