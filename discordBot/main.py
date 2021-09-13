from os import terminal_size
import discord
from discord import client
from discord.ext import commands
from discord.ext.commands.core import command

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('-------')
    
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        if message.content.startswith('hello'):
            await message.reply('Hello!', mention_author=True)

        if message.content.startswith('f off'):
            await message.reply('Bhak sale', mention_author=True)

        if (message.content.startswith('chup be')) or (message.content.startswith('Chup be')):
            await message.reply('Thik hai bhai maaf kardo', mention_author=True)

        if (message.content.startswith('ping')) or (message.content.startswith('Ping')):
            await message.reply('Pong!! {0}'.format(round(client.latency, 1)))

client = MyClient()
client.run("NzA1Njg0OTcwNDY2OTY3NTcy.XqvSVw.1K9UTTzJ-CzvBvK_-4VkrCVaW68")

# @client.event
# async def on_message(message):
#     print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
#     if str(message.author) == f"{message.author}" and "hello" in message.content.lower():
#         await message.channel.send('Hi!')

# @client.event
# async def on_message(message):
#     print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
#     if str(message.author) == f"{message.author}" and "f off" in message.content.lower():
#         await message.channel.send('Bhak sale')

# @client.event
# async def on_message(message):
#     print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
#     if str(message.author) == f"{message.author}" and "chup be" in message.content.lower():
#         await message.channel.send('Thik hai bhai maaf kardo')
 
# client.run("NzA1Njg0OTcwNDY2OTY3NTcy.XqvSVw.1K9UTTzJ-CzvBvK_-4VkrCVaW68")