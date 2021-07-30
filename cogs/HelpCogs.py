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

class help(commands.HelpCommand):
  async def send_bot_help(self, mapping):
      await self.context.send(embed=embed4)

class HelpCogs(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

    self._original_help_command = bot.help_command
    bot.help_command = help()
    bot.help_command.cog = self

  @commands.command(aliases=['F','f','faq'])
  @commands.cooldown(1, 30, commands.BucketType.channel)
  async def FAQ(self, ctx):
    await ctx.send(embed=embed5)

  @commands.command(aliases=['b','B','beginner'])
  @commands.cooldown(1, 30, commands.BucketType.channel)
  async def Beginner(self, ctx):
    await ctx.send(embed=embed6)

  @commands.command(aliases=['Q','q','questions'])
  @commands.cooldown(1, 30, commands.BucketType.channel)
  async def Questions(self, ctx):
    await ctx.send(embed=embed7)

  @commands.command(aliases=['I','i','inspiration'])
  @commands.cooldown(1, 30, commands.BucketType.channel)
  async def Inspiration(self, ctx):
    await ctx.send(embed=embed8)

  def __init__(self, bot):
    self.bot = bot

    self.bot = bot
    self._original_help_command = bot.help_command
    bot.help_command = help(command_attrs=dict(aliases=["H", "Help","h"])) 
    bot.help_command.cog = self

  def cog_unload(self):
      self.bot.help_command = self._original_help_command

embed4 = discord.Embed(
  title = '**Help Commands**',
  description = 'Use these commands for help in blender!\nUse "$cmds" for all of the commands.',
  colour = discord.Colour.blue()
)

embed5 = discord.Embed(
  title = '**Frequently Asked Questions**',
  description = 'These questions are asked often in Blender',
  colour = discord.Colour.magenta()
)

embed6 = discord.Embed(
  title = '**Beginner tools for use**',
  description = 'These resources may help you in Blender as a beginner',
  colour = discord.Colour.blurple()
)

embed7 = discord.Embed(
  title = '**Proper Questions Guide**',
  description = 'Use this guide to save time',
  colour = discord.Colour.gold()
)

embed8 = discord.Embed(
  title = '**If your looking for inspiration:**',
  description = 'Provide yourself with value so then\nwhen you see progression your\nmotivated to keep growing!',
  colour = discord.Colour.orange()
)

embed4.add_field(name = "**Help in Blender?**", value = "$FAQ ``[$F]``\n$Beginner ``[$B]``")

embed7.add_field(name = "Don't only say Hello", value = "**1.** Instead of saying Hello you could say:\nHello, could you help me [Inset Problem]?\n\n**Don't ask if anyone uses Blender**\n**2.** Instead of saying that you could say:\nCan anyone assist me in [Insert service]?\n\n**Use your resources first**\n**3.** If you don't know how to do something\nthen first Google it, or YouTube search it,\nor you can even use reddit, etc.")

embed6.add_field(name = "**Sculpting**", value = "**1.** https://www.youtube.com/watch?v=0lj643VmTsg\n\n**Modeling**\n**1.** https://www.youtube.com/watch?v=elUJCEC06r8\n**2.** https://www.youtube.com/watch?v=6mT4XFJYq-4\n**3.** https://www.youtube.com/watch?v=JMBMHSca_j0\n\n**Animating**\n**1.** https://www.youtube.com/watch?v=uDqjIdI4bF4&t=904s\n**2.** https://www.youtube.com/watch?v=_C2ClFO3FAY&t=535s\n\n**Graphic FX** ``GFX``\n**1.** https://www.youtube.com/watch?v=0F_w4ynybks\n**2.** https://www.youtube.com/watch?v=D2WuSJdQKjA\n\n**Visual FX** ``VFX``\n**1.** https://www.youtube.com/watch?v=-6nBuVHGGuI\n**2.** https://www.youtube.com/watch?v=wCge7Y-CmHk")

embed5.add_field(name = "**FAQ Blender**", value = "**1.** How to install blender?\n**2.** My mesh is see through!\n**3.** How do I subdivide?\n**4.** Blender to Roblox?\n**5.** How to extrude?\n**6.** Change blender layout?\n**7.** Blender experimental?\n**8.** Render faster?")

embed5.add_field(name = "**FAQ Answers**", value = "**1.** https://www.blender.org/download/\n **2.** Select character & go to materials, then change blend mode to Oqaque.\n**3.** Select the object & go to edit mode then right click then click subdivide.\n**4.** Save the file as a Obj file then open in roblox.\n**5.** Go to edit mode then select a face & press 'e'.\n**6.** Go to edit then preferences & click themes\n**7.** https://builder.blender.org/download/daily/\n**8.** Learn: https://www.sheepit-renderfarm.com/?tag=mazerfazer")

embed5.add_field(name = "\u200b", value = "\u200b")

embed4.add_field(name = "**Blender extras**", value = "$Questions ``[$Q]``\n$Inspiration ``[$I]``")

embed8.add_field(name = "**1.** https://www.youtube.com/watch?v=RHLn7gT6cpQ", value = " **2.** https://www.youtube.com/watch?v=n9YYrVQdCMY\n**3.** https://www.youtube.com/watch?v=_9dEqM3H31g\n **4.** https://www.youtube.com/watch?v=WG6aZDLhopg\n**5.** https://www.youtube.com/watch?v=zQVr9qyM00w\n")

def setup(bot):
  bot.add_cog(HelpCogs(bot))
