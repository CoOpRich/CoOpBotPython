# Work with Python 3.6
import discord
from xml.dom import minidom


mydoc = minidom.parse('CoOpBotParameters.xml')
# Unique Bot Token
token = mydoc.getElementsByTagName('BotToken')[0].firstChild.data
# Command prefix character
prefixChar = mydoc.getElementsByTagName('PrefixChar')[0].firstChild.data

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith(prefixChar+"hello"):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(token)