import discord
from discord.ext import commands
import random
#from random import shuffle

class CoOpGaming(commands.Cog):
    """Module for su commands"""

    # Use this init method for all modules
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases = ["mt"], pass_context=True)
    async def maketeams(self, ctx, numberOfTeams: int):
        """Splits the current voice chat room into a number of teams"""
        if ctx.message.author.voice_channel is None:
            await ctx.message.channel.send("You must be in a voice channel to use this command")
            #await self.bot.say("You must be in a voice channel to use this command")
            return

        channelsMade = 0
        users = ctx.message.author.voice_channel.voice_members
        random.shuffle(users)
        voiceChannels = {}

        numberOfTeams = min(numberOfTeams, len(users))

        while channelsMade < numberOfTeams:
            newChannel = await self.bot.create_channel(server=ctx.message.server, name=f"Team {channelsMade+1}", type = discord.ChannelType.voice)
            voiceChannels[channelsMade] = newChannel
            channelsMade += 1

        curChannel = 0

        for user in users:
            await self.bot.move_member(member = user, channel = voiceChannels[curChannel])
            curChannel += 1

    @commands.command(aliases = ["rt"], pass_context=True)
    async def removeteams(self, ctx):
        """Removes the created teams and returns everyone to one voice chat room"""
        # Find an empty voice channel to move everyone back to
        for channel in ctx.message.server.channels:
            if channel.type == discord.ChannelType.voice and not channel.name.startswith("Team") and len(channel.voice_members) == 0:
                moveToChannel = channel
                break

        # The moving & deleteion are separated because we can't iterate over channels and remove channels at the same time
        deleteChannels = []

        for channel in ctx.message.server.channels:
            if channel.type == discord.ChannelType.voice and channel.name.startswith("Team"):
                deleteChannels.append(channel)
                for user in channel.voice_members:
                    await self.bot.move_member(user, moveToChannel)
             
        for channel in deleteChannels:
            await self.bot.delete_channel(channel)


# The setup fucntion below is necessary. Remember we give bot.add_cog() the name of the class in this case CoOpGaming.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(CoOpGaming(bot))

