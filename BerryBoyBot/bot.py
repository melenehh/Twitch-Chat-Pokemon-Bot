import os 
import asyncio
import pypokedex
import Pokemon_Trivia
import threading
import subprocess
from twitchio.ext import commands



async def poketrivia():
    return subprocess.run(['python', 'Pokemon_Trivia.py'])


bot = commands.Bot(
    token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
    )

@bot.command(name='pokestart')
async def pokestart(ctx):
    if ctx.author.name.lower() == os.environ['CHANNEL'].lower():
        await ctx.channel.send("Pokemon Trivia is starting now!")
        await ctx.channel.send(f'Which pokemon is #{Pokemon_Trivia.pokeinfo.dex}?')




@bot.event()
async def event_message(ctx):
    if ctx.echo:
        if "got it right!" in ctx.content:
            quit()
            exit()
        return
    if Pokemon_Trivia.guessed == True:
        quit()
    elif ctx.content == "$pokestart":
        return
    await ctx.channel.send(Pokemon_Trivia.checkmon(ctx))

@bot.event()
async def event_message(ctx):
    if Pokemon_Trivia.hint1 in ctx.content:
        return
    elif Pokemon_Trivia.hint2 in ctx.content:
        return
    elif Pokemon_Trivia.count == 5:
        await ctx.channel.send(Pokemon_Trivia.hint1)
    elif Pokemon_Trivia.count == 10 and Pokemon_Trivia.hint2 not in ctx.content:
        await ctx.channel.send(Pokemon_Trivia.hint2)
    elif Pokemon_Trivia.count % 5 == 0 and Pokemon_Trivia.count >= 15:
        await ctx.channel.send(Pokemon_Trivia.hint2)
    else:
        return

if 1 == 1:
    bot.run()
