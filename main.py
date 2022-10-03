import discord
from discord.ext import commands

import os
import random
import time

intents = discord.Intents().all()

bot = commands.Bot(command_prefix='$', intents=intents, help_command=None)

@bot.event
async def on_ready():
    servercount = len(bot.guilds)
    latency = bot.latency * 1000

    print(' ______     ______     __  __     __         ______     ______     _____     ______     ______    ')
    print('/\  == \   /\  __ \   /\ \_\ \   /\ \       /\  __ \   /\  __ \   /\  __-.  /\  ___\   /\  == \   ')
    print('\ \  __<   \ \  __ \  \ \____ \  \ \ \____  \ \ \/\ \  \ \  __ \  \ \ \/\ \ \ \  __\   \ \  __<   ')
    print(' \ \_\ \_\  \ \_\ \_\  \/\_____\  \ \_____\  \ \_____\  \ \_\ \_\  \ \____-  \ \_____\  \ \_\ \_\ ')
    print('  \/_/ /_/   \/_/\/_/   \/_____/   \/_____/   \/_____/   \/_/\/_/   \/____/   \/_____/   \/_/ /_/ ')
    print('                                                                                                  ')
    time.sleep(2)
    print("Starting boot process...")
    time.sleep(1)
    print("Bot has logged in as {0.user}.".format(bot))
    time.sleep(0.5)
    print("{0.user} is in {1} server(s).".format(bot, servercount))
    time.sleep(0.5)
    print("Starting latency process...")
    chan = bot.get_channel(1021828189330362539)
    b4 = time.monotonic()
    msg = await chan.send("Pong!")
    ping = (time.monotonic() - b4) * 1000
    await msg.delete()
    time.sleep(0.5)
    print("The message latency is {0}ms.".format(int(ping)))
    time.sleep(0.5)
    print("The API latency is {0}ms.".format(latency))
    time.sleep(0.5)
    print("Latency process ended!")
    time.sleep(0.5)
    print("The token is {0}.".format(os.environ.get("DISCORD_TOKEN")))
    time.sleep(0.5)
    print("Boot process ended!")


red = discord.Color.from_rgb(255, 0, 0)
green = discord.Color.from_rgb(255, 87, 51)





# ------------ START RULES ------------
@bot.command()
@commands.has_role("Bot-Permissions")
async def rules(ctx):  # Send command

    embed = discord.Embed(
        title="Rules",
        color=0x00FF00,
    )
    embed.set_footer(
        text="Staff will warn you with a number corresponding to the rule you broke."
    )

    embed.add_field(
        name="-1 General Rules", value="*1.1* Discord TOS", inline=False
    )
    embed.add_field(
        name="-2 Chat Rules", value="*2.1* No racism of any kind \n *2.2* No sexism of any kind \n *2.3* No bullying \n *2.4* What Staff says goes (with some exceptions) \n *2.5* Splooge, Ddog and Milly are always right doesnt matter what they say (no im not a simp lol)", inline=False
    )
    embed.add_field(
        name="-3 Voice Chat Rules", value="*3.1* Rules 2.1 to 2.5 apply \n *3.2* No earrape", inline=False
    )

    

    await ctx.channel.purge(limit=1)
    await ctx.channel.send(embed=embed)


# ------------ END RULES ------------


# ------------ START SUGGESTIONS ------------
@bot.command()
async def suggest(ctx, *, args):  # Send command

    embed = discord.Embed(
        title="Suggestion",
        description="{author} suggests: \n {suggestion}".format(
            author=ctx.author, suggestion=args
        ),
        color=0x00FF00,
    )
    embed.set_footer(text="To suggest something use $suggest")
    await ctx.channel.purge(limit=1)
    await ctx.channel.send(embed=embed)


# ------------ END SUGGESTIONS ------------


