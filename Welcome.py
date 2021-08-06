BOT_PREFIX = "$"
WELCOME_CHANNEL_ID = 827603472467755008
LEAVE_CHANNEL_ID = 777396672048136212
MAX_REQUESTS = 10

from datetime import datetime
import aiosqlite
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
from discord.ext.commands import Bot
from discord_components import *

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=BOT_PREFIX, intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("WERE IN", bot.user.name)
    activity = discord.Streaming(name="Blender", url = "https://www.youtube.com/watch?v=7Gtyo_d4oqc")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    DiscordComponents(bot)

@bot.listen()
async def on_message(message):
    badwordresponse = ["Family friendly server!", "We don't use that language here!", "Watch your language!", "Language!"]
    badwords2 = ["sex","porn","fuck","pornography","hentai","dick","shit","what the fuck","drug","nigg"," nigga","fuk",
                 "cunt","cnut","d1ck","pussy","asswhole","b1tch","bitch","b!tch","blowjob","cock","c0ck","jack off","ejackulate",
                 "masterbait","penis","vaginia","penis","xvideo","xnxx","xhamster","tinder","booty", "ecchi", "nude", "nudse",
                "sh!t", "@sswhole", "d!ck", "dik", "d!k", "🖕"]
    
    content = message.content.lower()
    if any(word in content for word in badwords2):
        await message.delete()
        msg = await message.channel.send(f'{message.author.mention} **{random.choice(badwordresponse)}**')
        await asyncio.sleep(6)
        await msg.delete()

@bot.listen()
async def on_message(message):
    badwordresponse = ["Family friendly server!", "We don't use that language here!", "Watch your language!", "Language!"]
    content = message.content.lower()
    if message.content == 'ass':
        await message.delete()
        msg = await message.channel.send(f'{message.author.mention} **{random.choice(badwordresponse)}**')
        await asyncio.sleep(6)
        await msg.delete()

@bot.listen()
async def on_message(message):
    badwordresponse = ["Family friendly server!", "We don't use that language here!", "Watch your language!", "Language!"]
    content = message.content.lower()
    if message.content == 'anal':
        await message.delete()
        msg = await message.channel.send(f'{message.author.mention} **{random.choice(badwordresponse)}**')
        await asyncio.sleep(6)
        await msg.delete()

@bot.listen()
async def on_message(message):
    badwordresponse = ["Family friendly server!", "We don't use that language here!", "Watch your language!", "Language!"]
    content = message.content.lower()
    if message.content == 'Anal':
        await message.delete()
        msg = await message.channel.send(f'{message.author.mention} **{random.choice(badwordresponse)}**')
        await asyncio.sleep(6)
        await msg.delete()

@bot.listen()
async def on_message(message):
    badwordresponse = ["Family friendly server!", "We don't use that language here!", "Watch your language!", "Language!"]
    content = message.content.lower()
    if message.content == 'Ass':
        await message.delete()
        msg = await message.channel.send(f'{message.author.mention} **{random.choice(badwordresponse)}**')
        await asyncio.sleep(6)
        await msg.delete()
        
@bot.event
async def on_member_join(member):
    try:
        channel = bot.get_channel(827603472467755008)
        try:
            random_words = ['Welcome', 'Hello & welcome', 'Greetings', 'Hey', 'Hello']
            embed = discord.Embed(colour=discord.Colour.blue())
            embed.set_author(name=f'{random.choice(random_words)} {member.name}!', icon_url=member.avatar_url)
            await channel.send(embed=embed)
        except Exception as e:
            raise e
    except Exception as e:
        raise e

#await calcmsg.edit(embed=embed166)

embed9 = discord.Embed(
  title = '**Moderator commands**',
  description = 'You can use any moderator commands\nas long as you have permissions to use.\nUse prefix "$" when using commands!',
  colour = discord.Colour.teal()
)

embed10 = discord.Embed(
  title = '**All commands for Grimy Bot**',
  description = 'These are all the commands in Grimy\nbot. Use any of these commands! ',
  colour = discord.Colour.orange()
)

