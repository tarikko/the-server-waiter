# bot.py
import sys
import os
import time
import random
from PIL import Image, ImageDraw, ImageFont
import io
import discord
from discord.ext import tasks, commands
from discord import File
import asyncio
from unidecode import unidecode
import unicodedata

TOKEN = 'NzM1NDkzNjkzMTk2MjA2MDgy.XxhD4Q.YLGhN7Cjxm6M5y5OyM3wmvrER7w'
GUILD = 'Freework'

bot = discord.Client()
bot = commands.Bot(command_prefix='>')
bot.remove_command('help')

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    #members = '\n - '.join([member.name for member in guild.members])
    #print(unicodedata.normalize('NFKC', f"{members}"))

    while True :
        await bot.change_presence(activity=discord.Game(name=">help"))
        await asyncio.sleep(1)
        await bot.change_presence(activity=discord.Game(name=">documentation"))
        await asyncio.sleep(1)
        for guild in bot.guilds:
            if guild.name == GUILD:
                break
        channel = bot.get_channel(737992023184900197)
        await channel.edit(name = f'Total members : {guild.member_count}')


    #async for entry in guild.audit_logs(limit=100):
    #   print(unicodedata.normalize('NFKC', "{0.user} did {0.action} to {0.target}".format(entry)).encode("utf-8"))
    
@bot.event
async def on_message(message):
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    if message.author == bot.user:
        return

    if message.content.startswith('make coffee'):
        await message.channel.send('here is your coffee :coffee: !')
    if message.content.startswith('add text channel'):
        rand = random.randint(0, 100)
        name = 'personal-channels'
        category = discord.utils.get(guild.categories, name=name)
        await guild.create_text_channel(f'general-channel-ID-{rand}', category=category)
        await message.channel.send('channel created !') 
    if message.content.startswith('add voice channel'):
        rand = random.randint(0, 100)
        name = 'personal-channels'
        category = discord.utils.get(guild.categories, name=name)
        await guild.create_voice_channel(f'general-channel-ID-{rand}', category=category)
        await message.channel.send('channel created !')

    bad_words = ["anal", "banus", "barse", "ass", "b00b", "b0ll0ck", "b0ll0k", "b0ner", "b1atch", "b1tch", "balls", "ballsack", "bastard", "biatch", "bitch", "bl0w j0b", "bl0wj0b", "blow" , "blowjob", "bollock", "bollok", "boner", "boob", "bugger", "bum", "butt", "buttplug", "c00n", "c0ck", "cl1t0r1s", "cl1tor1s", "clit0ris", "clitoris",  "cock", "coon", "crap", "cunt", "d1ck", "d1ld0", "d1ldo", "damn", "dick", "dild0", "dildo", "d1psh1t", "dipsh1t", "dipshit", "dyke", "f u c k", "fag", "fart", "feck", "felch1ng", "felching",  "fellat10", "fellat1o", "fellate", "fellati0", "fellatio", "flange", "fuck", "fudge", "packer", "fudgepacker", "g0d damn", "g0ddamn", "god damn",  "goddamn",  "h0m0", "homo",  "j1zz",  "jerk",  "jizz",  "kn0b end",  "kn0bend",  "knob end",  "knobend",  "lab1a",  "labia",  "muff",  "n1gga",  "n1gger",  "nigga",  "nigger",  "p00p",  "p1ss",  "pen1s",  "penis",  "piss",  "poop", "prick",  "pube",  "pussy",  "queer",  "s h1t",  "s hit",  "scr0tum",  "scrotum",  "sh1t",  "shit",  "slut",  "smegma",  "spunk",  "t0sser",  "t1t",  "tit",  "tosser",  "turd",  "twat",  "vag1na",  "vagina",  "wank",  "wh0re",  "whore"]

    for word in bad_words:
        if message.content.count(word) > 0:
            await message.channel.purge(limit=1)
            await message.channel.send(f'（╬ಠ益ಠ) {message.author.mention} Saying ***BAD*** words like ||`**{word}**`|| is against the rules !')

    await bot.process_commands(message)
    
@bot.command()
async def add(ctx, left: int, right: int):
    sum = left + right
    await ctx.send(f"{left} + {right} = {sum}")

@bot.command()
async def devise(ctx, left: int, right: int):
    sum = left / right
    await ctx.send(f"{left} / {right} = {sum}")