# ------------ START RANDOM ------------
@bot.command()
async def randomNum(ctx, arg1, arg2):
    await ctx.channel.purge(limit=1)
    await ctx.send(random.randrange(int(arg1), int(arg2) + 1))


@bot.command()
async def eightball(ctx):
    answer = ["Yes", "No", "Maybe", "idfk"]
    await ctx.channel.purge(limit=1)
    await ctx.send("The Oracle says: " + random.choice(answer))


@bot.command()
async def coinflip(ctx):
    ht = ["Heads", "Tails"]
    await ctx.channel.purge(limit=1)
    await ctx.send("The Coin says: " + random.choice(ht))


# ------------ END RANDOM ------------


# ------------ START CALC ------------
@bot.command()
async def calc(ctx, num1: int, calculus, num2: int):
    await ctx.channel.purge(limit=1)
    if calculus == "-" or calculus == "minus" or calculus == "m":
        await ctx.send(str(num1 - num2))
    if calculus == "+" or calculus == "plus" or calculus == "p":
        await ctx.send(str(num1 + num2))
    elif calculus == "*" or calculus == "x" or calculus == "times" or calculus == "t":
        await ctx.send(str(num1 * num2))
    elif calculus == "/" or calculus == "divided by" or calculus == "d":
        await ctx.send(str(num1 / num2))


# ------------ END CALC ------------


# ------------ START LATENCY ------------
@bot.command()
async def defaultping(ctx):
    await ctx.send("pong")


@bot.command()
async def apiping(ctx):
    await ctx.send(f"Pong! Took: {round(bot.latency * 1000)}ms to ping the api!")


@bot.command()
async def ping(ctx):
    b4 = time.monotonic()
    msg = await ctx.send("Starting editing process...")
    ping = (time.monotonic() - b4) * 1000
    await msg.edit(content="Pong! Took: {}ms to edit!".format(int(ping)))


# ------------ END LATENCY ------------



# ------------ START INVITE ------------
@bot.command()
async def invites(ctx, usr: discord.Member=None):
    if usr == None:
       user = ctx.author
    else:
       user = usr
    total_invites = 0
    guild_invites = ctx.guild.invites()
    for i in await guild_invites:
        if i.inviter == user:
            total_invites += i.uses
    await ctx.send(f"{user.name} has invited {totalInvites} member{'' if totalInvites == 1 else 's'}!")


@bot.command()
async def leaderboard(ctx, x=10):
  with open('level.json', 'r') as f:
    
    users = json.load(f)
    
  leaderboard = {}
  total=[]
  
  for user in list(users[str(ctx.guild.id)]):
    name = int(user)
    total_amt = users[str(ctx.guild.id)][str(user)]['experience']
    leaderboard[total_amt] = name
    total.append(total_amt)
    

  total = sorted(total,reverse=True)
  

  em = discord.Embed(
    title = f'Top {x} highest leveled members in {ctx.guild.name}',
    description = 'The highest leveled people in this server'
  )
  
  index = 1
  for amt in total:
    id_ = leaderboard[amt]
    member = client.get_user(id_)
    
    
    em.add_field(name = f'{index}: {member}', value = f'{amt}', inline=False)
    
    
    if index == x:
      break
    else:
      index += 1
      
  await ctx.send(embed = em)
# ------------ END INVITE ------------



# ------------ START BASICS ------------
@bot.command()
@commands.has_role("Bot-Permissions")
async def announce(ctx, *, args):
    title = args.split("|")[0]
    desc = args.split("|")[1]
    footer = desc.split("~")[1]       
    embed = discord.Embed(title=title, description=desc.split("~")[0], color=0x00FF00)
    embed.set_footer(text=footer)

    await ctx.send(embed=embed)


@bot.command()
async def say(ctx, *, arg):
    await ctx.send(arg)


