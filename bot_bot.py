import discord
from botb_logic import gen_emodji
from botb_logic import gen_pass
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def emoji(ctx):
    await ctx.send(gen_emodji())

@bot.command()
async def gen(ctx):
    await ctx.send((gen_pass(10)))

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("")