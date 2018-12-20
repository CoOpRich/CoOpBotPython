import discord
from discord.ext import commands
import os
import subprocess
import globals

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


    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def suSetSpamTimer(self, ctx, seconds: int):
        """Sets the timer for spam messaging"""
        globals.setSpamTimer(seconds)
        await self.bot.say(f"Spam timer set to {seconds} seconds")


    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def suSetSpamMessageLimit(self, ctx, messages: int):
        """Sets the message limit for spam messaging"""
        globals.setSpamMessageLimit(messages)
        await self.bot.say(f"Spam message limit set to {messages} messages")
        

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def update(self, ctx):
        """Updates the bot by pulling the latest code from Git"""
        await self.bot.say(f"**Update bot using lastest Git commits?**")
        response = await self.bot.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
        #if response is None:
            #await self.bot.say("You took too long. I'm impatient, don't make me wait")
            #return
        if response.content == "yes" or response.content == "Yes":
            """updates and reboots bot"""
            from subprocess import run
            #gitResponse = run(["sudo ls", "-lrta"])
            gitResponse = check_output(["sudo git -C /var/CoOpBotPython/ pull"], shell=True)
            await self.bot.say("Update started")
            await self.bot.say(gitResponse)
            globals.getVersion()
            await self.bot.say(globals.version)
            # Restart program
            #os.execl("/var/CoOpBotPython/CoOpBot/CoOpBot/CoOpBot.py")
            #os.execl(__file__, "")

# The setup fucntion below is necessary. Remember we give bot.add_cog() the name of the class in this case SuperUserModule.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(SuperUserModule(bot))

