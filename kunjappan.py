import os
import sys
import random
import json

import discord
from discord.ext import commands

#client.run('')

client = commands.Bot(command_prefix = '.')

#client = discord.Client()
token = os.getenv('DISCORD_TOKEN')
if token is None:
    sys.exit("DISCORD_TOKEN is not found. Please set the the DISCORD_TOKEN in the environment")

with open('data.json') as f:
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

ariyilla = ['athinulla answer njan pinne parayam.', 'ariyilla', 'marannupoyi',
           'manasilayilla']
#@client.command(aliases=['para', 'vallom para', 'kunjappa'])
@client.command(name='kunjappa')
async def diag(ctx, *args):
    #await ctx.send(f'{random.choice(responses)}')
    #await ctx.send(f'athe, njan thanne kunjappan :p. Parayu. chodichthe: {ctx.message}')
    
    #print(ctx.message, dir(ctx.message))
    response = f'endha {ctx.message.author.name} ? para'
    if not args:
        await ctx.send(f"{response}")
        return None
    if '?' in ''.join(args):
        await ctx.send(f"{random.choice(ariyilla)}")
        return None
    await ctx.send(f'{random.choice(responses)}')

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
