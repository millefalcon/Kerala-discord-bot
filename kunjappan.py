import os
import sys
import random
import json

import discord
from discord.ext import commands

#client.run('')

client = commands.Bot(command_prefix = '.')

# language bot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious')
# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train based on the english corpus
trainer.train("chatterbot.corpus.english")

# Train based on english greetings corpus
trainer.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
trainer.train("chatterbot.corpus.english.conversations")


# Get a response to an input statement
#resp = chatbot.get_response("Hello, how are you today?")

#client = discord.Client()
token = os.getenv('DISCORD_TOKEN')
if token is None:
    sys.exit("DISCORD_TOKEN is not found. Please set the the DISCORD_TOKEN in the environment")

with open('data.json', encoding='utf-8') as f:
    responses = json.load(f)['responses']

channel = None
@client.event
async def on_ready():
    print('Kunjappan is live')
    global channel
    channel = client.get_channel(618270738247581708)

@client.event
async def on_member_join(member):
    print(f'{member} jas joined the server')
    await channel.send(f'welcome {member.name}. Please make yourselves home :)')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')
    await channel.send(f'Good bye {member.name}. Hope to see you soon :)')

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency *1000)} ms')

ariyilla = [
    'athinulla answer njan pinne parayam.', 'ariyilla', 'marannupoyi', 'manasilayilla']
ques = [
    'endha ?', 'endhado ?', 'parado', 'chumma vilichatha ?', 'endhina viliche ?'
]
#@client.command(aliases=['para', 'vallom para', 'kunjappa'])
botname = 'kunja'
@client.command(name=botname)
async def respond(ctx, *args):
    #await ctx.send(f'{random.choice(responses)}')
    #await ctx.send(f'athe, njan thanne kunjappan :p. Parayu. chodichthe: {ctx.message}')
    
    #print(ctx.message, dir(ctx.message))
    req_text = ' '.join(args).replace(f'.{botname}', '').replace('?', '')
    print('request', req_text)
    response = chatbot.get_response(req_text)
    await ctx.send(str(response))
    """
    response = f'endha {ctx.message.author.name}, {random.choice(ques)}'
    if not args:
        await ctx.send(f"{response}")
        return None
    if '?' in ''.join(args):
        await ctx.send(f"{random.choice(ariyilla)}")
        return None
    await ctx.send(f'{random.choice(responses)}')
    """

"""
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]
    call_words = ('.kunjappa',)
    if any(call_word in message.content for call_word in call_words)== '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
"""

if __name__ == '__main__':
    client.run(token)
