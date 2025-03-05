import discord
from discord.ext import commands
import requests
import random
import os

# Set up bot with command prefix !
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Cat API endpoint
CAT_API = "https://api.thecatapi.com/v1/images/search"

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='cat')
async def get_cat(ctx):
    """Sends a random cat picture when !cat command is used"""
    try:
        # Get cat image from API
        response = requests.get(CAT_API)
        data = response.json()
        cat_url = data[0]['url']
        
        # Create embed with cat image
        embed = discord.Embed(title="Here's your cat! 🐱", color=0xFF69B4)
        embed.set_image(url=cat_url)
        
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(f"Sorry, couldn't fetch a cat picture right now! Error: {str(e)}")

# Replace 'YOUR_BOT_TOKEN' with your actual Discord bot token
bot.run(os.getenv('DISCORD_TOKEN'))