@bot.command(pass_context=True)
async def whoAmI(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send(ctx.author)


@bot.command(pass_context=True)
async def topRoleMe(ctx):
    await ctx.channel.purge(limit=1)
    member = ctx.message.author
    top_role = member.top_role
    await ctx.send(top_role.name)


@bot.command(pass_context=True)
async def topRoleBot(ctx):
    await ctx.channel.purge(limit=1)
    member = ctx.guild.get_member(bot.user.id)
    top_role = member.top_role
    await ctx.send(top_role.name)


@bot.command()
async def noticeMe(ctx):
    await ctx.channel.purge(limit=1)
    user = await ctx.bot.fetch_user(610057690651033600)
    await user.send(ctx.author)


# ------------ END BASICS ------------



# ------------ START EVENTS ------------
@bot.event
async def on_member_join(member):
    #await bot.get_channel(1019253118124425277).send("Welcome <@!{0}>! Check <#{1}> to choose your Roles!".format(member.id, 1008376221471604766))

    embed = discord.Embed(
        title="Intruder Alert!", description="Welcome {0} to the DDOG Family! \n Check <#{1}> to choose your Roles; \n Look in <#{2}> to read the Rules; \n If you'd like to apply for staff check out <#{3}>".format(member.mention, 1019316218064281683, 941283597233553429, 1018554996847038504), color=0
    )

    embed.set_footer(text="Please dont ignore this message!")
    await bot.get_channel(940896090566316074).send(embed=embed)

# ------------ END EVENTS ------------



# ------------ START RR ------------
@bot.command(pass_context=True)
@commands.has_role("Bot-Permissions")
async def rrplatform(ctx):
    embed = discord.Embed(
        title="\n",
        description="♡ -₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋- ♡ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Choose Your Platform⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ \n ♡ -⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻- ♡ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🖥️ <@&{4}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⬛ <@&{3}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🕹️ <@&{2}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⬜ <@&{1}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀1️⃣  <@&{0}>; ".format(1019474334001147944, 1019474332256313384, 1019473942341230622, 1019473941493993492, 1019473940768366622),
        color=0,
    )

    embed.set_footer(text="Having Problems? Contact Staff!")
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("🖥️")
    await msg.add_reaction("⬛")
    await msg.add_reaction("🕹️")
    await msg.add_reaction("⬜")
    await msg.add_reaction("1️⃣")


@bot.command(pass_context=True)
@commands.has_role("Bot-Permissions")
async def rrintrests(ctx):
    embed = discord.Embed(
        title="\n",
        description="♡ -₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋- ♡ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Choose Your Intrests⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ \n ♡ -⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻- ♡ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🎮 <@&{4}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🛏️ <@&{3}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🤖 <@&{2}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🎧 <@&{1}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🍀 <@&{0}>; \n".format(1019474590289895424, 1019474581985165353, 1019474572036296704, 1019474570333392926, 1019474563836432386),
        color=0,
    )

    embed.set_footer(text="Having Problems? Contact Staff!")
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("🎮")
    await msg.add_reaction("🛏️")
    await msg.add_reaction("🤖")
    await msg.add_reaction("🎧")
    await msg.add_reaction("🍀")
        

        
@bot.command(pass_context=True)
@commands.has_role("Bot-Permissions")
async def rrcolor(ctx):
    embed = discord.Embed(
        title="\n",
        description="♡ -₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋- ♡ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Choose Your Color⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ \n ♡ -⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻- ♡ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🟡 <@&{7}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🟢 <@&{6}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🔵 <@&{5}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🔴 <@&{4}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🟣 <@&{3}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🟤 <@&{2}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⚪ <@&{1}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⚫ <@&{0}>; ".format(1019474733437304894, 1019474732703289394, 1019474731595993100, 1019474731294007376, 1019474730505486396, 1019474729754710027, 1019474729050058752, 1019474592298971236),
        color=0,
    )

    embed.set_footer(text="Having Problems? Contact Staff!")
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("🟡")
    await msg.add_reaction("🟢")
    await msg.add_reaction("🔵")
    await msg.add_reaction("🔴")
    await msg.add_reaction("⚪")
    await msg.add_reaction("⚫")
    await msg.add_reaction("🟣")
    await msg.add_reaction("🟤")
        


@bot.command(pass_context=True)
@commands.has_role("Bot-Permissions")
async def rragengender(ctx):
    embed = discord.Embed(
        title="\n",
        description="♡ -₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋- ♡ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Choose Your Age&Gender⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ \n ♡ -⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻- ♡ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀👩 <@&{4}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀👨 <@&{3}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🧑‍🦲 <@&{2}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀➖ <@&{1}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀➕ <@&{0}>; ".format(1019474404373180419, 1019474409217589249, 1019474429975216200, 1019474427303432204, 1019474424317100095),
        color=0,
    )

    embed.set_footer(text="Having Problems? Contact Staff!")
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("👩")
    await msg.add_reaction("👨")
    await msg.add_reaction("🧑‍🦲")
    await msg.add_reaction("➖")
    await msg.add_reaction("➕")
        


@bot.command(pass_context=True)
@commands.has_role("Bot-Permissions")
async def rrall(ctx): 
    await rragengender(ctx)
    await rrintrests(ctx)
    await rrplatform(ctx)
    await rrcolor(ctx)

    @bot.event
    async def on_reaction_add(reaction, user):
        if reaction.emoji == "🖥️":
            await ctx.send(str(user) + " chose PC")
        elif reaction.emoji == "⬛":
            await ctx.send(str(user) + " chose PS4")
        elif reaction.emoji == "🕹️":
            await ctx.send(str(user) + " chose Series")
        elif reaction.emoji == "⬜":
            await ctx.send(str(user) + " chose PS5")
        elif reaction.emoji == "1️⃣":
            await ctx.send(str(user) + " chose One")
        elif reaction.emoji == "🛏️":
            await ctx.send(str(user) + " chose Chilling")
        elif reaction.emoji == "🎮":
            await ctx.send(str(user) + " chose Games")
        elif reaction.emoji == "🤖":
            await ctx.send(str(user) + " chose Bots")
        elif reaction.emoji == "🎧":
            await ctx.send(str(user) + " chose Music")
        elif reaction.emoji == "🍀":
            await ctx.send(str(user) + " chose Luck")
        elif reaction.emoji == "🟡":
            await ctx.send(str(user) + " chose Yellow")
        elif reaction.emoji == "🟢":
            await ctx.send(str(user) + " chose Green")
        elif reaction.emoji == "🔵":
            await ctx.send(str(user) + " chose Blue")
        elif reaction.emoji == "🔴":
            await ctx.send(str(user) + " chose Red")
        elif reaction.emoji == "⚪":
            await ctx.send(str(user) + " chose White")
        elif reaction.emoji == "⚫":
            await ctx.send(str(user) + " chose Black")
        elif reaction.emoji == "🟣":
            await ctx.send(str(user) + " chose Purple")
        elif reaction.emoji == "🟤":
            await ctx.send(str(user) + " chose Brown")
        elif reaction.emoji == "👩":
            await ctx.send(str(user) + " chose Female")
        elif reaction.emoji == "👨":
            await ctx.send(str(user) + " chose Male")
        elif reaction.emoji == "🧑‍🦲":
            await ctx.send(str(user) + " chose Other")
        elif reaction.emoji == "➖":
            await ctx.send(str(user) + " chose +18")
        elif reaction.emoji == "➕":
            await ctx.send(str(user) + " chose -18")    
# ------------ END RR ------------


# ------------ START ERRORS ------------
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.channel.purge(limit=1)
        await ctx.send("You don't have the required permissions to do that")


@heist.error
async def heist_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.channel.purge(limit=1)
        await ctx.send("You don't have the required permissions to do that")


# ------------ END ERRORS ------------
TOKEN = os.environ.get("DISCORD_TOKEN")
bot.run(TOKEN)
