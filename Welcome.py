BOT_PREFIX = "$"
WELCOME_CHANNEL_ID = 827603472467755008
LEAVE_CHANNEL_ID = 777396672048136212
MAX_REQUESTS = 10

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
    badwords2 = ["sex","porn","fuck","pornography","hentai","ass","dick","shit","what the fuck","drug","nigg"," nigga","fuk","cunt","cnut","d1ck","pussy","asswhole","b1tch","bitch","b!tch","blowjob","cock","c0ck","jack off","ejackulate","masterbait","penis","vaginia","penis","xvideo","xnxx","xhamster","tinder","booty", "ecchi", "nude", "nudse"]
    content = message.content.lower()
    if any(word in content for word in badwords2):
        await message.delete()
        msg = await message.channel.send(f'{message.author.mention} **Family friendly server!**')
        await asyncio.sleep(6)
        await msg.delete()

@bot.event
async def on_member_join(member):
    try:
        channel = bot.get_channel(827603472467755008)
        try:
            embed = discord.Embed(colour=discord.Colour.blue())
            embed.set_author(name=member.name, icon_url=member.avatar_url)
            embed.add_field(name=F'> {member.name} **has joined us!**', value=F"**Welcome & remember to read <#775101922914992138>\nand personalize in <#774827950478327809>**", inline=False)
            embed.set_thumbnail(url=member.avatar_url)
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
async def Modcmds(ctx):
  await ctx.send(embed=embed9)

embed9.add_field(name = "**All moderator commands**", value = "`$mute [member]` to mute any members\n`$unmute [member]` to unmute any members\n`$ban [member]` to ban any members\n`$unban [member]` to unban any members\n`$softban [member]` to temp ban any members\n`$kick [member]` to kick any members\n`$purge [#]` to delete any amount of messages\n`$toggle [command]` to enable/disable commands")

@bot.command(name="commands", aliases=['C','cmds','Commands','Cmds'])
async def dashboard(ctx):
  await ctx.send(embed=embed10)

embed10.add_field(name = 'Use "$" when using commands!', value = "`$help` Use this for help in Blender!\n`$mod` Used for moderator commands.\n`$search` Use this to surf the web.\n`$misc` Use this for fun commands!\n`$info` Use this to get a user's info!\n`$verify` Log with your Roblox account!\n`$credit` Contributions of Grimy Bot\n`$report` This will notify the moderators.")

emojis = [":Checkmark:846176167505297419"]
emojis2 = [":YouTube:838302984701214720"]
emojis3 = ["👍"]
emojis4 = [":BlenderRegular:838308035914498058",":RobloxStudios:856704412704571392"]
emojis5 = ["❤️"]
emojis6 = ["🥳"]

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

@bot.command()
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
      except: await ctx.send(f'{ctx.message.author.mention} **Unable to find your user!**')
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
async def info(ctx, *, member: discord.Member=None):
    if not member:
        member = ctx.message.author
        roles = [role for role in member.roles]
    embed15 = discord.Embed().set_thumbnail(url = member.avatar_url).add_field(name="User's join date:", value=member.joined_at.strftime("```%a, %#d %B %Y, %I:%M %p EST```")).add_field(name="User's creation date:", value=member.created_at.strftime("```%a, %#d %B %Y, %I:%M %p EST```"))
    embed15.color = 0xe4b3ab
    await ctx.send(embed=embed15)

@info.error
async def info_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        await ctx.send(f'**I could not find this member.**', delete_after=5)

