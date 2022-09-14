import discord
from discord.ext import commands

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
    chan = bot.get_channel(940896090566316074)
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



@bot.command(pass_context=True)
@commands.has_role("Bot-Permissions")
async def rr1(ctx):
    embed = discord.Embed(
        title="\n",
        description="♡ -₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋- ♡ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Choose Your Platform⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ \n ♡ -⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻- ♡ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🖥️ <@&{4}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⬛ <@&{3}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🕹️ <@&{2}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⬜ <@&{1}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀1️⃣  <@&{0}>; ".format(1019474334001147944, 1019474332256313384, 1019473942341230622, 1019473941493993492, 1019473940768366622),
        color=0,
    )

    embed.set_footer(text="Having Problems? Contact me! Azazel#1949")
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("🖥️")
    await msg.add_reaction("⬛")
    await msg.add_reaction("🕹️")
    await msg.add_reaction("⬜")
    await msg.add_reaction("1️⃣")


@bot.command(pass_context=True)
@commands.has_role("Bot-Permissions")
async def rr2(ctx):
    embed = discord.Embed(
        title="\n",
        description="♡ -₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋- ♡ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Choose Your Intrests⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ \n ♡ -⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻- ♡ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🎮 <@&{4}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🛏️ <@&{3}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🤖 <@&{2}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🎧 <@&{1}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🍀 <@&{0}>; \n".format(1019474590289895424, 1019474581985165353, 1019474572036296704, 1019474570333392926, 1019474563836432386),
        color=0,
    )

    embed.set_footer(text="Having Problems? Contact me! Azazel#1949")
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("🎮")
    await msg.add_reaction("🛏️")
    await msg.add_reaction("🤖")
    await msg.add_reaction("🎧")
    await msg.add_reaction("🍀")
        

        
@bot.command(pass_context=True)
@commands.has_role("Bot-Permissions")
async def rr3(ctx):
    embed = discord.Embed(
        title="\n",
        description="♡ -₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋- ♡ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Choose Your Color⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ \n ♡ -⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻- ♡ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🟡 <@&{7}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🟢 <@&{6}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🔵 <@&{5}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🔴 <@&{4}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🟣 <@&{3}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🟤 <@&{2}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⚪ <@&{1}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⚫ <@&{0}>; ".format(1019474733437304894, 1019474732703289394, 1019474731595993100, 1019474731294007376, 1019474730505486396, 1019474729754710027, 1019474729050058752, 1019474592298971236),
        color=0,
    )

    embed.set_footer(text="Having Problems? Contact me! Azazel#1949")
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
async def rr4(ctx):
    embed = discord.Embed(
        title="\n",
        description="♡ -₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋- ♡ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Choose Your Age&Gender⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ \n ♡ -⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻- ♡ \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀👩 <@&{4}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀👨 <@&{3}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🧑‍🦲 <@&{2}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀➖ <@&{1}>; \n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀➕ <@&{0}>; ".format(1019474404373180419, 1019474409217589249, 1019474429975216200, 1019474427303432204, 1019474424317100095),
        color=0,
    )

    embed.set_footer(text="Having Problems? Contact me! Azazel#1949")
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("👩")
    await msg.add_reaction("👨")
    await msg.add_reaction("🧑‍🦲")
    await msg.add_reaction("➖")
    await msg.add_reaction("➕")
        


@bot.command(pass_context=True)
@commands.has_role("Bot-Permissions")
async def rrall(ctx): 
    await rr1(ctx)
    await rr2(ctx)
    await rr3(ctx)
    await rr4(ctx)

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

TOKEN = os.environ.get("DISCORD_TOKEN")
bot.run(TOKEN)