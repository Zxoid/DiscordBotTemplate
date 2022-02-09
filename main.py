import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '')
# put custom prefix insife of the apostrophe

@client.event
async def on_ready ():
  await client.change_presence(status=discord.Status.Online, activity=discord.Game(''))
 # put custom game inside of the apostrophe 

  print('Bot Is Online.')



@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=5):
  await ctx.channel.purge(limit=amount)

non_kick = ("no reason specified")
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=(non_kick)):
    await ctx.send(f"{member} was kicked for:\n {reason}")
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, * , reason=None): await member.ban(reason=reason)

client.run ('')
# Put your discord authentication token inside of the apostrophe 
