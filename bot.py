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
from datetime import datetime, timedelta
from pytz import timezone, country_timezones
import pytz
import json
#from unidecode import unidecode
#import unicodedata

TOKEN = 'Your token'
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
        await bot.change_presence(activity=discord.Game(name=">commands"))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Game(name=">documentation"))
        await asyncio.sleep(5)
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
   
    bad_words = ["anal", "banus", "barse", "ass", "b00b", "b0ll0ck", "b0ll0k", "b0ner", "b1atch", "b1tch", "balls", "ballsack", "bastard", "biatch", "bitch", "bl0w j0b", "bl0wj0b", "blow" , "blowjob", "bollock", "bollok", "boner", "boob", "bugger", "bum", "butt", "buttplug", "c00n", "c0ck", "cl1t0r1s", "cl1tor1s", "clit0ris", "clitoris", "cock", "coon", "crap", "cunt", "d1ck", "d1ld0", "d1ldo", "damn", "dick", "dild0", "dildo", "d1psh1t", "dipsh1t", "dipshit", "dyke", "fag", "fart", "feck", "felch1ng", "felching",  "fellat10", "fellat1o", "fellate", "fellati0", "fellatio", "flange", "fuck", "fudge", "packer", "fudgepacker", "g0d damn", "g0ddamn", "god", "damn",  "goddamn",  "h0m0", "homo",  "j1zz",  "jerk",  "jizz",  "kn0b",  "kn0bend",  "knobend",  "lab1a",  "labia",  "muff",  "n1gga",  "n1gger",  "nigga",  "nigger",  "p00p",  "p1ss",  "pen1s",  "penis",  "piss",  "poop", "prick",  "pube",  "pussy",  "queer",  "s h1t",  "s hit",  "scr0tum",  "scrotum",  "sh1t",  "shit",  "slut",  "smegma",  "spunk",  "t0sser",  "t1t",  "tit",  "tosser",  "turd",  "twat",  "vag1na",  "vagina",  "wank",  "wh0re",  "whore"]

    words = message.content.split()
    words_count = len(words)

    for word in bad_words :
        for x in range(words_count) : 
            if words[x] == word :
                await message.channel.purge(limit=1)
                await message.channel.send(f'（╬ಠ益ಠ) {message.author.mention} Saying ***BAD*** words like ||`{word}`|| is against the rules !')

    await bot.process_commands(message)
    

'''@bot.command()
    async def ping(ctx):
await ctx.channel.send('{0}S'.format(round(bot.latency, 1)))'''

'''@bot.command()
async def test(ctx, *args):

    for member in ctx.message.mentions:
        await ctx.send(f'{member.mention}')'''

@bot.command()
async def add_text_channel(ctx, name: str, person: discord.Member):
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    create = bot.get_channel(736612058480508998)
    if ctx.channel == create :
        member_role = guild.get_role(736305813294940231)
        seconds = 3600
        time_m = seconds / 60
        time_h = time_m / 60
        category_name = 'personal-channels'
        category = discord.utils.get(ctx.guild.categories, name=category_name)
        personal_channel = await ctx.guild.create_text_channel(f'{name}', category=category) 
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = True
        overwrite.read_messages = True
        await personal_channel.set_permissions(person, overwrite=overwrite)
        await personal_channel.set_permissions(member_role, read_messages=False)
        await ctx.send('Channel created !')
        time = await personal_channel.send('[time]')
        for i in range(seconds, 0, -1) :
            if i == 1 :
                await personal_channel.delete()
            else :
                await time.edit(content='This channel will be deleted in ' + str(i) + ' seconds or ' + str(round(i / 3600, 1)) + ' hours.') 
    else:
        await ctx.channel.send(f'To use this command, You need to write it in {create.mention}')

@bot.command()
async def add_voice_channel(ctx, name: str, person: discord.Member):
    create = bot.get_channel(736612058480508998)
    if ctx.channel == create :
        seconds = 3600
        time_m = seconds / 60
        time_h = time_m / 60
        category_name = 'personal-channels'
        category = discord.utils.get(ctx.guild.categories, name=category_name)
        personal_channel = await ctx.guild.create_voice_channel(f'{name}', category=category) 
        await personal_channel.set_permissions(person, read_messages=True, send_messages=True)
        await ctx.send('Channel created !')
        for i in range(seconds, 0, -1) :
            if i == 1 :
                await personal_channel.delete()
            else :
                await time.edit(content='This channel will be deleted in ' + str(i) + ' seconds or ' + str(i / 3600) + ' hours.') 
    else:
        await ctx.channel.send(f'To use this command, You need to write it in {create.mention}')

'''@bot.command()
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
        await ctx.channel.send(f'To use this command, You need to write it in {create.mention}')'''
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
        await DM.send("Hey there ! your request id is `" + str(message_embed.id) + "`" + "\n" + "To see the freelancers who want to work for you type \"`>freelancers_list " + str(message_embed.id) + " `\"\nTo delete your request send a message to <@449327117885505550>")
    else :
        request_color_1 = check_skip.content.replace("#", "0x")
        request_color_2 = int(request_color_1, 16)
        channel = bot.get_channel(735222904530141244)
        embed = discord.Embed(title =  title.content, description = 'Request by ' + ctx.message.author.mention + '\n' + content.content + "\nFreelancers needed are : " + mentions.content, color = request_color_2)
        message_embed = await channel.send(embed=embed)
        await message_embed.add_reaction('✅')
        DM = await ctx.message.author.create_dm()
        await DM.send("Hey there ! your request id is `" + str(message_embed.id) + "`" + "\n" + "To see the freelancers who want to work for you type \"`>freelancers_list " + str(message_embed.id) + " `\"\nTo delete your request send a message to <@449327117885505550>")

