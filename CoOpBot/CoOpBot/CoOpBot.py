# Work with Python 3.6
import discord
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

client = discord.Client()

@client.event
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

    if msg == None and messageStrLower.startswith(prefixChar+"hello"):
        msg = "Hello {0.author.mention}".format(message)

    if msg == None and messageStrLower.rfind("pixis") != -1:
        msg = "PIXISUUUUUUUU"

    if msg != None:
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(token)