@bot.command(aliases=['Credit','credits','Credits'], brief='credits', description='credits')
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
async def play(ctx):

  Choices=['Eat ramen', 'Eat paper', 'Eat potatoe', 'Eat token', 'Eat magic staff', 'Eat mushy stuff', 'Eat playdough','Eat lemons', 'Eat the barrels', 'Eat the cute panda', 'Eat the paintings', 'Eat nothing']

  bts = [
     Button(style=ButtonStyle.red, label = random.choice(Choices)),
     Button(style=ButtonStyle.blue, label = random.choice(Choices)),
     Button(style=ButtonStyle.green, label = random.choice(Choices))
]

  wordContent=["You died!", "You enjoyed!", "You had a heart attack", 'You fainted!', 'You learned how to fly!', 'You went super sayian', 'Eat it and teleport to anime world!', 'Eat this and live!', 'Ea- are you sure?', 'Eating it really?']

  content=['  https://media.discordapp.net/attachments/788968211307692053/861397315414523904/9531aca9a994cf5995da6fb423e4e5faa05ef5c7c7fa4f644cac6a8fada6d64e.png', 'https://media.discordapp.net/attachments/838315498050551828/861399043204448256/dbbf22dd0ece521d70af71ef223ebfff8d9f9ac74bc2952013b0497dc65e13f3.png', 'https://media.discordapp.net/attachments/838315498050551828/861401559367811112/62115a035004df85775da4092c41e423f628c08ed386ce2724c9bb3efe5ffaed.png', 'https://media.discordapp.net/attachments/782045221164417084/861599985123196938/unknown.png', 'https://media.discordapp.net/attachments/782045221164417084/861788945590255646/main-qimg-722ecfc93dbf9003c2c9833ee84563f2.png?width=392&height=239', 'https://media.discordapp.net/attachments/782045221164417084/861789072078143498/main-qimg-ed34733997c52d634152a1d01d34461d.png?width=482&height=270', 'https://media.discordapp.net/attachments/782045221164417084/861789160444002335/0dca507297bc9eab3251871ded823b0a.png?width=512&height=384', 'https://images-ext-2.discordapp.net/external/JfCxORi7gK8wtprXRId1d8P_fNRlSg68gW4as23dBe8/https/i.pinimg.com/originals/07/8e/e0/078ee00171b9eb2939b4e6437a4e6d7b.jpg?width=453&height=453', 'https://images-ext-2.discordapp.net/external/sydFjlCTp9DsBr5XbjSYLhhPDvbA3-VSUHDr2MfkdIo/https/i.ytimg.com/vi/X7NdykPg_mM/maxresdefault.jpg?width=805&height=453']

  urls = random.choice(content)
  wordContents = random.choice(wordContent)

  embed24 = discord.Embed(
    title = f'{wordContents}',
    colour = discord.Colour.orange()
  )

  embed24.set_image(url = f'{urls}')
  
  await ctx.send("Your starving... what do you eat?", components = [bts])
  interaction = await bot.wait_for("button_click")
  await interaction.respond(embed=embed24)

embed155 = discord.Embed(
  title = 'Win to get a special role! [Now in Beta]',
  colour = discord.Colour.blurple()
)

embed166 = discord.Embed(
  title = 'Nope',
  colour = discord.Colour.blurple()
)

@bot.command()
async def find(ctx):


    calcmsg = await ctx.send(embed=embed155)
    emojis20 = ['💩', '👻', '🤖', '😺', '💌', '💥', '👁️‍🗨️', '🗨', '💤', '🦾', '👅', '💂‍♂️']



    t = [ 
        Button(style=ButtonStyle.random_color(), label= random.choice(emojis20)),
        Button(style=ButtonStyle.random_color(), label= random.choice(emojis20)),
        Button(style=ButtonStyle.random_color(), label= random.choice(emojis20)),
        Button(style=ButtonStyle.random_color(), label= random.choice(emojis20))
    ]

    ts = [ 
        Button(style=ButtonStyle.random_color(), label= random.choice(emojis20)),
        Button(style=ButtonStyle.random_color(), label= random.choice(emojis20)),
        Button(style=ButtonStyle.random_color(), label= random.choice(emojis20)),
        Button(style=ButtonStyle.random_color(), label= random.choice(emojis20)),
    ]

    tts = [ 
        Button(style=ButtonStyle.random_color(), label= random.choice(emojis20)),
        Button(style=ButtonStyle.random_color(), label= random.choice(emojis20)),
        Button(style=ButtonStyle.random_color(), label= random.choice(emojis20)),
        Button(style=ButtonStyle.random_color(), label= random.choice(emojis20))
    ]

    await ctx.send("`This is in beta currently! type: $cmds`", components = [t, ts, tts])

    while True:
        interaction1 = await bot.wait_for("button_click", check=lambda i:i.component.label.startswith(f'{random.choice(emojis20)}'))
        await interaction1.respond(type= InteractionType.DeferredUpdateMessage, content = await calcmsg.edit(embed=embed155))
    else:
         await calcmsg.edit(embed=embed166)

@bot.command()
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

bot.load_extension('cogs.ToggleCog')
bot.load_extension('cogs.HelpCogs')
bot.load_extension('cogs.MiscCog')
bot.load_extension('cogs.ErrorCog')
bot.load_extension('cogs.AdminCogs')
bot.load_extension('cogs.SearchCog')

bot.run('ODM5MjA5MjU2ODIwNTM5NDAy.YJGUhg.EaEr2koDq4z1aURI1YASB_gGrp8')

#member.avatar_url
#ctx.guild.member
#ctx.guild.owner
#user = ctx.author
#userAvatar = member.avatar_url
#member = ctx.message.author
