import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix='!')
token = "ODM1MDIzMTYwMDg4MDY4MDk3.YIJZ6w.Wv46oOKIunnZ3xg0aWcZBEOJM8s"

@client.event
async def on_ready():
    print("Bot is ready.")

@client.event
async def on_member_join(member):
    print(f"{member} has joined a server")

@client.event
async def on_message(message):
    if "Kyle" in message.content and not message.author.bot:
        channel = message.channel
        await channel.send(message.content.replace("Kyle", "Pogi"))
    elif "kyle" in message.content and not message.author.bot:
        channel = message.channel
        await channel.send(message.content.replace("kyle", "Pogi"))
    elif "vic" in message.content:
        channel = message.channel
        await channel.send(message.content.replace("vic", "Pogi Vic"))
    elif "victor" in message.content:
        channel = message.channel
        await channel.send(message.content.replace("victor", "Pogi Vic"))
    elif "isaac" in message.content:
        channel = message.channel
        await channel.send(message.content.replace("isaac", "pangit"))
    elif "pogi" in message.content and not message.author.bot:
        channel = message.channel
        await channel.send("Si kyle ang pogi")

client.run(token)
