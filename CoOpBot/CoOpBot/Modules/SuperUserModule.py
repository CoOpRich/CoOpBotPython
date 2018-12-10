import discord
from discord.ext import commands

class SuperUserModule:
    """Module for su commands"""

    # Use this init method for all modules
    def __init__(self, bot):
        self.bot = bot

    @commands.group(Name="Super user", pass_context=True)
    @commands.has_permissions(administrator=True)
    async def su(self):
        """Dummy comment to initialise su prefix"""

    @su.error
    async def su_error(self, ctx, error):
        if isinstance(ctx, commands.errors.CheckFailure):
            print("Unauthorised or incorrect attempt at running a super user command:")
            print(f"[{error.message.channel.name}]{error.message.author.name}: {error.message.content}")

        elif isinstance(ctx, commands.errors.CommandNotFound):
            print("Command not found:")
            print(f"[{error.message.channel.name}]{error.message.author.name}: {error.message.content}")
            await self.bot.say("Command not recognised")

        elif isinstance(ctx, commands.errors.CommandError):
            print("Command error:")
            print(f"[{error.message.channel.name}]{error.message.author.name}: {error.message.content}")
            print(f"[{error.message._clean_content}")

        elif isinstance(ctx, commands.errors.MissingRequiredArgument):
            print("Command missing required argument:")
            print(f"[{error.message.channel.name}]{error.message.author.name}: {error.message.content}")

        elif isinstance(ctx, commands.errors.BadArgument):
            print("Bad argument in command:")
            print(f"[{error.message.channel.name}]{error.message.author.name}: {error.message.content}")

        elif isinstance(ctx, commands.errors.NoPrivateMessage):
            print("No private message error:")
            print(f"[{error.message.channel.name}]{error.message.author.name}: {error.message.content}")

        elif isinstance(ctx, commands.errors.DisabledCommand):
            print("Command disabled:")
            print(f"[{error.message.channel.name}]{error.message.author.name}: {error.message.content}")

        elif isinstance(ctx, commands.errors.CommandInvokeError):
            print("Command invoke error:")
            print(f"[{error.message.channel.name}]{error.message.author.name}: {error.message.content}")
            print(f"[{error.message._clean_content}")

        elif isinstance(ctx, commands.errors.TooManyArguments):
            print("Too many arguments in command:")
            print(f"[{error.message.channel.name}]{error.message.author.name}: {error.message.content}")

        elif isinstance(ctx, commands.errors.UserInputError):
            print("User input error:")
            print(f"[{error.message.channel.name}]{error.message.author.name}: {error.message.content}")

        elif isinstance(ctx, commands.errors.CommandOnCooldown):
            print("Command on cooldown:")
            print(f"[{error.message.channel.name}]{error.message.author.name}: {error.message.content}")

        else:
            print("Unknown error")

    @su.command(name="test")
    async def test(self):
        await self.bot.say(f"**TEST**!")
        
# The setup fucntion below is necessary. Remember we give bot.add_cog() the name of the class in this case SuperUserModule.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(SuperUserModule(bot))

