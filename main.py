import discord
import yaml
import random
from discord.ext import commands
import os
intents = discord.Intents.default()
intents.messages = True


#client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print(f'Chrum chrum witam tu użytkowniczka {bot.user.name}')


@bot.command(name='roll',help='Gra dla prawdziwych mężczyzn')
async def roll(ctx,max=100):
    print('rolling')
    try:
        rolled = random.randrange(1,max)
    except ValueError:
        await ctx.send(f'Zjebałeś, *{ctx.author.name}*. Podaj liczbę powyżej 1')
        return

    if rolled == 1:
        await ctx.send(f'<:gogogo:1004137356422557776> To twój koniec, *{ctx.author.name}*. Przegranko. <:gogogo:1004137356422557776>')
    else:
        await ctx.send(f'Użytkownik *{ctx.author.name}* wyrollował {rolled}!')


if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_TOKEN")
    bot.run(TOKEN)