@bot.command(invoke_without_command=True, aliases=['Mod','mod','modcmds'])
@commands.cooldown(1,10,commands.BucketType.user)
async def Modcmds(ctx):
  await ctx.send(embed=embed9)

embed9.add_field(name = "**All moderator commands**", value = "`$mute [member]` to mute any members\n`$unmute [member]` to unmute any members\n`$ban [member]` to ban any members\n`$unban [member]` to unban any members\n`$softban [member]` to temp ban any members\n`$kick [member]` to kick any members\n`$purge [#]` to delete any amount of messages\n`$toggle [command]` to enable/disable commands\n`$event [command]` to open/close events")

@bot.command(name="commands", aliases=['C','cmds','Commands','Cmds'])
@commands.cooldown(1,10,commands.BucketType.user)
async def dashboard(ctx):
  emojis0 = ['<a:Like:868457775108354090>']
  message = channel.fetch_message(messageid)
  author = ctx.message.author
  await author.send(embed=embed10)
  await message.add_reaction(emojis0)

embed10.add_field(name = 'Use "$" when using commands!', value = "`$help` Use this for help in Blender!\n`$mod` Used for moderator commands.\n`$search` Use this to surf the web.\n`$misc` Use this for fun commands!\n`$info` Use this to get a user's info!\n`$verify` Log with your Roblox account!\n`$credit` Contributions of Grimy Bot.\n`$report` This will notify the moderators.\n`$server` To view the server's info.\n`$invites` To view user invites.")

emojis = [":Checkmark:846176167505297419", "<a:BlueVerified:868287579710169099>", "<a:Like:868457775108354090>", "<a:Bell:868457765650186290>", "<a:Applause:868457781009743922"]
emojis2 = [":YouTube:838302984701214720", "<a:TwinParrot:868457780321857597>", "<a:PepeRun:868278334046474261>", "<a:HappyPepe:868273311006740531>"]
emojis3 = ["<a:BlueVerified:868287579710169099>"]
emojis4 = [":BlenderRegular:838308035914498058",":RobloxStudios:856704412704571392"]
emojis5 = ["❤️"]
emojis6 = ["🥳"]
emojis7 = ["<a:Like:868457775108354090>", "<a:Dislike:868457777142587412>"]


@bot.listen('on_message')
async def MsgReact(message):
    if(message.channel.id == 795434230117040148):
        for i in emojis:
            await message.add_reaction(i)
    if(message.channel.id == 775103140172267530):
        for i in emojis2:
            await message.add_reaction(i)
    if(message.channel.id == 775101922914992138):
        for i in emojis3:
            await message.add_reaction(i)
    if(message.channel.id == 856250305476821042):
        for i in emojis4:
            await message.add_reaction(i)
    if(message.channel.id == 775101922914992138):
        for i in emojis3:
            await message.add_reaction(i)
    if(message.channel.id == 858908131475062835):
        for i in emojis5:
            await message.add_reaction(i)
    if(message.channel.id == 860971153929142313):
        for i in emojis6:
            await message.add_reaction(i)
    if(message.channel.id == 775103140172267530):
        for i in emojis9:
            await message.add_reaction(i)

