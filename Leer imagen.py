import discord, requests
from discord.ext import commands
import os, random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('Images'))
    with open(f'Images/{img_name}', 'rb') as f:

        picture = discord.File(f)

    await ctx.send(file=picture)

@bot.command()
async def Superhero(ctx):
    img_name = random.choice(os.listdir('Superhero'))
    with open(f'Superhero/{img_name}', 'rb') as f:

        picture = discord.File(f)

    await ctx.send(file=picture)

@bot.command()
async def Meme(ctx):
    img_name = random.choice(os.listdir('Meme'))
    with open(f'Meme/{img_name}', 'rb') as f:

        picture = discord.File(f)

    await ctx.send(file=picture)



def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):

    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("TOKEN")
