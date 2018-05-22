                                                "https://media1.tenor.com/images/fdafbad47d6a69cb5d3a90a8b9dff86f/tenor.gif?itemid=4936338",
                                                         "https://data.whicdn.com/images/284330063/original.gif"]))


    if message.content.lower().startswith('/coinflip'):
       await client.send_message(message.channel, random.choice(["Tails! :large_orange_diamond:",
                                                                "Heads! :large_blue_diamond:",
                                                                "Heads! :large_blue_diamond:",
                                                                "Tails! :large_orange_diamond:",
                                                                "Tails! :large_orange_diamond:",
                                                                "Heads! :large_blue_diamond:"]))
    if message.content.lower().startswith("/say"):
        variable = message.content[len('/say'):].strip()
        await client.send_message(message.channel, variable)
        await client.delete_message(message)
    
    if message.content.lower().startswith("/rage"):
        await client.send_message(message.channel, random.choice(["(ノ ゜Д゜)ノ ︵ ┻━┻",
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
        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('/server'):
        embed = discord.Embed(title="Fun Channel", url="https://discord.gg/T5Q7C5Q", color=0x4afbf7)
        embed.set_author(name="Server Details", icon_url="https://cdn.discordapp.com/attachments/347362023828488192/441064604366405642/Dab.png")
        embed.add_field(name="Welcome!", value="Fun channel as the name suggests is where we have fun! feel free to talk and chat to people! <3", inline=True)
        embed.add_field(name="Rules", value="We follow simple rules and simple rule system to fully know these rules please read #information this channel will also provide more information about the server!", inline=True)
        embed.add_field(name="What is the purpose of this server?", value="Honestly, Even myself can't answer that :P This server was originally made because of me being bored however i never intended to have this community yet even if its still a *smol* community i still love it and thank all the people who made this server alive <3", inline=True)
        embed.add_field(name="What is the server about?", value="This server is about gaming, however we can still talk about other stuff if you wish, This server provides and accepts everything! So feel free to talk about whatever topic you want!", inline=True)
        embed.add_field(name="Who made this?", value="*100%* not Cupquake123#2042", inline=True)
        embed.set_footer(text="Fun Channel")
        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('/apply'):
        embed = discord.Embed(color=0xb1fcf4)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/347362023828488192/446892855609262080/Dab.png")
        embed.add_field(name="Staff Application Fourm", value="Fun Channel", inline=False)
        embed.add_field(name="Apply now!", value="https://goo.gl/forms/9SF8PtdpudF3dfqr1", inline=True)
        await client.send_message(message.channel, embed=embed)
    
    
    if message.content.lower().startswith('/socialmedia'):
        embed = discord.Embed(title="Social Media", color=0x78f5d0)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/438864185976291342/443230701974978561/kotori_pfp.png")
        embed.add_field(name="Twitter", value="https://twitter.com/abbyplays123", inline=False)
        embed.add_field(name="Youtube", value="http://bit.ly/2tM7TNC", inline=True)
        embed.add_field(name="Discord", value="https://discord.gg/T5Q7C5Q", inline=True)
        embed.add_field(name="My Anime List", value="https://myanimelist.net/profile/AbbyCakez", inline=False)
        embed.set_footer(text="Cake Bot | Fun Channel")
        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('/links'):
        embed = discord.Embed(title="Social Media", color=0x78f5d0)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/438864185976291342/443230701974978561/kotori_pfp.png")
        embed.add_field(name="Twitter", value="https://twitter.com/abbyplays123", inline=False)
        embed.add_field(name="Youtube", value="http://bit.ly/2tM7TNC", inline=True)
        embed.add_field(name="Discord", value="https://discord.gg/T5Q7C5Q", inline=True)
        embed.add_field(name="My Anime List", value="https://myanimelist.net/profile/AbbyCakez", inline=False)
        embed.set_footer(text="Cake Bot | Fun Channel")
        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('/invite'):
        embed=discord.Embed(color=0xf0ea6c)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/347362023828488192/446892855609262080/Dab.png")
        embed.add_field(name="Discord Invite Link", value="https://discord.gg/T5Q7C5Q", inline=False)
        await client.send_message(message.channel, embed=embed)

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
 
            await client.send_message(message.channel, embed=userembed)
        except IndexError:
            await client.send_message(message.channel, "Couldn't find user! Mention the user you want to check!")
        except:
            await client.send_message(message.channel, "An error as occured! Try again later.")
        finally:
            pass

    if match("<@!?435379055253127178>", message.content) is not None:
        await client.send_message(message.channel,"Hi {0.author.mention} i'm ᴄᴀᴋᴇ ʙᴏᴛ nice to meet you! I'm ran and made by cupcake!".format(message))
    

    if 'ᴄᴀᴋᴇ' in message.content:
        await client.send_message(message.channel, '/help')


    if message.content.startswith('/dab'):
        await client.send_message(message.channel, "<o/")
        await client.delete_message(message)
    
    if client.user.id != message.author.id:
        if 'anime is shit' in message.content.lower():
            await client.send_message(message.channel, 'no u {0.author.mention}'.format(message))

    if client.user.id != message.author.id:
        if 'anime is sht' in message.content.lower():
            await client.send_message(message.channel, 'no u {0.author.mention}'.format(message))

    if client.user.id != message.author.id:
        if 'anime is bad' in message.content.lower():
            await client.send_message(message.channel, 'no u {0.author.mention}'.format(message))

    if client.user.id != message.author.id:
        if 'fk anime' in message.content.lower():
            await client.send_message(message.channel, 'no u {0.author.mention}'.format(message))

    if client.user.id != message.author.id:
        if 'fuck anime' in message.content.lower():
            await client.send_message(message.channel, 'no u {0.author.mention}'.format(message))


    if client.user.id != message.author.id:
        if 'no u' in message.content.lower():
            await client.send_message(message.channel, 'no u {0.author.mention}'.format(message))
    
    if client.user.id != message.author.id:
        if 'anime suck' in message.content.lower():
            await client.delete_message(message)
            await client.send_message(message.channel, 'no u {0.author.mention}'.format(message))

    if client.user.id != message.author.id.lower():
        if 'gay' in  message.content.lower():
            await client.send_message(message.channel, 'no u {0.author.mention}'.format(message))    
           

    if client.user.id != message.author.id:
        if 'gey' in message.content.lower():
            await client.send_message(message.channel, 'no u {0.author.mention}'.format(message))
    
    if client.user.id != message.author.id:
        if '<o/' in message.content.lower():
            await client.send_message(message.channel, 'YA YEET <o/ {0.author.mention}'.format(message))

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, id="365737396781973504")
    await client.add_roles(member, role)



















    


              

        
    


         


  




        
    

    
    



   
client.run(str(os.environ.get('BOT_TOKEN')))



















