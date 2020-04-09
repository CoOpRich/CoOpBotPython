import discord
from discord.ext import commands
import random

class AdminModule(commands.Cog):
    """Module for role management & other admin functions"""

    # Use this init method for all modules
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def playing(self, ctx, *gameName: str):
        """Sets the bot to be "playing" a game"""
        game = " ".join(gameName)
        await self.bot.change_presence(game=discord.Game(name=f"{game}"))


    @commands.command(aliases = ["ar"], pass_context=True)
    async def addrole(self, ctx, role: discord.Role, *users: discord.Member):
        """Add one or more users to a role"""
        for user in users:
            await self.bot.add_roles(user, role)


    @commands.command(aliases = ["rr"], pass_context=True)
    async def removerole(self, ctx, role: discord.Role, *users: discord.Member):
        """Remove one or more users from a role"""
        for user in users:
            await self.bot.remove_roles(user, role)


    @commands.command(aliases = ["nr", "createRole"], pass_context=True)
    async def newrole(self, ctx, *roleName: str):
        """Create a new role"""

        roleNameStr = " ".join(roleName)
        for role in ctx.message.server.roles:
            if role.name == roleNameStr:
                await ctx.message.channel.send(f"A role already exists with name {roleNameStr}")
                #await self.bot.say(f"A role already exists with name {roleNameStr}")
                return

        rng = lambda: random.randint(0,255)
        colourValue = '{:02x}{:02x}{:02x}'.format(rng(), rng(), rng())
        colour = discord.Colour(int(colourValue, 16))
        await self.bot.create_role(ctx.message.server, name = roleNameStr, mentionable = True, colour = colour)


    @commands.command(aliases = ["dr","deleteRoles"], pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def deleterole(self, ctx, *roles: discord.Role):
        """Delete one or more roles from the server"""
        for role in roles:
            await self.bot.delete_role(server = ctx.message.server, role = role)


    @commands.command(pass_context=True)
    async def gamerole(self, ctx, user: discord.Member):
        """Creates a role with the name of the game that the mentioned user is playing"""
        if user.game is None:
            await ctx.message.channel.send(f"{user.name} is not playing a game, no role created")
            #await self.bot.say(f"{user.name} is not playing a game, no role created")
            return
        else:
            # Make sure role does not already exist
            for role in ctx.message.server.roles:
                if role.name == user.game.name:
                    await ctx.message.channel.send(f"A role already exists with name {user.game.name}")
                    #await self.bot.say(f"A role already exists with name {user.game.name}")
                    return

        # Create the role
        rng = lambda: random.randint(0,255)
        colourValue = '{:02x}{:02x}{:02x}'.format(rng(), rng(), rng())
        colour = discord.Colour(int(colourValue, 16))
        await self.bot.create_role(ctx.message.server, name = user.game.name, mentionable = True, colour = colour)
        await ctx.message.channel.send(f"Role for {user.game.name} created")
        #await self.bot.say(f"Role for {user.game.name} created")


    @commands.command(aliases = ["rm"], pass_context=True)
    async def rolemembers(self, ctx, role: discord.Role):
        """Lists the members in the given role"""
        output = ""
        count = 0

        for user in ctx.message.server.members:
            if role in user.roles:
                output += f"\n{user.name}"
                count += 1

        if count == 0:
            await self.bot.say(f"```{role.name} has {count} members :(```\n\n**Do you want me to delete this empty role?**")
            response = await self.bot.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            #if response is None:
                #await self.bot.say("You took too long. I'm impatient, don't make me wait")
                #return
            if response.content == "yes":
                await self.bot.delete_role(server = ctx.message.server, role = role)
                await ctx.message.channel.send("Role deleted")
                #await self.bot.say("Role deleted")
                #return
        elif count == 1:
            await self.bot.say(f"```{role.name} has {count} member:{output}```")
        else:
            await self.bot.say(f"```{role.name} has {count} members:{output}```")


    # TODO - Merge roles command when string translation functionality is done
    #@commands.command(pass_context=True)
    #@commands.has_permissions(manage_roles=True)
    #async def mergeRoles(self, ctx, mergeToRole: discord.Role, mergeFromRole: discord.Role):
    #    """Merges the members from one role to another and adds a string transaltion from the old to the new (for auto role assignment)"""


    @commands.command(pass_context=True, hidden=True)
    async def fn(self, ctx):
        """Lists all the methods available for an object type. Outputs to both the client and the console.
        
        Object type must be specified in the code"""
        obj = commands
        count = 0

        output = "Object Data: "
        output += f"\nObject Type: {type(obj)}\n"

        for method in dir(obj):
            # the end=" " at the end of the print statement, 
            # makes it printing in the same line, 4 times (count)
            print("|    {:25}".format(method), end=" ")
            output += f"\n{method}"
            if (len(output) > 1900):
                await ctx.message.channel.send(f"```{output}```")
                #await self.bot.say(f"```{output}```")
                output = ""
                count = 0
            else:
                count += 1
                if count == 4:
                    count = 0
                    print("")
        await ctx.message.channel.send(f"```{output}```")
        #await self.bot.say(f"```{output}```")
        

# The setup fucntion below is necessary. Remember we give bot.add_cog() the name of the class in this case AdminModule.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(AdminModule(bot))

