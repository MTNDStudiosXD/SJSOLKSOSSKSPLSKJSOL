import discord
import asyncio
import functools
import itertools
import math
import random
import youtube_dl
from async_timeout import timeout
from discord.ext import commands
from discord import Game
from discord.ext.commands import Bot
import status
import ctypes
import json
import datetime
import random
import asyncio
import time
import client
import chalk
import keep_alive
import os
#------------------------------------
from discord.ext import *
from discord.ext import commands
#-------------------------------------

print("Bot loading...")

bot = commands.Bot(command_prefix='m?')
bot.remove_command:help

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Game(name=f"m?help | {len(bot.guilds)} Servers | Version 2", url="https://www.twitch.tv/FREEGIFTS"))
  print(f"Bot is online!") # Shows on the console that the bot is working.

@bot.command(pass_text=True)
async def doge(ctx):
  await ctx.send('Woof! https://images-na.ssl-images-amazon.com/images/I/81-yKbVND-L._SY355_.png')

@bot.command(pass_text=True)
async def invite(ctx):
  await ctx.send('Invite Link to MTND Bot Support: https://discord.gg/GUd9YgC')

@bot.command(pass_text=True)
async def ping(ctx):
    await ctx.send('Trying To Break Discord ``ToS``? Massing PING Or Pinging Someone Is Breaking It!')

@bot.command(pass_text=True)
async def gay(ctx):
    await ctx.send('no u! https://media.tenor.com/images/e6e5bf6d67496bde8f409917a217f1d2/tenor.gif')
    print ("Typing no u....")

@bot.command(pass_text=True)
async def clear(ctx, amount=5):
  if not ctx.author.permissions_in(ctx.channel).manage_messages:
    await ctx.send("Uh-Oh! Looks Like You're Missing The Permission ``Manage_Messages``!")
    return
  if not ctx.author.permissions_in(ctx.channel).manage_messages:
    await ctx.send("Uh-Oh! Looks Like You're Missing The Permission ``Manage_Messages``!")
    return
  await ctx.channel.purge(limit=amount)
  await ctx.send('Cleared.')
  return

@bot.command(pass_text=True)
async def nuke(ctx, amount=10**10):
  if not ctx.author.permissions_in(ctx.channel).manage_messages:
    await ctx.send("Uh-Oh! Looks Like You're Missing The Permission ``Manage_Messages``!")
    return
  if not ctx.author.permissions_in(ctx.channel).manage_messages:
    await ctx.send("Uh-Oh! Looks Like You're Missing The Permission ``Manage_Messages``!")
    return
  await ctx.channel.purge(limit=amount)
  await ctx.send('Channel Nuked. https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTpmGGORHb6XzBqB7v9Z2G0xOHBmCe5R692SYjFOsQAZ75-GD2g')
  return

@bot.command(none="say", pass_text=True, aliases=["announce"])
async def say(ctx, *, message):
  await ctx.message.delete()
  await ctx.send(message)

@bot.command(pass_text=True)
async def hi(ctx):
  await ctx.send('hello!')

@bot.command(pass_text=True)
async def slap(ctx, member):
  await ctx.send(f'Slapped {member} https://media3.giphy.com/media/xT9IgzTnZHL9zp6IPS/source.gif')

@bot.command(pass_text=True)
async def snipe(ctx, member):
  await ctx.send(f'Sniped {member} Oh, he must be dead, RUN!! https://media.giphy.com/media/1xpCkcxtaGERQNVku0/giphy.gif')

@bot.command(pass_text=True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, member:discord.Member, *, arg):
 author = ctx.author
 guild = ctx.message.guild


 await ctx.send(f'{member.mention} warned for: {arg} warned by: {author.mention}')
 await member.send(f'{author.mention} warned you for: {arg}')
 await ctx.message.delete()

@bot.command(pass_text=True)
async def buy(ctx):
  await ctx.send("Buy This Bot? Well, Contact ``MTND#0024``!")

keep_alive.keep_alive()
token = os.environ.get("BOT_TOKEN_HERE")
bot.run(token, bot= True, reconnect=True) 