@bot.command()
async def time(ctx, type: str, time: str = None):
    if type == 'help' :
        embed = discord.Embed(title = '**Timezones available**', description = 'For timezone conversion visit this website : <https://www.thetimezoneconverter.com/>', colour= 0x55B4B0)
        embed.set_image(url='https://www.timetemperature.com/time-zone-maps/expanded-world-time-zone-map.gif')
        await ctx.channel.send(embed=embed)
        with open("timezones.txt", "rb") as file:
            await ctx.send(file=discord.File(file, "timezones.txt"))
    elif type == 'full_timezone_name':
        fmt = '%H:%M:%S %Z%z'
        timezone_full = timezone(time)
        await ctx.channel.send(datetime.now(timezone_full).strftime(fmt))
    elif type == 'alias':
        fmt = '%H:%M:%S %Z%z'
        tz = pytz.country_timezones(time)
        await ctx.channel.send('You will receive a message in your DM !')
        for x in range(len(tz)) :
            DM = await ctx.message.author.create_dm()
            timezone_eg = tz[x]
            await DM.send('Time in ' + timezone_eg + ' : ' + datetime.now(timezone(timezone_eg)).strftime(fmt))
            
@bot.command()
async def freelancers_list(ctx, id: int):
    channel_name = bot.get_channel(735222904530141244)
    msg = await channel_name.fetch_message(id)
    reaction = msg.reactions[0]
    users = await reaction.users().flatten()
    the_manager_id = '<@449327117885505550>'
    DM = await ctx.message.author.create_dm()
    await DM.send("The users who want to work for you are : ")
    for x in range(1,len(users)): 
        await DM.send(str(users[x].mention))
    await DM.send( "\nRequest ID : " + str(id) + "\nFor hireing the freelancers DM them or talk with them on a private channel in the server \nFor help, just DM " + str(the_manager_id) + " or ping him in the server to talk to him.\nRequest preview : ")
    await DM.send(embed=msg.embeds[0])

'''@bot.command()
async def delete_request(ctx, id: int):
    db = TinyDB('DB/db.json')
    request_author = ctx.message.author
    request_author_id = ctx.message.author.id
    User = Query()
    check_user = db.search(User.id == request_author_id)
    await ctx.channel.send('Requests : ' + json.dumps(check_user[0]["requests"]))
    await ctx.channel.send('Request sent by ' + request_author.mention + ' with the ID ' + str(request_author_id))
    if check_user == []:
        await ctx.channel.send('The user who made the request ***does not*** exist in the db')
        await ctx.channel.send('Adding the user to the database...')
        db.insert({'id': request_author_id, 'requests': 0})
    else:
        await ctx.channel.send('This user ***does*** exist in the database')
        await ctx.channel.send('User requests : ' + check_requests)
        channel_name = bot.get_channel(735222904530141244)
    msg = await channel_name.fetch_message(id)
    await msg.delete()
    await ctx.channel.send('Request deleted !')'''
    #just ask the manager to delete your request, the next update we'll fix this issue

@bot.command()
async def colors(ctx):
    embed = discord.Embed(title = "Some nice colors :", description = "#b62828 \n #d57211 \n #ffce00 \n #ffee2d \n #36395a \n ***For reviewing the colors type \'>review_color\' and type the hex code*** \n EX : >review_color #d57211 \n for more hex colors check out : https://www.w3schools.com/Colors/colors_picker.asp", color = 0xb62828)
    await ctx.send(embed=embed)

'''@bot.command()
async def profile(ctx, value:str):
    db = TinyDB('DB/db.json')
    db.insert({'user': 1, 'char': value})
    User = Query()
    json_result = db.search(User.user == 1)
    await ctx.channel.send(json_result)
    string_result = json.dumps(json_result) 
    await ctx.channel.send(string_result)
    r = json_result[0]
    await ctx.channel.send(r["user"])'''

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
async def commands(ctx):
    id = '<@449327117885505550>'
    embed = discord.Embed(title = "INFO :", description = f"I am a bot created by {id} \n I manage this server and organise it \n If you want a bot like it just contact {id} in the DM or ping him in the chat \n ***The commands are : *** \n**>add_text_channel**\n**>add_voice_channel**\n**>request**\n**>freelancers_list**\n**>delete_request**\n**>colors**\n**>review_color**\n**>commands**\n**>documentation**", color = 0x00ff00)
    await ctx.send(embed=embed)

@bot.command()
async def documentation(ctx):
    id = '<@449327117885505550>'
    embed = discord.Embed(title = "INFO :", description = f"I am a bot created by {id} \n I manage this server and organise it \n If you want a bot like it just contact {id} in the DM or ping him in the chat \n ***The commands and their job : *** \n ¤¸¸.•´¯`•¸¸.•..>> ☵ <<..•.¸¸•´¯`•.¸¸¤¸¸.•´¯`•¸¸.•..>> ☵ <<..•.¸¸•´¯`•.¸¸¤ \n **>add_text_channel <channel name> <user>\nThis command adds a __text__ channel and makes the person that you mention and yourself the only user who can see and enter it.**", color = 0xDD4124)
    await ctx.send(embed=embed)
'''@bot.command()
async def help(ctx):
    embed = discord.Embed(title = "The bot commands are :", description = "- >add (first number) (second number) \n adds two numbers\n - >devise \n - >multiply \n - >substract \n - >add_custom_text_channel", color = 0xb62828)
    await ctx.send(embed=embed)'''

bot.run(TOKEN)
''' if message.content.startswith('add text channel'):
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
        await message.channel.send('channel created !')'''
