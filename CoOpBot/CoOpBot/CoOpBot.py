# Work with Python 3.6
import discord
from discord.ext import commands
from xml.dom import minidom
import random

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
bot = commands.Bot(command_prefix = str(prefixChar), description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print("Prefix char: "+prefixChar)
    print('------')



#######################################################################
# 
# Commands callable in the chat by using the prefix character
# 
#######################################################################
@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command(aliases=["flip"])
async def coinflip():
    print('coinflip')
    coinsides = ['Heads', 'Tails']
    await bot.say(f"Coin flip result: **{random.choice(coinsides)}**!")
    



#######################################################################
# 
# Commands that aren't explictly called
# checks for certain text in each message
# 
#######################################################################
@bot.event
async def on_message(message):

    messageStrLower = message.content
    msg = None
    # We do not want the bot to reply to itself or any other bots
    if message.author.bot:
        return
    
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

# Start the bot
bot.run(token)