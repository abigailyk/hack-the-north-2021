# Import Discord Package (pip install python)
import discord

from discord.ext import commands

# Client (our bot)
#client = discord.Client()
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    # RUN COMMANDS
    #general_channel = client.get_channel(886724634534354966)
    print('i am prepared for this')
    #await general_channel.send('beep booper is ready')

@client.command()
async def test(ctx):
    # RUN COMMANDS
    embed = discord.Embed(title = " Ping:", description = f"Pong! {round(client.latency * 1000)}ms")

    await ctx.channel.send(embed = embed)
    #ping = get(ctx.guild.members, name = 'AcquaSerene')
    #response = f'Suck my pp {ping.mention}'
    #await general_channel.send(response)

@client.command()
async def parrot(ctx, *, arg):
    await ctx.send(arg)


@client.event
async def on_message(message):

    if message.content.lower() == 'play "fly me to the moon" by frank sinatra':
        general_channel = client.get_channel(886724634534354966)
        response = f'Nah fric you {message.author.mention}'
        await general_channel.send(response)

# Run the client on the server
client.run('ODg4NjMwNTM1MTg0ODcxNDU2.YUVfrQ.ddMzTWNOYFX59z0RRWSCGpCj1Cc')