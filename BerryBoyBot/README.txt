MAKE SURE TO READ Setup.txt

This bot is designed to spice up ad breaks and make them more enjoyable for everyone. It runs a Pokemon guessing game entirely through chat where it tells you a Pokedex number and then anyone can guess which one it is. For every wrong guess, the bot will tell you how far the guess was from the mon you are trying to guess, and then after 5 wrong guesses, it will tell you the type of the mon, and after 10 it will tell you it's second type if it has one, and what generation it is from (and repeat this hint every 5 guesses until the game is finished).

This is my first real python project and its just a little something to spice up ad breaks it is very much so a WIP although it is at a mostly functioning state, I plan on making a wordle-type module and hopefully more in the near future, and maybe eventually having it be fully available online instead of running locally. Please let me know if you have any suggestions for future games!

There are a few known bugs that I have not fully worked out yet:

1 - In the attempt to mitigate chat spam by only letting the bot respond to messages that have the same amount of words as the pokemon's name, it has started raising an error, if you see this in the cmd while running the game, do not worry the bot should still run fine, but I will continue to look into a better workaround

2 - The bot posts hint messages twice, but I decided to leave that be cause it helps make it more obvious.

3 - Sometimes the bot is a bit slow at responding and may take a few seconds to actually send a message.