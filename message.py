import discord
from discord.ext.commands import Bot
from discord.ext import commands
import json
from datetime import datetime
from random import randint
from time import sleep
import os





BOT = discord.Client()
bot_prefix = "$"
bot = commands.Bot(command_prefix=bot_prefix)
yaziTuraGIF = ""
yazıTura = 0
settings = ""
delay = 3


token = "null"
with open("token.txt") as file:
    token = file.readline()



with open("bad-words.txt") as file:
    bad_words = [bad_word.strip().lower() for bad_word in file.readlines()]

with open("anti-ad.txt") as file:
    antiAds = [antiAd.strip().lower() for antiAd in file.readlines()]


with open('settings.json') as f:
  settings = {}
  settings = json.load(f)
  yaziTuraGIF = settings["yaziTuraGIF"]
  kufurisEnabled = settings["kufurisEnabled"]
  f.close()



kullaniciSettings = {
    "userName" : "name",
    "language" : "null",
    "messageLev" : 0,
    "currentLevel" : 0,
    "needXP" : 20,
}


@bot.event
async def on_message(message):
    varise = os.path.exists("userSettings/" + str(message.author.id) + ".json")
    if(varise == False):
        with open("userSettings/"+str(message.author.id) + ".json","w") as file:
            kullaniciSettings["userName"] = message.author.name
            kullaniciSettings["language"] = "tr_TR"
            json.dump(kullaniciSettings,file,indent=4)
    else:
        with open("userSettings/"+str(message.author.id) + ".json","r") as file:
            userSettings = json.load(file)


    mesaj = message
    currentTime = datetime.now()
    digerZaman = str(currentTime)
    userMention = message.author.mention
    

    userSettings["messageLev"] +=1
    with open("userSettings/"+str(message.author.id) + ".json","w") as file:
        json.dump(userSettings,file,indent=4)



    if(message.content == "$cleardatabase"):
        if(message.author.id == 764101448766062592):
            print("BOT Author Tested and passed")
            print("Database silme islemi")


    if(userSettings["messageLev"] == userSettings["needXP"]):
        userSettings["currentLevel"] += 1
        if(userSettings["language"] == "tr_TR"):
            await message.channel.send(userMention)
            embed=discord.Embed(title="Seviye Atladın!")
            embed.add_field(name="Seviyen", value=userSettings["currentLevel"], inline=False)
            embed.add_field(name="Sonraki seviye için gereken mesaj sayısı.", value=userSettings["needXP"], inline=False)
            await message.channel.send(embed=embed)
            userSettings["messageLev"] = 0
            userSettings["needXP"] += 20
        
        if(userSettings["language"] == "en_US"):
            await message.channel.send(userMention)
            embed=discord.Embed(title="Level Up!")
            embed.add_field(name="Your Level", value=userSettings["currentLevel"], inline=False)
            embed.add_field(name="Number of messages required for the next level.", value=userSettings["needXP"], inline=False)
            await message.channel.send(embed=embed)
            userSettings["messageLev"] = 0
            userSettings["needXP"] += 20
        with open("userSettings/"+str(message.author.id) + ".json","w") as file:
            json.dump(userSettings,file,indent=4)

    if(userSettings["language"] == "tr_TR"):
        if(message.content == "$davetet"):
            embed=discord.Embed(title="Hey !", description="DM Mesajlarına bakarmısın ? ")
            embed.set_footer(text="Selam ! Ben hyper!")
            await message.channel.send(embed=embed)
            embedTwo=discord.Embed(title="Davet etmek için tıkla!", url="https://discord.com/oauth2/authorize?client_id=712325623770775555&scope=bot&permissions=473136198")
            embedTwo.add_field(name="Hyper'ı davet etmek istiyorsan", value="Tıkla!", inline=False)
            await message.author.send(embed=embedTwo)

    if(userSettings["language"] == "en_US"):
        if(message.content == "$inviteme"):
            embed=discord.Embed(title="Hey !", description="Can you see DM ?")
            embed.set_footer(text="Hi! I'm hyper")
            await message.channel.send(embed=embed)
            embedTwo=discord.Embed(title="Click me for invite me your server!", url="https://discord.com/oauth2/authorize?client_id=712325623770775555&scope=bot&permissions=473136198")
            embedTwo.add_field(name="If you want invite hyper click the link!", value="Click me!", inline=False)
            await message.author.send(embed=embedTwo)

    if(userSettings["language"] == "tr_TR"):
        if(message.content == "$küfüraç"):
            embed=discord.Embed(title=message.channel.guild.name, description="Küfür koruma devre dışı.")
            await message.channel.send(embed=embed)
            kufurisEnabled = True
            settings["kufurisEnabled"] = True
            with open('settings.json','w') as f:
                json.dump(settings,f,indent=4)

    if(userSettings["language"] == "en_US"):
        if(message.content == "$enableswearing"):
            embed=discord.Embed(title=message.channel.guild.name, description="Anti swearing disabled")
            await message.channel.send(embed=embed)
            kufurisEnabled = True
            settings["kufurisEnabled"] = True
            with open('settings.json','w') as f:
                json.dump(settings,f,indent=4)
            
    if(userSettings["language"] == "tr_TR"): 
        if(message.content == "$küfürkapat"):
            embed=discord.Embed(title=message.channel.guild.name, description="Küfür koruma etkin.")
            await message.channel.send(embed=embed)
            kufurisEnabled = False
            settings["kufurisEnabled"] = False
            with open('settings.json','w') as f:
                json.dump(settings,f,indent=4)


    if(userSettings["language"] == "en_US"):
        if(message.content == "$level"):
            embed=discord.Embed(title=f"Ihm {message.author.name} , I think you want to learn your level.")
            embed.add_field(name="Your level", value=str(userSettings["currentLevel"]) + " " +"Lv.", inline=False)
            embed.add_field(name="Number of messages required for the next level.", value=str(userSettings["needXP"]) + " " + "XP", inline=False)
            embed.add_field(name="Message Level.", value=str(userSettings["messageLev"]) + " " + "XP", inline=False)
            await message.channel.send(embed=embed)
    if(userSettings["language"] == "tr_TR"):
        if(message.content == "$seviye"):
            embed=discord.Embed(title=f"Ihm {message.author.name}, Sanırım seviyeni öğrenmek istiyorsun.")
            embed.add_field(name="Seviyen", value=str(userSettings["currentLevel"]) + " " +"Sv.", inline=False)
            embed.add_field(name="Sonraki seviye için gereken mesaj sayısı.", value=str(userSettings["needXP"]) + " " + "XP", inline=False)
            embed.add_field(name="Seviye Puanın.", value=str(userSettings["messageLev"]) + " " + "XP", inline=False)
            await message.channel.send(embed=embed)
          

    if(userSettings["language"] == "en_US"): 
        if(message.content == "$disableswearing"):
            embed=discord.Embed(title=message.channel.guild.name, description="Anti Swearing is enabled.")
            await message.channel.send(embed=embed)
            kufurisEnabled = False
            settings["kufurisEnabled"] = False
            with open('settings.json','w') as f:
                json.dump(settings,f,indent=4)

    with open("logfile.txt" , "a",encoding="utf-8") as file:
        file.write("(" + digerZaman + ")" + " " + str(message.author) + ":" + message.content + "\n")
    
    if(userSettings["language"] == "tr_TR"): 
        if(message.content == "$yardım"):
            embed=discord.Embed(title="Yardım", description="Selam sana birkaç komuttan bahsedeyim öncelikle ben hyper bunlar da benim komutlarım!")
            embed.add_field(name="Kullanıcı komutları:", value="Komutlar ;", inline=False)
            embed.add_field(name="$yazıtura", value="Arkadaşlarınla yazı tura oynamanı sağlar!", inline=True)
            embed.add_field(name="$davetet", value="Beni sunucuna davet etmeni sağlar!", inline=False)
            embed.add_field(name="$language en_US yada $language tr_TR", value="Bu komut sayesinde dil değiştirebilirsin.", inline=False)
            embed.add_field(name="Yönetici komutları :", value="Komutlar ;", inline=True)
            embed.add_field(name="$clear (mesaj sayısı)", value="Konuşma mesajları silmeye yarar.", inline=False)
            embed.add_field(name="$ban (kullanıcı)  'sebep'", value="Kullanıcıyu sunucudan yasaklamaya yarar.", inline=True)
            embed.add_field(name="$kick (kullanıcı) 'sebep'", value="Kullanıcı sunucudan atmaya yarar.", inline=False)
            embed.add_field(name="$language en_US yada $language tr_TR", value="Bu komut sayesinde dil değiştirebilirsin.", inline=False)
            embed.set_footer(text="selam ben hyper!")
            await message.author.send(embed=embed)
            embed=discord.Embed(title="Hey !", description="DM Mesajlarına bakarmısın ? ")
            embed.set_footer(text="Selam ! Ben hyper!")
            await message.channel.send(embed=embed)

    if(userSettings["language"] == "en_US"): 
        if(message.content == "$help"):
            embed=discord.Embed(title="Help", description="Hi! I can teach some commands follow me!")
            embed.add_field(name="User commands:", value="Commands;", inline=False)
            embed.add_field(name="$headortails", value="Play head or tails with your friends!", inline=True)
            embed.add_field(name="$inviteme", value="You can invite me your servers!", inline=False)
            embed.add_field(name="$language en_US or $language tr_TR", value="You can change language with this command!.", inline=False)
            embed.add_field(name="Admin commands :", value="Commands ;", inline=True)
            embed.add_field(name="$clear (message number)", value="You can delete message with this command!", inline=False)
            embed.add_field(name="$ban (user)  'reason'", value="You can ban users with this command.", inline=True)
            embed.add_field(name="$kick (user) 'reason'", value="You can kick users with this command.", inline=False)
            embed.set_footer(text="Hi! I'm hyper!")
            await message.author.send(embed=embed)
            embed=discord.Embed(title="Hey !", description="Can you look DM? ")
            embed.set_footer(text="Hi ! I'm hyper!")
            await message.channel.send(embed=embed)

    if (message.content == "sa"):
        await message.channel.send(userMention + " " +"Aleyküm selam, Hoşgeldin!")
     
    if(userSettings["language"] == "en_US"): 
        if (message.content == "$headortails"):
            await message.channel.send(yaziTuraGIF)
            yazıTura = randint(0,1)
            sleep(1.2)
            if(yazıTura == 1):
                embed=discord.Embed(title="Head won!", description="Congrats for winner!")
                embed.set_author(name="hyper")
                await message.channel.send(embed=embed)
            if(yazıTura == 0):
                embed=discord.Embed(title="Tails won!", description="Congrats for winner!")
                embed.set_author(name="hyper")
                await message.channel.send(embed=embed)

    if(userSettings["language"] == "tr_TR"): 
        if (message.content == "$yazıtura"):
            await message.channel.send(yaziTuraGIF)
            yazıTura = randint(0,1)
            sleep(1.2)
            if(yazıTura == 1):
                embed=discord.Embed(title="Tura kazandı!", description="Kazanana tebrikler!")
                embed.set_author(name="hyper")
                await message.channel.send(embed=embed)
            if(yazıTura == 0):
                embed=discord.Embed(title="Yazı kazandı!", description="Kazanana tebrikler!")
                embed.set_author(name="hyper")
                await message.channel.send(embed=embed)
 


    if(settings["kufurisEnabled"] == False):  
        if any(bad_word in message.content for bad_word in bad_words):
            print("Küfür algılandı")
            if(userSettings["language"] == "tr_TR"):
                await message.author.send("Küfür ettin! Küfür ettiğin için " + message.guild.name + " sunucusu tarafından uyarıldın!")
                with open("userSettings/"+str(message.author.id) + ".json","w") as file:
                    json.dump(userSettings,file)
                await message.delete()
                message = await message.channel.send(userMention + " " + "Hey onu gördüm!" + " Hyper polisi devrede VİYU VİYU VİYU!")
                sleep(delay)
                await message.delete()
                
            if(userSettings["language"] == "en_US"):
                await message.author.send("You sweared! and " + message.guild.name + " from be warned!!")
                with open("userSettings/"+str(message.author.id) + ".json","w") as file:
                    json.dump(userSettings,file)
                await message.delete()
                message = await message.channel.send(userMention + " " + "Hey onu gördüm!" + " Hyper polisi devrede VİYU VİYU VİYU!")
                sleep(delay)
                await message.delete()

    if any(antiAd in message.content for antiAd in antiAds):
        await message.delete()
        message = await message.channel.send(userMention + " " + "Hey o reklamı gördüm!" + " Hyper polisi devrede VİYU VİYU VİYU!")
        sleep(delay)
        await message.delete()



try:
    bot.run(token)
except:
    print("Error while trying to start bot.")