@bot.command()
async def multiply(ctx, left: int, right: int):
    sum = left * right
    await ctx.send(f"{left} * {right} = {sum}")

@bot.command()
async def substract(ctx, left: int, right: int):
    sum = left - right
    await ctx.send(f"{left} - {right} = {sum}")

@bot.command()
async def ping(ctx):
    await ctx.channel.send('{0}S'.format(round(bot.latency, 1)))

@bot.command()
async def test(ctx, *args):

    for member in ctx.message.mentions:
        await ctx.send(f'{member.mention}')

@bot.command()
async def add_text_channel(ctx, name: str, *args):
    create = bot.get_channel(736612058480508998)
    if ctx.channel == create :
        category = discord.utils.get(ctx.guild.categories, name=category_name)
        category_name = 'personal-channels'
        member_role = discord.utils.get(ctx.guild.Role.name, name="Member")
        personal_channel = await ctx.guild.create_text_channel(f'{name}', category=category)
        await personal_channel.set_permissions(ctx.message.author, read_messages=True, send_messages=True)
        await personal_channel.set_permissions(ctx.guild.default_role, read_messages=True, send_messages=True)
        await personal_channel.set_permissions(member_role, read_messages=False, send_messages=False)
        await ctx.send('channel created !') 
    else:
        await ctx.channel.send(f'To use this command, You need to write it in {create.mention}')

@bot.command()
async def add_voice_channel(ctx, name: str, person: discord.Member):
    create = bot.get_channel(736612058480508998)
    if ctx.channel == request_channel :
        category_name = 'personal-channels'
        category = discord.utils.get(ctx.guild.categories, name=category_name)
        personal_channel = await ctx.guild.create_voice_channel(f'{name}', category=category) 
        await personal_channel.set_permissions(person, read_messages=True, send_messages=True)
        await ctx.send('channel created !') 
    else:
        await ctx.channel.send(f'To use this command, You need to write it in {create.mention}')

@bot.command()
async def remove_text_channel(ctx, channel: discord.TextChannel):
    create = bot.get_channel(736612058480508998)
    if ctx.channel == request_channel :
        channel_name = channel.name
        await ctx.send(f" \'{channel_name}\' is being deleted .....")
        await channel.delete()
        await ctx.send("Successfully deleted !")
    else:
        await ctx.channel.send(f'To use this command, You need to write it in {create.mention}')

@bot.command()
async def remove_voice_channel(ctx, channel: discord.VoiceChannel):
    create = bot.get_channel(736612058480508998)
    if ctx.channel == request_channel :
        channel_name = channel.name
        await ctx.send(f" \'{channel_name}\' is being deleted .....")
        await channel.delete()
        await ctx.send("Successfully deleted !")
    else:
        await ctx.channel.send(f'To use this command, You need to write it in {create.mention}')
@bot.command()
async def request(ctx):
    await ctx.send("*** Please type the title for your request :***")
    def check(MT):
        return MT.content
    title = await bot.wait_for("message", check=check)
    await ctx.send("*** Please type the description for your request :***")
    def check(MD):
        return MD.content
    content = await bot.wait_for("message", check=check)
    choose_the_right_person = bot.get_channel(735458766165770260)
    await ctx.send(f"*** Please mention the people you need, (for more info, check {choose_the_right_person.mention}) ***")
    def check(MM):
        return MM.content
    mentions = await bot.wait_for("message", check=check)
    await ctx.send("*** Please choose a color for your request (EX: #000000) [optional, for skipping type \"skip\"] :***")
    def check(MC):
        return MC.content
    check_skip = await bot.wait_for("message", check=check)
    if check_skip.content == "skip" :
        channel = bot.get_channel(735222904530141244)
        embed = discord.Embed(title =  title.content, description = 'Request by ' + ctx.message.author.mention + '\n' + content.content + "\nFreelancers needed are : " + mentions.content, color = 0x000000)
        message_embed = await channel.send(embed=embed)
        await message_embed.add_reaction('✅')
        DM = await ctx.message.author.create_dm()
        await DM.send("Hey there ! your request id is `" + str(message_embed.id) + "`" + "\n" + "To see the freelancer who want to work for you type \"`>freelancers_list <your request id>`\"\nTo delete your request type \"`>delete_request <your request id>`\"")
    else :
        request_color_1 = check_skip.content.replace("#", "0x")
        request_color_2 = int(request_color_1, 16)
        channel = bot.get_channel(735222904530141244)
        embed = discord.Embed(title =  title.content, description = 'Request by ' + ctx.message.author.mention + '\n' + content.content + "\nFreelancers needed are : " + mentions.content, color = request_color_2)
        message_embed = await channel.send(embed=embed)
        await message_embed.add_reaction('✅')
        DM = await ctx.message.author.create_dm()
        await DM.send("Hey there ! your request id is `" + str(message_embed.id) + "`" + "\n" + "To see the freelancers who want to work for you type \"`>freelancers_list <your request id>`\"\nTo delete your request type \"`>delete_request <your request id>`\"")

