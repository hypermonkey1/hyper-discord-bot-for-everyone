import discord
from discord.ext import commands
from time import sleep
from discord.ext.commands import has_permissions, CheckFailure
import discord.ext
from discord.ext.commands import has_permissions
import json
import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


BOT = discord.Client()
bot_prefix = "$"
bot = commands.Bot(command_prefix=bot_prefix)



token = "null"
with open("token.txt") as file:
    token = file.readline()


userSettings = {
    "userName" : "name",
    "language" : "null",
    "messageLev" : 0,
    "currentLevel" : 0,
    "needXP" : 20,
}

varise = False



@bot.event
async def on_ready():
    bot.remove_command('help')
    print("Bot is started.")


        



@bot.command()
async def rank(ctx):
    with open("userSettings/"+str(ctx.author.id) + ".json","r") as file:
        okunanDosya = json.load(file)
    if(okunanDosya["language"] == "en_US"):
        await ctx.channel.send(ctx.author.mention + " " + "Your level is : " + str(okunanDosya["currentLevel"]))
    if(okunanDosya["language"] == "tr_TR"):
        await ctx.channel.send(ctx.author.mention + " " + "Senin seviyen : " + str(okunanDosya["currentLevel"]))



@bot.command()
async def language(ctx,LANGUAGE_ID):
    with open("userSettings/"+str(ctx.author.id) + ".json","r") as file:
        okunanDosya = json.load(file)
    if(LANGUAGE_ID == "tr_TR"):
        with open("userSettings/"+str(ctx.author.id) + ".json","w") as file:
            userSettings["userName"] = ctx.author.name
            userSettings["language"] = "tr_TR"
            userSettings["currentLevel"] = okunanDosya["currentLevel"]
            userSettings["messageLev"] = okunanDosya["messageLev"]
            userSettings["needXP"] = okunanDosya["needXP"]
            await ctx.channel.send(ctx.author.mention + " " + "Dilin başarıyla değiştirildi şu anki dil: " + LANGUAGE_ID)
            json.dump(userSettings,file,indent=4)
    if(LANGUAGE_ID == "en_US"):
        with open("userSettings/"+str(ctx.author.id) + ".json","w") as file:
            userSettings["userName"] = ctx.author.name
            userSettings["language"] = "en_US"
            userSettings["currentLevel"] = okunanDosya["currentLevel"]
            userSettings["messageLev"] = okunanDosya["messageLev"]
            userSettings["needXP"] = okunanDosya["needXP"]
            json.dump(userSettings,file,indent=4)
            await ctx.channel.send(ctx.author.mention + " " + "Your language successfully changed current language: " + LANGUAGE_ID)




@bot.command()
@has_permissions(manage_channels=True)
async def clear(ctx,amount):
    with open("userSettings/" + str(ctx.author.id) + ".json","r") as file:
        userLanguage = {}
        userLanguage = json.load(file)
    if(userLanguage["language"] == "tr_TR"):
        userMention = ctx.author.mention
        await ctx.channel.purge(limit=int(amount))
        sleep(1)
        await ctx.channel.send("Hey !" + " " + userMention + " " + amount + " Mesaj silindi!")

    if(userLanguage["language"] == "en_US"):
        userMention = ctx.author.mention
        await ctx.channel.purge(limit=int(amount))
        sleep(1)
        await ctx.channel.send("Hey !" + " " + userMention + " " + amount + " Message deleted!")
@clear.error
async def clear_error(ctx,error):
    with open("userSettings/" + str(ctx.author.id) + ".json","r") as file:
        userLanguage = {}
        userLanguage = json.load(file)
    if(userLanguage["language"] == "en_US"):
        print("Hata" + ":" +error)
        embed=discord.Embed(title="Sorry you don't have permission.")
        await ctx.channel.send(embed=embed)
    if(userLanguage["language"] == "tr_TR"):
        print("Hata" + ":" +error)
        embed=discord.Embed(title="Üzgünüm bu komut için yetkin yok.")
        await ctx.channel.send(embed=embed)






@bot.command()
@has_permissions(ban_members=True)
async def ban(ctx,member : discord.Member,reason = None):
    embed=discord.Embed(title=ctx.message.guild.name, description="adlı sunucudan yasaklandın.")
    embed.add_field(name="Sebep :", value=reason, inline=False)
    embed.set_footer(text="selam ben hyper!")
    await member.send(embed=embed)
    embedChat=discord.Embed(title=member.mention, description="sunucudan yasaklandı.")
    embedChat.add_field(name="Sebep :", value=reason, inline=False)
    embedChat.set_footer(text="selam ben hyper!")
    await ctx.channel.send(embed=embedChat)
    await member.ban(reason=reason)
    with open("bannedUsers.txt" , "a",encoding="utf-8") as file:
        file.write(str(member.mention) + " " + "banned reason : " + reason)
@ban.error
async def ban_error(ctx,error):
    with open("userSettings/" + str(ctx.author.id) + ".json","r") as file:
        userLanguage = {}
        userLanguage = json.load(file)
    if(userLanguage["language"] == "en_US"):
        print("Hata" + ":" +error)
        embed=discord.Embed(title="Sorry you can't have permission.")
        await ctx.channel.send(embed=embed)
    if(userLanguage["language"] == "tr_TR"):
        print("Hata" + ":" +error)
        embed=discord.Embed(title="Üzgünüm bu komut için yetkin yok.")
        await ctx.channel.send(embed=embed)





@bot.command()
async def öneri(ctx,oneri):
    ONERI = f"{ctx.author.name} : {oneri}"
    with open("suggestions.txt","a") as file:
        file.write(ONERI + "\n")
        embed=discord.Embed(title="Önerin gönderildi.")
        embed.add_field(name=ctx.author.name + ":", value=oneri, inline=False)
        await ctx.channel.send(embed=embed)

@bot.command()
async def suggestion(ctx,oneri):
    ONERI = f"{ctx.author.name} : {oneri}"
    with open("suggestions.txt","a") as file:
        file.write(ONERI + "\n")
        embed=discord.Embed(title="You're suggestion sent.")
        embed.add_field(name=ctx.author.name + ":", value=oneri, inline=False)
        await ctx.channel.send(embed=embed)
        

    





@bot.command()
@has_permissions(kick_members=True)
async def kick(ctx,member : discord.Member,reason = None):
    embed=discord.Embed(title=ctx.message.guild.name, description="adlı sunucudan atıldın.")
    embed.add_field(name="Sebep :", value=reason, inline=False)
    embed.set_footer(text="selam ben hyper!")
    await member.send(embed=embed)
    embedChat=discord.Embed(title=member.name, description="sunucudan atıldı.")
    embedChat.add_field(name="Sebep :", value=reason, inline=False)
    embedChat.set_footer(text="selam ben hyper!")
    await ctx.channel.send(embed=embedChat)
    await member.kick(reason=reason)
@kick.error
@ban.error
async def kick_error(ctx,error):
    with open("userSettings/" + str(ctx.author.id) + ".json","r") as file:
        userLanguage = {}
        userLanguage = json.load(file)
    if(userLanguage["language"] == "en_US"):
        print("Hata" + ":" +error)
        embed=discord.Embed(title="Sorry you can't have permission.")
        await ctx.channel.send(embed=embed)
    if(userLanguage["language"] == "tr_TR"):
        print("Hata" + ":" +error)
        embed=discord.Embed(title="Üzgünüm bu komut için yetkin yok.")
        await ctx.channel.send(embed=embed)








try:
    bot.run(token)
except:
    print("Error while trying to start bot.")