import discord
from discord.ext import commands 

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self, ctx):

        "Invite the bot"

        url = discord.utils.oauth_url(self.bot.user.id)
        emb = discord.Embed(title = "Invite Me", url = url, colour = 0x76a7b5)
        await ctx.send(embed = emb)

def setup(bot):
    bot.add_cog(Misc(bot))