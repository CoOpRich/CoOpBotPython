import time
import sched
import discord
import subprocess
import asyncio
from discord.ext import commands


#######################################################################
# 
# Initialise variable names and values
# 
#######################################################################
startTime = None
spamControl = {}
spamTimer = 6
spamMessageLimit = 4


#######################################################################
# 
# Methods to change the values of variables as the bot is running
# Changes will be lost when the bot reboots
# 
#######################################################################
def setStartTime():
    global startTime
    startTime = time.time()


def setSpamTimer(seconds: int):
    global spamTimer
    spamTimer = seconds


def setSpamMessageLimit(messageCount: int):
    global spamMessageLimit
    spamMessageLimit = messageCount
    
def getVersion():
    global version
    from subprocess import run
    version = run(["sudo git", "rev-parse", "/var/CoOpBotPython/", "--short", "HEAD"], shell=True)

#######################################################################
# 
# Other functions
# 
#######################################################################
async def addSpamCounter(user: discord.Member, bot: commands.Bot, server: discord.Server, channel: discord.Channel):
    global spamControl
    global spamMessageLimit

    if user not in spamControl:
        spamControl[user] = 1
    else:
        spamControl[user] += 1
       
    if spamControl[user] == spamMessageLimit:
        await bot.send_message(channel, "#StopCamSpam")

        mutedRole = None
        for role in server.roles:
            if role.name == "Muted":
                mutedRole = role
                break

        if mutedRole is not None:
            await bot.add_roles(user, role)
        else:
            await bot.send_message(channel, "Unable to mute user, make sure the **Muted** role exists")


async def reduceSpamCounter(user: discord.Member, bot: commands.Bot):
    global spamControl
    global spamTimer
    global spamMessageLimit

    await asyncio.sleep(spamTimer)
    
    if user in spamControl:
        spamControl[user] -= 1
        
    if spamControl[user] == (spamMessageLimit-1):
        mutedRole = None
        for role in user.roles:
            if role.name == "Muted":
                mutedRole = role
                break
            
        if mutedRole is not None:
            await bot.remove_roles(user, role)
