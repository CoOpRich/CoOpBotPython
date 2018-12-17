import discord
from discord.ext import commands
import random

class AdminModule:
    """Module for role management functions"""

    # Use this init method for all modules
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["ar"], pass_context=True)
    async def addRole(self, ctx, role: discord.Role, *users: discord.Member):
        """Add one or more users to a role"""
        for user in users:
            await self.bot.add_roles(user, role)

    @commands.command(aliases = ["rr"], pass_context=True)
    async def removeRole(self, ctx, role: discord.Role, *users: discord.Member):
        """Remove one or more users from a role"""
        for user in users:
            await self.bot.remove_roles(user, role)

    @commands.command(aliases = ["dr","deleteRoles"], pass_context=True)
    async def deleteRole(self, ctx, *roles: discord.Role):
        """Delete one or more roles from the server"""
        for role in roles:
            await self.bot.delete_role(server = ctx.message.server, role = role)

    @commands.command(pass_context=True, hidden=True)
    async def fn(self, ctx):
        """Lists all the methods available for an object type. Outputs to both the client and the console.
        
        Object type must be specified in the code"""
        obj = self.bot
        count = 0

        output = "Object Data: "
        output += f"\nObject Type: {type(obj)}\n"

        for method in dir(obj):
            # the end=" " at the end of the print statement, 
            # makes it printing in the same line, 4 times (count)
            print("|    {:25}".format(method), end=" ")
            output += f"\n{method}"
            if (len(output) > 1900):
                await self.bot.say(f"```{output}```")
                output = ""
                count = 0
            else:
                count += 1
                if count == 4:
                    count = 0
                    print("")
        await self.bot.say(f"```{output}```")
        
# The setup fucntion below is necessary. Remember we give bot.add_cog() the name of the class in this case RollModule.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(AdminModule(bot))

