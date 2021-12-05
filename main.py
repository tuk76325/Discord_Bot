import discord
import random


token = 'OTE2OTU1Mzg3MzMxMjMxNzU0.YaxrQA.w7FZuhVmIjjFX74ght0zLOtLOCc'
lst = ['It is certain', 'It is decidedly so.', 'Without a doubt.', 'Yes definitely', 'You may rely on it.', 'As I see it, yes', 'Most likely.', 'Outlook good.', 'Yes.',
       'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.', "Don't count on it.",
       'My reply is no.', 'My sources say no.', 'Outlook not so good', 'Very doubtful']

client = discord.Client()

@client.event
async def on_ready():
        print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!8ball'):
        await message.channel.send(lst[random.randint(0, 19)])
        

client.run(token)