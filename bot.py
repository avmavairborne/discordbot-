import discord 
from discord.ext import commands 
import random 


#commmand 
client = commands.Bot(command_prefix='[chosen command')
# for the embed 
@client.command(name='embed')
async def  embed (context):
    myEmbed = discord.Embed(title='[title of the embed]', description='[description of the embed]',color=0x00ff00)
    myEmbed.add_field(name = '[additional stuff]',value = '[additional stuff]',inline = True)
    myEmbed.add_field(name='[additional stuff]', value = '[additional stuff]',inline= True)
    # repeat the above line according to your prefrence
    myEmbed.set_footer(text='[footer of the embed]')
    myEmbed.set_author(name = '[author of the embed]')
    await context.message.channel.send(embed=myEmbed)


#kick command 
@client.command(name='kick',pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick (context,member:discord.Member):
    await member.kick()
    await context.send('user '  +member.display_name+ ' has been kicked')



#ban command 
@client.command(name='ban',pass_context= True)
@commands.has_permissions(kick_members=True)
async def ban (context,member:discord.Member,*,reason=None):
    await member.ban(reason=reason)
    await context.send('user '  +member.display_name+ ' has been banned')

#for pictures 
@client.command(name='command for pictures')
async def meme(context):
    images = ['path of the image tou want to send ']
    random_image=random.choice(images)
    await context.send(file=discord.File(random_image))


#for giphy images 
@client.command(name='command for giphy image ')
async def meme(context):
     images =['path of giphy image']
     random_image=random.choice(images)
     await context.send(file=discord.File(random_image))

 
#replying to messages 
@client.event
async def on_message(message):
    if message.content == "messgae":
        general_channel = client.get_channel(text channel ID)
        await general_channel.send('reply')
    if message.content=="message":
        general_channel = client.get_channel(text channel ID)
        await general_channel.send('reply')
    if message.content=='message':
        general_channel = client.get_channel(text channel ID)
        await general_channel.send('reply')
    if message.content=='message':
        general_channel = client.get_channel(text channel ID)
        await general_channel.send('reply')
    #repeat for as many message as you want
#replying to dms 
    if message.content=='message':
        await message.author.send('reply')
    if message.content =='message':
        await message.author.send('reply')
    if message.content=='message':
        await message.author.send('reply')
    if message.content=='message':
        await message.author.send('reply')
    
    await client.process_commands(message)

   # repeat for as many messages as you want 
  
 #displaying status 
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,activity=discord.Game('staus you want to display'))
   # link with the application 

client.run("enter client ID")
