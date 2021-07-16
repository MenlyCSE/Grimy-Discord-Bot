import discord
import os
import shutil
from discord.ext import commands
from discord.ext import commands, tasks
from main import commands
from discord.utils import get
import asyncio
import discord, requests, time, random
from discord.ext.commands import MissingPermissions
from googlesearch import search
import traceback
import sys

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())

class toggle(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="toggle",description="Disable or Enable")
  @commands.has_permissions(administrator=True)
  async def toggle(self, ctx, *, command):

      embed20 = discord.Embed(title = 'Events are currently closed! Winners will be announced!', colour = discord.Colour.red())

      embed24 = discord.Embed(title = 'Events are currently opened! You may enter in now!', colour = discord.Colour.blue())

      embeds = [embed20, embed24]

      command = self.bot.get_command(command)
      channel2 = bot.get_channel(858908131475062835)
      if command is None:
          await ctx.send("**That command doesn't exist :(**", delete_after=5)
      elif ctx.command == command:
          await ctx.send("**You cannot disable this command :(**", delete_after=5)
      else:
          command.enabled = not command.enabled
          quirk = await ctx.send(embed=embed24) if command.enabled else await ctx.send(embed=embed20)
          await ctx.message.delete()

def setup(bot):
  bot.add_cog(toggle(bot))