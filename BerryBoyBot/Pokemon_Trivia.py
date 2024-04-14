import os
import pypokedex
import random
import asyncio
from twitchio.ext import commands

bot = commands.Bot(
    token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
    )


count = 0

monreal = False

generation = 0

guessed = False

def pokeguess(guess, chat):
    global guessed
    if pokeinfo.name == guess.name:
        guessed = True
        return f'@{chat.author.name} got it right! Pokemon #{pokeinfo.dex} is {pokeinfo.name.capitalize()}!'
    else:
        return f"@{chat.author.name} {guess.name.capitalize()} is not correct. {guess.name.capitalize()} is pokemon #{guess.dex} and is {abs(int(pokeinfo.dex) - int(guess.dex))} away!"

def checkmon(guess):
    global count
    guesslen = len(guess.content.split(" "))
    try:
        monguess = pypokedex.get(name = guess.content)
    except:
        if guesslen > pokelen:
            return
        elif guesslen == pokelen:
            if pokepart1 in guess.content:
                return pokeguess(pokeinfo, guess)
            else:
                count += 1
                return f"@{guess.author.name} {guess.content} is not registered :p"
        else:
            count += 1
            return f"@{guess.author.name} {guess.content} is not registered :p"
    count += 1
    return pokeguess(monguess, guess)

pokeinfo = pypokedex.get(dex=random.randint(1,649))

pokelen = len(pokeinfo.name.split("-"))

pokepart1 = (pokeinfo.name.split("-"))[0]

hint1 = f'Pokemon #{pokeinfo.dex} is a {pokeinfo.types[0]} type'

hint2 = ''

if pokeinfo.dex <= 151:
    generation = 1
elif pokeinfo.dex <= 251:
    generation = 2
elif pokeinfo.dex <= 386:
    generation = 3
elif pokeinfo.dex <= 493:
    generation = 4
else: 
    generation = 5

if len(pokeinfo.types) > 1:
    hint2 = f'Pokemon #{pokeinfo.dex} is {pokeinfo.types[0]} and {pokeinfo.types[1]} type and the pokemon is from generation {generation}'
else:
    hint2 = f'Pokemon #{pokeinfo.dex} is only a {pokeinfo.types[0]} type and the pokemon is from generation {generation}'