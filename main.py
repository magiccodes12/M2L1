import os, random
import discord
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')

@bot.command()
async def programacion(ctx):
    img_name = random.choice(os.listdir("images"))
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def animales(ctx):
    img_name = random.choice(os.listdir("img"))
    with open(f'img/{img_name}', 'rb') as f:
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('dog')
async def dog(ctx):
    '''Una vez que llamamos al comando dog, 
    el programa llama a la función get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

def get_fox_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']

@bot.command('fox')
async def fox(ctx):
    '''Una vez que llamamos al comando fox, 
    el programa llama a la función get_fox_image_url'''
    image_url = get_fox_image_url()
    await ctx.send(image_url)

def get_pokemon_image_url():    
    url = 'https://pokeapi.co/api/v2/pokemon/pikachu'
    res = requests.get(url)
    data = res.json()
    return data['sprites']['back_default']

@bot.command('pokemon')
async def pokemon(ctx):
    '''Una vez que llamamos al comando pokemon, 
    el programa llama a la función get_pokemon_image_url'''
    image_url = get_pokemon_image_url()
    await ctx.send(image_url)

def get_tokio_image_url():    
    url = 'https://kitsu.io/api/edge/anime?filter[text]=tokyo'
    res = requests.get(url)
    data = res.json()
    return data['data'][0]['attributes']['posterImage']['original']

@bot.command("tokio")
async def tokio(ctx):
    '''Una vez que llamamos al comando tokio, 
    el programa llama a la función get_tokio_image_url'''
    image_url = get_tokio_image_url()
    await ctx.send(image_url)

     
bot.run("BOT TOKEN")