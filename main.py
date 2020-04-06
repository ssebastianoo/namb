import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

bot = commands.Bot(command_prefix=commands.when_mentioned_or("namb!"), description='A Music Bot')
bot.remove_command("help")
bot.load_extension("jishaku")

@bot.event
async def on_ready():
    print('Ready as', bot.user)
    await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.listening, name = "l o f i"), status = discord.Status.idle)

for a in os.listdir("./cogs"):
    if a.endswith(".py"):
        bot.load_extension(f"cogs.{a[:-3]}")

load_dotenv(dotenv_path=".env")
token = os.environ.get("token")
bot.run(token)