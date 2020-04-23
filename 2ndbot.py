import discord
from discord.ext import commands, tasks
from itertools import cycle
client = commands.Bot(command_prefix = '>.')
status = cycle(['Property of EVIL EMPIRE', 'EVIL EMPIRE'])


@client.event
async def on_ready():
    print('bot is ready')

@tasks.loop(seconds=11110000000000)
async def  change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
 await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
 await member.ban(reason=reason)
 await ctx.send(f'Banned {member.name}#{member.mention}')


client.run('NzAyMDU4NTYxNzk0MjExOTAw.XqE4pQ.AOLEg_VgSqE3q5CZys5N30R4xd0')