@bot.command()
@commands.cooldown(1, 25, commands.BucketType.channel)
async def verify(ctx):
    t = 0
    embed15 = discord.Embed(color=discord.Color.orange(), description=f'{ctx.message.author.mention} Step 1/3 **Enter your Roblox username:**')

    embed18 = discord.Embed(color=discord.Color.blue(), description=f'{ctx.message.author.mention} Step 3/3 | **Verfication Completed!**')

    privKey = ' '.join(random.choices([line.strip() for line in open('words.txt', 'r')], k=7))

    embed16 = discord.Embed(color=discord.Color.orange(), description=f'{ctx.message.author.mention} Step 2/3 | **Insert following in Roblox description:**\n`{privKey}`')

    embed16.set_image(url="https://media.giphy.com/media/QxFwKWYK8LBIGvJT2d/giphy.gif")
    
    while True:
      await ctx.send(embed=embed15)
      msg = await bot.wait_for('message', check=lambda message: message.author == ctx.message.author)
      Username = msg.content
      try:
        Id = requests.get(f'https://api.roblox.com/users/get-by-username?username={msg.content}').json()['Id']
        await ctx.send(embed=embed16)
        break
      except:
        await ctx.send(f'{ctx.message.author.mention} **Unable to find your user!**')
        break
    while True:
        if requests.get(f'https://users.roblox.com/v1/users/{Id}').json()['description'] == privKey: 
            await ctx.send(embed=embed18)
            await ctx.message.author.edit(nick = msg.content)
            break
        else:
            if t >= MAX_REQUESTS: 
                await ctx.send(f"{ctx.message.author.mention} **you took to long!**")
                break
            else:
                time.sleep(3);t+=1

@bot.command(aliases=['Info'])
@commands.cooldown(1,5,commands.BucketType.user)
async def info(ctx, *, member: discord.Member=None):
    if not member:
        member = ctx.message.author
        roles = [role for role in member.roles]
    embed15 = discord.Embed().set_thumbnail(url = member.avatar_url).add_field(name="User's join date:", value=member.joined_at.strftime("```%a, %#d %B %Y, %I:%M %p EST```")).add_field(name="User's creation date:", value=member.created_at.strftime("```%a, %#d %B %Y, %I:%M %p EST```"))
    await ctx.send(embed=embed15)

@info.error
async def info_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        await ctx.send(f'**I could not find this member.**', delete_after=5)

@bot.command(aliases=['Credit','credits','Credits'], brief='credits', description='credits')
@commands.cooldown(1,20,commands.BucketType.user)
async def credit(ctx):
    user2 = await bot.fetch_user(730157936684433508)
    user3 = await bot.fetch_user(838512073989816410)
    em = discord.Embed(title="credits", color=discord.Color.gold(),
                       description="Users who participated in the creation of grimy bot.")
    em.set_image(url = 'https://media.discordapp.net/attachments/788968211307692053/865297116007366671/therewego.png?width=664&height=228')
    em.add_field(name='Inculpable', value='**`60% of Cmds`**\n**`Profile`**\n**`Welcomer`**\n**`MsgReact`**')
    em.add_field(name=user2.name, value='`$search`\n`$report`\n**`Search filter`**\n`Responder`')
    em.add_field(name=user3.name, value='`$info`\n**`Error Handlers`**\n**`Status`**\n**`Chat filter`**')
    await ctx.send(embed=em)

@bot.command(aliases=['Enter', 'E', 'e'])
async def enter(ctx, *, args):
    channel2 = bot.get_channel(858908131475062835)

    if not ctx.message.attachments:

      await ctx.send(f'{ctx.message.author.mention} **must include or be a gif/image (Only imports) & add text!**')

      attachment = ctx.message.attachments[0].url

    if(ctx.channel.id == 858907794227855380):

      attachment = ctx.message.attachments[0]

      embed16 = discord.Embed(color=discord.Color.gold(), title=f'{args}').set_image(url=f'{attachment}').set_footer(text="Created by: {} ".format(ctx.message.author.name))

      await channel2.send(embed=embed16)
      
      await ctx.send(f'{ctx.message.author.mention} **you have been listed in** <#858908131475062835>**!**')