@bot.command()
async def freelancers_list(ctx, id: int):
    channel_name = bot.get_channel(735222904530141244)
    msg = await channel_name.fetch_message(id)
    # await ctx.channel.send(msg.reactions[0])
    reaction = msg.reactions[0]
    users = await reaction.users().flatten()
    # people_who_reacted = users[0].mention
    the_manager_id = '<@449327117885505550>'
    DM = await ctx.message.author.create_dm()
    await DM.send("The users who want to work for you are : ")
    for x in range(1,len(users)): 
        await DM.send(str(users[x].mention))
    await DM.send( "\nRequest ID : " + str(id) + "\nFor hireing the freelancers DM them or talk with them on a private channel in the server \nFor help, just DM " + str(the_manager_id) + " or ping him in the server to talk to him.\nRequest preview : ")
    await DM.send(embed=msg.embeds[0])

@bot.command()
async def delete_request(ctx, id: int):
    channel_name = bot.get_channel(735222904530141244)
    msg = await channel_name.fetch_message(id)
    await msg.delete()
    await ctx.channel.send('Request deleted !')

@bot.command()
async def colors(ctx):
    embed = discord.Embed(title = "Some nice colors :", description = "#b62828 \n #d57211 \n #ffce00 \n #ffee2d \n #36395a \n ***For reviewing the colors type \'>review_color\' and type the hex code*** \n EX : >review_color #d57211 \n for more hex colors check out : https://www.w3schools.com/Colors/colors_picker.asp", color = 0xb62828)
    await ctx.send(embed=embed)

@bot.command(name='review_color')
async def review_color(ctx, color: str):
    def hex_to_rgb(value):
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

    color_value = hex_to_rgb(color)

    IMAGE_WIDTH = 200
    IMAGE_HEIGHT = 200 

    image = Image.new('RGB', (IMAGE_WIDTH, IMAGE_HEIGHT))

    draw = ImageDraw.Draw(image)
    draw.rectangle([200, 200, 0, 0], fill=color_value)

    buffer = io.BytesIO()

    image.save(buffer, format='PNG')

    buffer.seek(0)

    await ctx.send(file=File(buffer, 'myimage.png'))

@bot.command()
async def help(ctx):
    id = '<@449327117885505550>'
    embed = discord.Embed(title = "INFO :", description = f"I am a bot created by {id} \n I manage this server and organise it \n If you want a bot like it just contact {id} in the DM or ping him in the chat \n ***The commands are : *** \n **>add** ----> adds  a number to another one \n **EX :** >add 1 2 \n **result :** 1 + 2 = 3 \n ¤¸¸.•´¯`•¸¸.•..>> ☵ <<..•.¸¸•´¯`•.¸¸¤¸¸.•´¯`•¸¸.•..>> ☵ <<..•.¸¸•´¯`•.¸¸¤ \n **>substract** ----> substracts the first number by the second one \n **EX :** >substract 3 2 \n **result :** 3 - 2 = 1 \n  ¤¸¸.•´¯`•¸¸.•..>> ☵ <<..•.¸¸•´¯`•.¸¸¤¸¸.•´¯`•¸¸.•..>> ☵ <<..•.¸¸•´¯`•.¸¸¤ \n **>devise** ----> devises the first number by the second one \n **EX :** >devise 2 2 \n **result :** 2 / 2 = 1 \n ", color = 0xDD4124)
    await ctx.send(embed=embed)

'''@bot.command()
async def help(ctx):
    embed = discord.Embed(title = "The bot commands are :", description = "- >add (first number) (second number) \n adds two numbers\n - >devise \n - >multiply \n - >substract \n - >add_custom_text_channel", color = 0xb62828)
    await ctx.send(embed=embed)'''

bot.run(TOKEN)
