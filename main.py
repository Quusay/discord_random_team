import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import random
import math

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
bot = commands.Bot(command_prefix='.', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.watching, name="YOUR MOMS ASS"))

@bot.command(name='random', aliases=['r', 'rand'], help='*name (how many teams) e.g player1 player2 player3 player4 etc 2')
async def lol(ctx, *, msg):
    splitPlayerNames = msg.split()
    storeTeam = int(splitPlayerNames[-1])
    splitPlayerNames.remove(splitPlayerNames[-1])
    maxTeamSize = math.ceil(len(splitPlayerNames) / storeTeam)
    splitIntoTeams = [[] for x in range(storeTeam)]
    if len(splitPlayerNames) < storeTeam:
        embed = discord.Embed(
        description= "Too many teams",
        color=0xFF5733)
        embed.set_author(name=ctx.author.display_name,
                    icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        counter = 0
        while len(splitPlayerNames) > 0:
            getRandomPlayer = random.choice(splitPlayerNames)
            splitIntoTeams[counter].append(getRandomPlayer)
            splitPlayerNames.remove(getRandomPlayer)
            if len(splitIntoTeams[counter]) >= maxTeamSize:
                counter+=1
            
        filter(None, splitIntoTeams)
        for i in range(storeTeam):
            embed = discord.Embed(
                title=f"Team {i+1}",
                description= f"{' '.join(splitIntoTeams[i]).title()}",
                color=0xFF5733)
            embed.set_author(name=ctx.author.display_name,
                            icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    
@bot.command(help='purges')
async def purge(ctx, msg=5):
    # msg = int(msg)
    await ctx.channel.purge(limit = msg+1)
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.send('You did not give me anything to repeat!')

bot.run(TOKEN)
