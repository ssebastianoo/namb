import discord
from discord.ext import commands 
import platform
import psutil
from datetime import datetime

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.launchtime = datetime.utcnow()

    @commands.command()
    async def invite(self, ctx):

        "Invite the bot"

        url = discord.utils.oauth_url(self.bot.user.id)
        emb = discord.Embed(title = "Invite Me", url = url, colour = 0x76a7b5)
        await ctx.send(embed = emb)

    @commands.command()
    async def about(self, ctx):

        "See bot info"

        invite = discord.utils.oauth_url(self.bot.user.id)

        delta_uptime = datetime.utcnow() - self.launchtime
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        uptime = f"{days}d {hours}h {minutes}m {seconds}s"

        owner = self.bot.get_user(self.bot.owner_id)

        emb = discord.Embed(colour = discord.Colour.greyple())
        emb.add_field(name = "Developer", value = owner)
        emb.add_field(name = "Invite", value = f"**[Click Me]({invite})**")
        emb.add_field(name = "Uptime", value = uptime)
        emb.add_field(name = "Library", value = f"discord.py {discord.__version__}")
        emb.add_field(name = "Python", value = platform.python_version())
        emb.add_field(name = "Memory", value = f"{psutil.virtual_memory()[2]}%")
        emb.add_field(name = "CPU", value = f"{psutil.cpu_percent()}%")
        emb.add_field(name = "Operative System", value = platform.system())
        emb.add_field(name = "Guilds", value = len(self.bot.guilds))
        emb.add_field(name = "Users", value = len(self.bot.users))
        emb.set_thumbnail(url = self.bot.user.avatar_url_as(static_format = "png"))

        await ctx.send(embed = emb)

def setup(bot):
    bot.add_cog(Misc(bot))