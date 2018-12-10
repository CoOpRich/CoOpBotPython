import discord
from discord.ext import commands
import random

class RollModule:
    """Module for dice rolls, coin flips, etc"""

    # Use this init method for all modules
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="coinflip", aliases=["flip"])
    async def coinflip(self):
        coinsides = ['Heads', 'Tails']
        await self.bot.say(f"Coin flip result: **{random.choice(coinsides)}**!")
        
# The setup fucntion below is necessary. Remember we give bot.add_cog() the name of the class in this case RollModule.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(RollModule(bot))