@bot.command()
@commands.cooldown(1,20,commands.BucketType.user)
async def report(ctx, *, args, aliases=['r','R','Report']):
 if ctx.message.attachments:
  attachment02 = ctx.message.attachments[0].url
  user = await bot.fetch_user(608326260271087616)
  embed01 = discord.Embed(title = f'{args}', description = f'{ctx.message.author} ', colour = discord.Colour.random())
  embed02 = discord.Embed(title = f'Your report has been succesfully recorded.',colour = discord.Colour.random())
  embed01.set_image(url=attachment02)
  await ctx.message.delete()
  await user.send(embed=embed01)
  await ctx.send(embed=embed02, delete_after=10)

 if not ctx.message.attachments:

  user = await bot.fetch_user(608326260271087616)
  embed01 = discord.Embed(title = f'{args}', description = f'{ctx.message.author} ', colour = discord.Colour.random())
  embed02 = discord.Embed(title = f'Your report has been succesfully recorded.', colour = discord.Colour.random())
  await ctx.message.delete()
  await user.send(embed=embed01)
  await ctx.send(embed=embed02, delete_after=7)

def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)

@bot.command(name= 'restart')
async def restart(ctx):
  if ctx.author.id == 608326260271087616:
      await ctx.send("**🤖 Re-proccessing, starting now!**")
      await ctx.send("**✅ I have finished re-proccessing!**")
      restart_bot()
  else:
      await ctx.send("**Missing permission!**")
        
@bot.command(aliases=['Server', 'Serverinfo', 'serverinfo'])
@commands.cooldown(1,5,commands.BucketType.user)
async def server(ctx):
    embed116 = discord.Embed().set_thumbnail(url ='https://cdn.discordapp.com/icons/774813762733604865/a_06195d2df5258c5c55752761cb7191fc.gif?size=128&quot').add_field(name="Server's created date:", value="```Sat, 01 May 2020, 02:00 PM EST```").add_field(name="Creator: Inculpable", value="```©️ Reserved rights, article 23 section 15.```")
    await ctx.send(embed=embed116)
        
async def update_totals(member):
    invites = await member.guild.invites()

    c = datetime.today().strftime("%Y-%m-%d").split("-")
    c_y = int(c[0])
    c_m = int(c[1])
    c_d = int(c[2])

    async with bot.db.execute("SELECT id, uses FROM invites WHERE guild_id = ?", (member.guild.id,)) as cursor: # this gets the old invite counts
        async for invite_id, old_uses in cursor:
            for invite in invites:
                if invite.id == invite_id and invite.uses - old_uses > 0: # the count has been updated, invite is the invite that member joined by
                    if not (c_y == member.created_at.year and c_m == member.created_at.month and c_d - member.created_at.day < 7): # year can only be less or equal, month can only be less or equal, then check days
                        print(invite.id)
                        await bot.db.execute("UPDATE invites SET uses = uses + 1 WHERE guild_id = ? AND id = ?", (invite.guild.id, invite.id))
                        await bot.db.execute("INSERT OR IGNORE INTO joined (guild_id, inviter_id, joiner_id) VALUES (?,?,?)", (invite.guild.id, invite.inviter.id, member.id))
                        await bot.db.execute("UPDATE totals SET normal = normal + 1 WHERE guild_id = ? AND inviter_id = ?", (invite.guild.id, invite.inviter.id))

                    else:
                        await bot.db.execute("UPDATE totals SET normal = normal + 1, fake = fake + 1 WHERE guild_id = ? and inviter_id = ?", (invite.guild.id, invite.inviter.id))

                    return
    
# events
@bot.event
async def on_member_join(member):
    await update_totals(member)
    await bot.db.commit()
        
@bot.event
async def on_member_remove(member):
    cur = await bot.db.execute("SELECT inviter_id FROM joined WHERE guild_id = ? and joiner_id = ?", (member.guild.id, member.id))
    res = await cur.fetchone()
    if res is None:
        return
    
    inviter = res[0]
    
    await bot.db.execute("DELETE FROM joined WHERE guild_id = ? AND joiner_id = ?", (member.guild.id, member.id))
    await bot.db.execute("DELETE FROM totals WHERE guild_id = ? AND inviter_id = ?", (member.guild.id, memebr.id))
    await bot.db.execute("UPDATE totals SET left = left + 1 WHERE guild_id = ? AND inviter_id = ?", (member.guild.id, inviter))
    await bot.db.commit()

