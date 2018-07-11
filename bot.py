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
from urllib.parse import urlparse
from discord.ext import commands
import re



bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print(bot.user.id)
    print("Bot is ready and connected to discord")
    await bot.change_presence(game=discord.Game(name="Life is joke", type=3))

#Fun Commands!

@bot.event
async def on_message(message):    
    if message.content.lower().startswith('/8ball'):
      await bot.send_message(message.channel, random.choice(["It is decidedly so :8ball:",
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
                                                              "Yes your gay, Wait what? that wasn't the question? Well uh just letting ya know."]))                                         
                                                          
    if message.content.lower().startswith("/gif"):
        await bot.send_message(message.channel, random.choice(["https://media0.giphy.com/media/f4V2mqvv0wT9m/giphy.gif",
                                                         "https://media.giphy.com/media/4QxQgWZHbeYwM/giphy.gif",
                                                         "https://thumbs.gfycat.com/OblongRapidAvocet-size_restricted.gif",
                                                         "https://media1.tenor.com/images/445c3de1f9a6a87694bcbb2739d35451/tenor.gif?itemid=8312712",
                                                         "https://i.pinimg.com/originals/b6/5c/5e/b65c5e33a54a2468a6e9f6e119cdaf9f.gif",
                                                         "https://i.imgur.com/M3BG3Ck.gif",
                                                         "http://i0.kym-cdn.com/photos/images/newsfeed/001/087/562/93c.gif",
                                                         "http://i.imgur.com/0jAef66.gif",
                                                         "https://thumbs.gfycat.com/InfatuatedUnrulyGyrfalcon-max-1mb.gif",
                                                         "https://i.gifer.com/Jn9R.gif",
                                                         "https://i.pinimg.com/originals/63/78/68/6378684a9a66f479c952d1ee1e854bd9.gif",
                                                         "https://media.giphy.com/media/gnvlmIRPzVnGM/giphy.gif",
                                                         "https://i.pinimg.com/originals/29/91/7a/29917a5226ee8f1ef08a4a2e6afde524.gif",
                                                         "https://78.media.tumblr.com/8a1e120208a2d5b9d73ac9d3131d2fa2/tumblr_obrs3lLMna1s5f9ado2_500.gif",
                                                         "https://78.media.tumblr.com/399259fe9dcae09a36f7ee4d35f7b514/tumblr_okt2l5Khy31tydz8to1_500.gif",
                                                         "https://media1.tenor.com/images/9a64d7e66082895dfd26872e1929631a/tenor.gif?itemid=6062473",
                                                         "https://media1.tenor.com/images/694927eede67ccf45f2601b9c2aad98b/tenor.gif?itemid=5401519",
                                                         "https://media1.tenor.com/images/9db3300382b4692e3aa95164161ab2e8/tenor.gif?itemid=9188406",
                                                         "https://thumbs.gfycat.com/LegalMiniatureChihuahua-size_restricted.gif",
                                                         "https://media1.tenor.com/images/80a38c215bcde77ab897d1bea3c7bf96/tenor.gif?itemid=6078924",
                                                         "https://vignette.wikia.nocookie.net/love-live/images/6/65/KoiAqua_Hanamaru.gif/revision/latest?cb=20160712080936",
                                                         "https://media1.tenor.com/images/bea0139e175637da295b61164a8e33c2/tenor.gif?itemid=7222980",
                                                         "https://media.giphy.com/media/ZLr299JYCUEHm/giphy.gif",
                                                         "https://media1.tenor.com/images/fcc16d68c200fd0ff17e6e27978fb6c3/tenor.gif?itemid=7552283",
                                                         "https://media1.tenor.com/images/831c64bcece59befbe6157bbb3a9f0fe/tenor.gif?itemid=7817206",
                                                         "https://media1.tenor.com/images/fdafbad47d6a69cb5d3a90a8b9dff86f/tenor.gif?itemid=4936338",
                                                         "https://data.whicdn.com/images/284330063/original.gif"]))


        
    if message.content.lower().startswith('/coinflip'):
       await bot.send_message(message.channel, random.choice(["Tails! :large_orange_diamond:",
                                                                "Heads! :large_blue_diamond:",
                                                                "Heads! :large_blue_diamond:",
                                                                "Tails! :large_orange_diamond:",
                                                                "Tails! :large_orange_diamond:",
                                                                "Heads! :large_blue_diamond:"]))
    if message.content.lower().startswith("/say"):
            variable = message.content[len('/say'):].strip()
            await bot.delete_message(message)
            await bot.send_message(message.channel, variable)
            
        
    
    if message.content.lower().startswith("/rage"):
        await bot.send_message(message.channel, random.choice(["(ノ ゜Д゜)ノ ︵ ┻━┻",
                                                                 "(╯°□°)╯︵ ┻━┻ ︵ ╯(°□° ╯)",
                                                                 "http://i39.tinypic.com/kd0rk4.jpg",
                                                                 "http://cdn.playbuzz.com/cdn/ee40bd70-7e8d-4a83-b492-0aa7ee791f76/4ae7d4fd-3ea3-4d4a-8d37-f2c726480e72.jpg",
                                                                 "http://www.ragefaces.memesoftware.com/faces/large/neutral-suspicious-l.png",]))

    if message.content.lower().startswith('/help'):
        embed=discord.Embed(color=0xf4ea60)
        embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1508719360/_animepaper.net_avatar-box-anime-k-on_-i-love-my-music-mio-195545-wonderngo-medium-6c54be5d.jpg")
        embed.add_field(name="Hi! I'm cake bot", value="I'm a bot made for a server called fun channel!", inline=True)
        embed.add_field(name="My Commands", value="my prefix is = /", inline=True)
        embed.add_field(name="Help" , value="This (Duh)", inline=False)
        embed.add_field(name="Links" , value="My Master's Social links! (Be sure to follow!)", inline=True)
        embed.add_field(name="User" , value="Shows a user's information", inline=True)
        embed.add_field(name="8Ball" , value="Predicts everything and anything", inline=False)
        embed.add_field(name="Coinflip" , value="Flips you a majestic coin", inline=True)
        embed.add_field(name="Say" , value="Copies what you say!", inline=False)
        embed.add_field(name="Dab", value="Ehm.. <o/", inline=True)
        embed.add_field(name="Rage" , value="Sends a random rage picture", inline=False)
        embed.add_field(name="Gif" , value="Random anime gifs", inline=True)
        embed.add_field(name="Invite" , value="Shows the server's invite link!", inline=False)
        embed.set_footer(text="Many more commands to come! | Fun Channel")
        await bot.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('/server'):
        embed = discord.Embed(title="Fun Channel", url="https://discord.gg/T5Q7C5Q", color=0x4afbf7)
        embed.set_author(name="Server Details", icon_url="https://cdn.discordapp.com/attachments/347362023828488192/441064604366405642/Dab.png")
        embed.add_field(name="Welcome!", value="Fun channel as the name suggests is where we have fun! feel free to talk and chat to people! <3", inline=True)
        embed.add_field(name="Rules", value="We follow simple rules and simple rule system to fully know these rules please read #information this channel will also provide more information about the server!", inline=True)
        embed.add_field(name="What is the purpose of this server?", value="Honestly, Even myself can't answer that :P This server was originally made because of me being bored however i never intended to have this community yet even if its still a *smol* community i still love it and thank all the people who made this server alive <3", inline=True)
        embed.add_field(name="What is the server about?", value="This server is about gaming, however we can still talk about other stuff if you wish, This server provides and accepts everything! So feel free to talk about whatever topic you want!", inline=True)
        embed.add_field(name="Who made this?", value="*100%* not Cupquake123#2042", inline=True)
        embed.set_footer(text="Fun Channel")
        await bot.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('/apply'):
        embed = discord.Embed(color=0xb1fcf4)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/347362023828488192/446892855609262080/Dab.png")
        embed.add_field(name="Staff Application Fourm", value="Fun Channel", inline=False)
        embed.add_field(name="Apply now!", value="https://goo.gl/forms/9SF8PtdpudF3dfqr1", inline=True)
        await bot.send_message(message.channel, embed=embed)
    
    
    if message.content.lower().startswith('/socialmedia'):
        embed = discord.Embed(title="Social Media", color=0x78f5d0)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/438864185976291342/443230701974978561/kotori_pfp.png")
        embed.add_field(name="Twitter", value="https://twitter.com/abbyplays123", inline=False)
        embed.add_field(name="Youtube", value="http://bit.ly/2tM7TNC", inline=True)
        embed.add_field(name="Discord", value="https://discord.gg/T5Q7C5Q", inline=True)
        embed.add_field(name="My Anime List", value="https://myanimelist.net/profile/AbbyCakez", inline=False)
        embed.set_footer(text="Cake Bot | Fun Channel")
        await bot.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('/links'):
        embed = discord.Embed(title="Social Media", color=0x78f5d0)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/347362023828488192/457009454521778176/profile.png")
        embed.add_field(name="Twitter", value="https://twitter.com/abbyplays123", inline=False)
        embed.add_field(name="Youtube", value="http://bit.ly/2tM7TNC", inline=True)
        embed.add_field(name="Discord", value="https://discord.gg/pQDbbx9", inline=True)
        embed.add_field(name="My Anime List", value="https://myanimelist.net/profile/AbbyCakez", inline=False)
        embed.set_footer(text="Cake Bot | Fun Channel")
        await bot.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('/invite'):
        embed=discord.Embed(color=0xf0ea6c)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/347362023828488192/446892855609262080/Dab.png")
        embed.add_field(name="Discord Invite Link", value="https://discord.gg/pQDbbx9", inline=False)
        await bot.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('/user'):
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
 
            await bot.send_message(message.channel, embed=userembed)
        except IndexError:
            await bot.send_message(message.channel, "Couldn't find user! Mention the user you want to check!")
        except:
            await bot.send_message(message.channel, "An error as occured! Try again later.")
        finally:
            pass

    if match("<@!?435379055253127178>", message.content) is not None:
        await bot.send_message(message.channel,"Hi {0.author.mention} i'm Cake Bot nice to meet you! I'm ran and made by cupcake!".format(message))


    if message.content.lower().startswith('/dab'):
        await bot.send_message(message.channel, "<o/")
        await bot.delete_message(message)
    
    if bot.user.id != message.author.id:
        if 'anime is shit' in message.content.lower():
            await bot.send_message(message.channel, 'no u {0.author.mention}'.format(message))

    if bot.user.id != message.author.id:
        if 'anime is sht' in message.content.lower():
            await bot.send_message(message.channel, 'no u {0.author.mention}'.format(message))

    if bot.user.id != message.author.id:
        if 'anime is bad' in message.content.lower():
            await bot.send_message(message.channel, 'no u {0.author.mention}'.format(message))

    if bot.user.id != message.author.id:
        if 'fk anime' in message.content.lower():
            await bot.send_message(message.channel, 'no u {0.author.mention}'.format(message))

    if bot.user.id != message.author.id:
        if 'fuck anime' in message.content.lower():
            await bot.send_message(message.channel, 'no u {0.author.mention}'.format(message))


    if bot.user.id != message.author.id:
        if 'no u' in message.content.lower():
            await bot.send_message(message.channel, 'no u {0.author.mention}'.format(message))
    
    if bot.user.id != message.author.id:
        if 'anime suck' in message.content.lower():
            await bot.delete_message(message)
            await bot.send_message(message.channel, 'no u {0.author.mention}'.format(message))
  

    if bot.user.id != message.author.id:
        if ':thinking:' in message.content.lower():
            await bot.send_message(message.channel, ':thinking: THINKING INTENSIFIES {0.author.mention}'.format(message))
      
    if message.content.lower().startswith('/role'):
        user = message.author
        role = discord.utils.get(user.server.roles, id="449884167271088141")
        if "395085021721133057" in [role.id for role in message.author.roles]:
            await bot.add_roles(user, role)
            await bot.add_reaction(message, "👍")
            delete = await bot.send_message(message.channel, "Success! You now have grammar nazi role!")
            await bot.delete_message(delete)
        else:
            await bot.send_message(message.channel, "You need to be level 30+ to be able to this command!")
            await bot.delete_message(message)

    if message.content.lower().startswith('/punish'):
        role = discord.utils.get(message.server.roles,id='420576440111726592') 
        if "340682622932090890" in [role.id for role in message.author.roles]:
            await bot.add_roles(message.mentions[0], role)
            await bot.send_message(message.channel, "Successfully punished!")
        else:
            await bot.send_message(message.channel, "You do not have permissions to do this command")

    if message.content.lower().startswith('/unpunish'):
        role = discord.utils.get(message.server.roles,id='420576440111726592') 
        if "340682622932090890" in [role.id for role in message.author.roles]:
            await bot.remove_roles(message.mentions[0], role)
            await bot.send_message(message.channel, "Successfully unpunished")
        else:
            await bot.send_message(message.channel, "You do not have permissions to do this command!")

    if message.content.lower().startswith('poll:'):
        await bot.add_reaction(message, "👍")
        await bot.add_reaction(message, "👎")
        mention = await bot.send_message(message.channel, "@everyone")
        await bot.delete_message(mention)

    if message.content.lower().startswith("/poll"):
            variable = message.content[len('/poll'):].strip()
            await bot.delete_message(message)
            botmessage = await  bot.send_message(message.channel, variable)
            await bot.send_message(message.channel,"Asked by {0.author.mention}".format(message))
            await bot.add_reaction(botmessage,"💙")
            await bot.add_reaction(botmessage,"💜")
            await bot.add_reaction(botmessage,"💛")
            mention = await bot.send_message(message.channel, "@everyone")
            await bot.delete_message(mention)

    if message.content.lower().startswith('/suggest'):
        variable = message.content[len('/suggest'):].strip()
        channel = bot.get_channel("393357389606158347")
        botmsg = await bot.send_message(channel, variable)
        await bot.add_reaction(botmsg, "👍")
        await bot.add_reaction(botmsg, "👎")
        await bot.send_message(channel, "Suggested by {0.author.mention}".format(message))

    if message.content.lower().startswith('/kick'):
        await bot.kick(message.mentions[0])
        await bot.send_message(message.channel, "Succesfully kicked")

    if message.content.startswith('/statmsg'):
        await bot.send_typing(message.channel)
        mesg = await bot.send_message(message.channel, 'Calculating... this might take a while. 💜')
        counter = 0
        async for msg in bot.logs_from(message.channel, limit=9999999):
            if msg.author == message.author:
                counter += 1
        await bot.edit_message(mesg, '{} has {} messages in {}.'.format(message.author, str(counter), message.channel))
   
    if message.content.lower().startswith('/club'):
       embed = discord.Embed(color=0x51f79b)
       embed.add_field(name="Clubs!", value="To create a club simply register at https://goo.gl/forms/6XhLVh3f6aKm9cKu2 make sure you meet the requirements (as listed below) and you also agree on our rules.", inline=True)
       embed.add_field(name="Club Requirements", value="We have this to keep the clubs organized, active and fun!", inline=True)
       embed.add_field(name="- Club Must be PG", value="Keep it PG, Any NSFW Clubs will be automatically disbanded", inline=True)
       embed.add_field(name="- Club must have atleast 3 members", value="on making a club you require atleast 3 members to create your club so we don't have any clubs called 'Welcome to the club that has a long name because i have no friends' yeah...", inline=True)
       embed.add_field(name="- Club must the only subject", value="Ex. Anime club and weeb club, same subject this will make it so there's no dupe clubs of any sort", inline=True)
       embed.add_field(name="- Club Leader must be level 10+ while club members needs to be level 2+", value="To make sure clubs are active :D", inline=True)
       embed.add_field(name="=====CLUB RULES=====", value="Rules that EVERY club should follow!", inline=True)
       embed.add_field(name="1. Club Recuirtment", value="Now, i know you wanna spam everybody in the channel about your new club that you made with your friends! If you want to do that go #club-recruitment, however please do not spam general or spam people about your club or force them to join or this will lead to a punishment", inline=False)
       embed.add_field(name="AND MANY MORE RULES TO COME!", value="Yeah i ran out of ideas whachu gunna do about it ? ;3", inline=True)
       await bot.send_message(message.channel, embed=embed)
    
    


@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, id="365737396781973504")
    await bot.add_roles(member, role)
    msg = "Hi! {0} Welcome to {1}".format(member.mention, member.server.name)
    await bot.send_message(discord.Object(id='434605560382619650'), msg)


@bot.event
async def on_member_remove(member):
    msg = "Aw Leaving so soon? Cya later! {0}".format(member.mention)
    await bot.send_message(discord.Object(id='434605560382619650'), msg)





client.run(str(os.environ.get('BOT_TOKEN')))

    
   



















