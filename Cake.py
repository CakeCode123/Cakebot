#Cakebot by Abby 


import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import logging
from discord.utils import get
import datetime
from re import match
import json
import os.path
import os

Client = discord.Client()
client = commands.Bot(command_prefix = "/")

@client.event
async def on_ready():
    print(client.user.id)
    print("Bot is ready and connected to discord")
    await client.change_presence(game=discord.Game(name='with version 1.2 alpha'))
    #Fun!

@client.event
async def on_message(message):
    if message.content.upper().startswith('/HEWO'):
        if "437923291047526402" in [role.id for role in message.author.roles]: 
            await client.send_message(message.channel, "Nice!")
        else:
            await client.send_message(message.channel, "You do not have permissions to execute this command!") 
    if message.content.startswith('/8ball'):
      await client.send_message(message.channel, random.choice(["It is decidedly so :8ball:",
                                                              "Without a doubt :8ball:",
                                                              "Yes, definitely :8ball:",
                                                              "If you try hard then you will figure it out :8ball:",
                                                              "As I see it, yes :8ball:",
                                                              "Most likely :8ball:",
                                                              "Gomen'nasai i don't hanasu english, Try again later. :8ball:",
                                                              "Yes :8ball:",
                                                              "What? Are you a dumb? Of course! :8ball:",
                                                              "Well... I honestly don't know WHO DO YOU THINK I'AM?! :8ball:",
                                                              "Yes 100% :8ball:",
                                                              "Its better for you to not know. :8ball:",
                                                              "Hmm.. Yes :8ball:",
                                                              "Ask yourself. :8ball:",
                                                              "According to my calulations its a no :8ball:",
                                                              "Call 911, they let will let you know. :8ball:",
                                                              "My sources say no :8ball:",
                                                              "Outlook not so good :8ball:",
                                                              "Your IQ is too low for this question, Try another one :8ball:",
                                                              "Why are you asking me?! Ask google! :8ball:",
                                                              "Instant deny!:8ball:",
                                                              "NO! JUST NO.:8ball:",
                                                              "Invalid Question.exe"]))   
    if message.content.startswith('/coinflip'):
       await client.send_message(message.channel, random.choice(["Tails! :large_orange_diamond:",
                                                                "Heads! :large_blue_diamond:",
                                                                "Heads! :large_blue_diamond:",
                                                                "Tails! :large_orange_diamond:",
                                                                "Tails! :large_orange_diamond:",
                                                                "Heads! :large_blue_diamond:"]))
    if message.content.startswith("/say"):
        variable = message.content[len('/say'):].strip()
        await client.send_message(message.channel, variable)
        await client.delete_message(message)
    
    if message.content.startswith("/rage"):
        await client.send_message(message.channel, random.choice(["(ノ ゜Д゜)ノ ︵ ┻━┻",
                                                                 "(╯°□°)╯︵ ┻━┻ ︵ ╯(°□° ╯)",
                                                                 "http://i39.tinypic.com/kd0rk4.jpg",
                                                                 "http://cdn.playbuzz.com/cdn/ee40bd70-7e8d-4a83-b492-0aa7ee791f76/4ae7d4fd-3ea3-4d4a-8d37-f2c726480e72.jpg",
                                                                 "http://www.ragefaces.memesoftware.com/faces/large/neutral-suspicious-l.png",]))

    if message.content.startswith('/help'):
        embed = discord.Embed(title="Guide", description="Hi i'm cake bot and i'm made by Cupquake123#2042! ", color=0xfcf467)
        embed.set_author(name="Cupquake123#2042", url="https://bit.ly/2xDvi4x", icon_url="https://pbs.twimg.com/profile_images/974402424071794688/Q2Sq6RPO_400x400.jpg")
        embed.add_field(name="Commands", value="My commands are", inline=False)
        embed.set_footer(text="/8ball - /coinflip - /say - /rage - /user - /dab - /server - /links")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('/server'):
        embed = discord.Embed(title="Fun Channel", url="https://discord.gg/T5Q7C5Q", color=0x4afbf7)
        embed.set_author(name="Server Details", icon_url="https://cdn.discordapp.com/attachments/347362023828488192/441064604366405642/Dab.png")
        embed.add_field(name="Welcome!", value="Fun channel as the name suggests is where we have fun! feel free to talk and chat to people! <3", inline=True)
        embed.add_field(name="Rules", value="We follow simple rules and simple rule system to fully know these rules please read #information this channel will also provide more information about the server!", inline=True)
        embed.add_field(name="What is the purpose of this server?", value="Honestly, Even myself can't answer that :P This server was originally made because of me being bored however i never intended to have this community yet even if its still a *smol* community i still love it and thank all the people who made this server alive <3", inline=True)
        embed.add_field(name="What is the server about?", value="This server is about gaming, however we can still talk about other stuff if you wish, This server provides and accepts everything! So feel free to talk about whatever topic you want!", inline=True)
        embed.add_field(name="Who made this?", value="*100%* not Cupquake123#2042", inline=True)
        embed.set_footer(text="Fun Channel")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('/links'):
        embed = discord.Embed(title="Social Media", color=0x78f5d0)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/438864185976291342/443230701974978561/kotori_pfp.png")
        embed.add_field(name="Twitter", value="https://twitter.com/abbyplays123", inline=False)
        embed.add_field(name="Youtube", value="http://bit.ly/2tM7TNC", inline=True)
        embed.add_field(name="Discord", value="https://discord.gg/T5Q7C5Q", inline=True)
        embed.add_field(name="My Anime List", value="https://myanimelist.net/profile/AbbyCakez", inline=False)
        embed.set_footer(text="Cake Bot | Fun Channel")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('/socialmedia'):
        embed = discord.Embed(title="Social Media", color=0x78f5d0)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/438864185976291342/443230701974978561/kotori_pfp.png")
        embed.add_field(name="Twitter", value="https://twitter.com/abbyplays123", inline=False)
        embed.add_field(name="Youtube", value="http://bit.ly/2tM7TNC", inline=True)
        embed.add_field(name="Discord", value="https://discord.gg/T5Q7C5Q", inline=True)
        embed.add_field(name="My Anime List", value="https://myanimelist.net/profile/AbbyCakez", inline=False)
        embed.set_footer(text="Cake Bot | Fun Channel")
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith('/user'):
        try:
            user = message.mentions[0]
            userjoinedat = str(user.joined_at).split('.', 1)[0]
            usercreatedat = str(user.created_at).split('.', 1)[0]
 
            userembed = discord.Embed(
                title="Username:",
                description=user.name,
                color=0xe67e22
            )
            userembed.set_author(
                name="User Info"
            )
            userembed.add_field(
                name="Joined the server at:",
                value=userjoinedat
            )
            userembed.add_field(
                name="User Created at:",
                value=usercreatedat
            )
            userembed.add_field(
                name="Discriminator:",
                value=user.discriminator
            )
            userembed.add_field(
                name="User ID:",
                value=user.id
            )
 
            await client.send_message(message.channel, embed=userembed)
        except IndexError:
            await client.send_message(message.channel, "Couldn't find user! Mention the user you want to check!")
        except:
            await client.send_message(message.channel, "An error as occured! Try again later.")
        finally:
            pass
    if match("<@!?435379055253127178>", message.content) is not None:
        text = await client.send_message(message.channel, "**Baking a cake**")

        


        await client.edit_message(text, "Hi {0.author.mention} i'm cake bot nice to meet you! do /help for more details!".format(message))

    if message.content.startswith('/dab'):
        await client.send_message(message.channel, "<o/")
        await client.delete_message(message)

    if match("<@!?33758026412370649601>", message.content) is not None:
        await client.delete_message(message)
        await client.send_message(message.channel, "OI! {0.author.mention} That's not allowed! My Master is in do not distrub mode! Don't bother my master!".format(message))
    
    if message.content.startswith('anime is shit'):
        await client.delete_message(message)
        await client.send_message(message.channel, "no u {0.author.mention}".format(message))

    if message.content.startswith('anime is sht'):
        await client.delete_message(message)
        await client.send_message(message.channel, "no u {0.author.mention}".format(message))

    if message.content.startswith('anime is bad'):
        await client.delete_message(message)
        await client.send_message(message.channel, "no u {0.author.mention}".format(message))

    if message.content.startswith('fk anime'):
        await client.delete_message(message)
        await client.send_message(message.channel, "no u {0.author.mention}".format(message))

    if message.content.startswith('anime is gud'):
        await client.delete_message(message)
        await client.send_message(message.channel, "Very naice <3 Ofc it is {0.author.mention}".format(message))
    
    if message.content.startswith('anime sucks'):
        await client.delete_message(message)
        await client.send_message(message.channel, "no u {0.author.mention}".format(message))

    if message.content.startswith('anime sucks'):
        await client.delete_message(message)
        await client.send_message(message.channel, "no u {0.author.mention}".format(message))
    
      
    if client.user.id != message.author.id:
        if 'gay' in message.content:
            await client.send_message(message.channel, 'ur gayer {0.author.mention}'.format(message))

    if client.user.id != message.author.id:
        if 'Gay' in message.content:
            await client.send_message(message.channel, 'ur gayer {0.author.mention}'.format(message))

    if client.user.id != message.author.id:
        if 'Gey' in message.content:
            await client.send_message(message.channel, 'ur gayer {0.author.mention}'.format(message))
    

    if client.user.id != message.author.id:
        if 'GEY' in message.content:
            await client.send_message(message.channel, 'ur geyer {0.author.mention}'.format(message))

@client.event
async def on_member_join(member):
    server = member.server 
    for user in server.members:
        if user.server_permissions.administrator:
            await client.send_message(user, "A new member has joined fun channel! :3")
            await client.send_message(discord.Object(id='347362023828488192'), 'Welcome to fun channel!, ')


    
            

    


              

        
    


         


  




        
    

    
    



   
client.run("NDM1Mzc5MDU1MjUzMTI3MTc4.Dd1NTw.G-9AdRdO_40_F0ch4tQwPbM3k-o")



















