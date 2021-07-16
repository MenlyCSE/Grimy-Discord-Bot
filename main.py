from discord.ext import commands
import discord
from Keep_alive import keep_alive
import Welcome

client = commands.Bot(command_prefix="$", intents=discord.Intents.all())

keep_alive()