@bot.event
async def on_invite_create(invite):
    await bot.db.execute("INSERT OR IGNORE INTO totals (guild_id, inviter_id, normal, left, fake) VALUES (?,?,?,?,?)", (invite.guild.id, invite.inviter.id, invite.uses, 0, 0))
    await bot.db.execute("INSERT OR IGNORE INTO invites (guild_id, id, uses) VALUES (?,?,?)", (invite.guild.id, invite.id, invite.uses))
    await bot.db.commit()
    
@bot.event
async def on_invite_delete(invite):
    await bot.db.execute("DELETE FROM invites WHERE guild_id = ? AND id = ?", (invite.guild.id, invite.id))
    await bot.db.commit()

@bot.event
async def on_guild_join(guild): # add new invites to monitor
    for invite in await guild.invites():
        await bot.db.execute("INSERT OR IGNORE INTO invites (guild_id, id, uses), VAlUES (?,?,?)", (guild.id, invite.id, invite.uses))
        
    await bot.db.commit()
    
@bot.event
async def on_guild_remove(guild): # remove all instances of the given guild_id
    await bot.db.execute("DELETE FROM totals WHERE guild_id = ?", (guild.id,))
    await bot.db.execute("DELETE FROM invites WHERE guild_id = ?", (guild.id,))
    await bot.db.execute("DELETE FROM joined WHERE guild_id = ?", (guild.id,))

    await bot.db.commit()
    
# commands
@bot.command(aliases=['Invites'])
async def invites(ctx, member: discord.Member=None):
    if member is None: member = ctx.author

    # get counts
    cur = await bot.db.execute("SELECT normal, left, fake FROM totals WHERE guild_id = ? AND inviter_id = ?", (ctx.guild.id, member.id))
    res = await cur.fetchone()
    if res is None:
        normal, left, fake = 0, 0, 0

    else:
        normal, left, fake = res

    total = normal - (left + fake)
    
    em = discord.Embed(
        title=f"{member.name}#{member.discriminator}",
        description=f"**{total}** invites. (**{normal}** normal, **{left}** left, **{fake}** fake).",
        timestamp=datetime.now(),
        colour=discord.Colour.blurple())

    await ctx.send(embed=em)
    
async def setup():
    await bot.wait_until_ready()
    bot.db = await aiosqlite.connect("inviteData.db")
    await bot.db.execute("CREATE TABLE IF NOT EXISTS totals (guild_id int, inviter_id int, normal int, left int, fake int, PRIMARY KEY (guild_id, inviter_id))")
    await bot.db.execute("CREATE TABLE IF NOT EXISTS invites (guild_id int, id string, uses int, PRIMARY KEY (guild_id, id))")
    await bot.db.execute("CREATE TABLE IF NOT EXISTS joined (guild_id int, inviter_id int, joiner_id int, PRIMARY KEY (guild_id, inviter_id, joiner_id))")
    
    # fill invites if not there
    for guild in bot.guilds:
        for invite in await guild.invites(): # invites before bot was added won't be recorded, invitemanager/tracker don't do this
            await bot.db.execute("INSERT OR IGNORE INTO invites (guild_id, id, uses) VALUES (?,?,?)", (invite.guild.id, invite.id, invite.uses))
            await bot.db.execute("INSERT OR IGNORE INTO totals (guild_id, inviter_id, normal, left, fake) VALUES (?,?,?,?,?)", (guild.id, invite.inviter.id, 0, 0, 0))
                                 
    await bot.db.commit()


bot.load_extension('cogs.ToggleCog')
bot.load_extension('cogs.HelpCogs')
bot.load_extension('cogs.MiscCog')
bot.load_extension('cogs.ErrorCog')
bot.load_extension('cogs.AdminCogs')
bot.load_extension('cogs.SearchCog')

bot.loop.create_task(setup())
bot.run(os.getenv('BOT_TOKEN'))
asyncio.run(bot.db.close())

#member.avatar_url
#ctx.guild.member
#ctx.guild.owner
#user = ctx.author
#userAvatar = member.avatar_url
#member = ctx.message.author
