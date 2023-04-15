import discord
import Mindustry

from Mindustry import Server
from discord.ext import *
from discord.ext.commands import *

bot = Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("On")

@bot.command()
async def ping(ctx, ip):
    srv = Server(host=ip)
    await ctx.send(f"{srv.get_info(timeout=100)}")
    
async def sendcommand(ctx,ip, command):
    srv = Server(host=ip)
    if ctx.author.id == your id:
        await ctx.send(f"{srv.send(command=command)}")
        await ctx.send(f"Send Command To {ip} Complete!")
    else:
        await ctx.reply("You No Perm!")
bot.run("bot token")
