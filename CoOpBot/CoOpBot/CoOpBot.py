# Work with Python 3.6
import discord
from discord.ext import commands
from xml.dom import minidom
import random
import os
import asyncio
import globals

try:
    mydoc = minidom.parse("CoOpBotParameters.xml")
except:
    print("Unable to open file CoOpBotParameters.xml")
    raise

# Unique Bot Token
token = mydoc.getElementsByTagName('BotToken')[0].firstChild.data
# Command prefix character
prefixChar = mydoc.getElementsByTagName('PrefixChar')[0].firstChild.data

description = '''Bot for the Friendly CoOp Discord server'''
bot = commands.Bot(command_prefix = str(prefixChar), description = description)

globals.setStartTime()


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print("Prefix char: "+prefixChar)
    print('------')


#######################################################################
# 
# Background task
# runs every 5 minutes to automatically assign game roles to users
# 
#######################################################################
async def assign_game_roles():
    await bot.wait_until_ready()
    while not bot.is_closed:
        # Do for each server
        for server in bot.connection.servers:
            # Do for each user in that server
            for user in server.members:
                # Check if they are playing a game
                if user.game is None:
                    pass
                else:
                    # Loop through the roles in the current server
                    for role in server.roles:
                        # Check if the game name exists as a role
                        if user.game.name == role.name:
                            # Assign role to user if they are not a member of that role already
                            if role in user.roles:
                                pass
                            else:
                                await bot.add_roles(user, role)

        # TODO - check if a string translation exists from the game being played to a valid role name

        await asyncio.sleep(300)
    
        
#######################################################################
# 
# Anti-spam background task
# runs every time a message is sent and mutes people if they spam too many messages
# 
#######################################################################
async def antiSpam(message):
    bot.loop.create_task(globals.addSpamCounter(user = message.author, bot = bot, server = message.server, channel = message.channel))
    bot.loop.create_task(globals.reduceSpamCounter(user = message.author, bot = bot))


#######################################################################
# 
# Commands that aren't explictly called
# checks for certain text in each message
# 
#######################################################################
@bot.event
async def on_message(message):

    messageStrLower = message.content.lower()
    msg = None
    # We do not want the bot to reply to itself or any other bots
    if message.author.bot:
        return

    bot.loop.create_task(antiSpam(message))

    if messageStrLower == "ayyy":
        msg = "Ayyy, lmao"

    if msg == None and messageStrLower == "winner winner":
        msg = "Chicken dinner"

    if msg == None and messageStrLower == "new number":
        msg = "Who dis?"

    if msg == None and (messageStrLower == "you" or messageStrLower == "u"):
        msg = "No u"

    if msg == None and messageStrLower == "good bot":
        goodBotResponses = ["Good human"]
        goodBotResponses.append("No u")
        goodBotResponses.append("Why thank you!");
        goodBotResponses.append("(◠﹏◠✿)");
        goodBotResponses.append("ｖ(◠ｏ◠)ｖ");
        goodBotResponses.append("( ͡° ͜ʖ ͡°)");
        goodBotResponses.append("Beep Boop");
        goodBotResponses.append("Yes {0.author.mention}, good bot indeed".format(message));
        goodBotResponses.append("More like Gu'd bot");
        goodBotResponses.append("Bot is the Cakeob!");
        msg = random.choice(goodBotResponses)

    if msg == None and messageStrLower.rfind("pixis") != -1:
        msg = "PIXISUUUUUUUU"

    # Send Message if we have one
    if msg != None:
        await bot.send_message(message.channel, msg)
    # Try to process commands if no message sent by the bot yet
    else:
        await bot.process_commands(message)

# import modules
for file in os.listdir("Modules"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"Modules.{name}")

# Set the background task to run
bot.loop.create_task(assign_game_roles())
# Start the bot
bot.run(token, bot=True, reconnect=True)