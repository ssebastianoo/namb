import discord
from discord.ext import commands 

class Help(commands.Cog):

  def __init__(self, bot):

    self.bot = bot  

  @commands.command(hidden = True)
  async def help(self, ctx, *, command = None):

    "Get some help"

    if not command:

      for c in self.bot.commands:

        if not c.hidden:

          music = ""

          for a in self.bot.commands:
            if a.cog_name == "Music":
              if not a.hidden:

                music += f"`{a.name} {a.signature}` - {a.help}\n"

                try:
                  
                  for b in a.commands:

                    music += f"`{a.name} {b.name} {b.signature}` - {b.help}\n"

                except:

                  pass

          emb = discord.Embed(title = "Help", colour = discord.Colour.blurple(), timestamp = ctx.message.created_at)
          emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url_as(static_format = "png"))
          emb.add_field(name = "Music", value = music, inline = False)
          emb.set_footer(text = ctx.guild.name, icon_url = ctx.guild.icon_url_as(static_format = "png"))

          return await ctx.send(embed = emb)

    else:
        
        cmd = self.bot.get_command(command)
        error = f"Command \"`{command}`\" not found."
        emb = discord.Embed(title = "Help", colour = discord.Colour.blurple(), timestamp = ctx.message.created_at)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url_as(static_format = "png"))
        emb.set_footer(text = ctx.guild.name, icon_url = ctx.guild.icon_url_as(static_format = "png"))

        if not cmd:

          await ctx.send(error)

          return

        if not cmd.hidden:

          if cmd.parent:

            emb.add_field(value = f'`{cmd.parent} {cmd.name} {cmd.signature}`', name = "Usage", inline = False)

          else:
            
            emb.add_field(value = f'`{cmd.name} {cmd.signature}`', name = "Usage", inline = False)

          emb.add_field(name = "Definition", value = cmd.help)
          
          if cmd.aliases:

            aliases = ""

            for a in cmd.aliases:

              aliases += f"\n`{a}`"
            
            emb.add_field(name = 'Aliases', value = aliases, inline = False)

          try: 
            
            commands = ""
            
            for a in cmd.commands:
              
              commands += f"`{cmd.name} {a.name} {a.signature}`\n"
              
            emb.add_field(name = "Subcommands", value = commands, inline = False)

          except:

            pass
        
        else:

          await ctx.send(error)
          return

        await ctx.send(embed = emb)
        
        return

def setup(bot):
  bot.add_cog(Help(bot))