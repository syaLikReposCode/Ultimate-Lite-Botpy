import discord as Discord
import os
import wikipedia
try:
 from googlesearch import search
except Exception as e:
  print(e)
from asyncio import TimeoutError
import fandom
from random import randint
from server import keep_alive
from discord.ext import commands

prefix = "f"
client = commands.Bot(command_prefix=prefix)
client.remove_command('help')
 
@client.event
async def on_ready():
  print("Logged in and register as {0.user}".format(client) + " With FORCE!") 
@client.event
async def on_message(message):
  if client.user.mentioned_in(message):
    await message.channel.send(f"\n**{prefix}**risk is a quiet human, she/he is the seventh (7th) "+
    f"human that fell down here **{prefix}**risk is a Neutral Girl/Boy Sometimes he/she does Genocide for fun only "+
   f"**{prefix}**risk followed chara because it is the main narrator for UNDERTALE he/she save/killer for the monsters in underground")
  elif message.author == client.user:
    return
  elif message.author.bot:
    return
  await client.process_commands(message)
  

@client.command()
async def help(ctx):
 colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1] 
 for colours in colors:
        i = int(randint(0, colours))
        embed=Discord.Embed(
       title=":snake: python command",
       color = i
        )
 embed.add_field(name=":question: General", value="Help, py", inline=True)
 embed.add_field(name=":mag: Searching", value="wiki, google, searchwiki, wikia, searchwikia", inline=False)
 await ctx.send(embed=embed)





@client.command()
async def wiki(ctx):
 try:
  try:
   await ctx.send("You're Looking For:")
   def check(msg):
         return msg.author == ctx.author and msg.channel == ctx.channel
   message = await client.wait_for("message", check=check, timeout=25)
   if message:
         text = (message.content)
         res = wikipedia.summary(text)
         if len(res) > 2000:
               await ctx.send("Article Exceeds Discord Limit")
         else:
               await ctx.send(res)
   else: 
         await ctx.send("Not Found.")
  except TimeoutError:
        await ctx.send("Timeout Reached, Searching Cancelled")
 except Exception as e:
       print(e)




@client.command()
async def py(ctx):
 try:
  try:
   await ctx.send("please write your code: ")
   def check(msg):
         return msg.author == ctx.author and msg.channel == ctx.channel
   message = await client.wait_for("message", check=check, timeout=25)
   if message:
         text = (message.content)
         space = text.join(' ')
         await ctx.send(exec(compile(space, "summary", "exec")))
  except TimeoutError:
       await ctx.send("Timeout Reached")
 except Exception as e:
       print(e)
       await ctx.send("Having problem while compiling your code")


@client.command()
async def searchwiki(ctx):
 await ctx.send("Search wiki page: ")
 try:
  try:
   def check(msg):
    return msg.author == ctx.author and msg.channel == ctx.channel
   message = await client.wait_for("message", check=check,timeout=25)
   text = (message.content)
   res = wikipedia.search(text)
   for result in res:
       await ctx.send("Here: " + f"**{result}**")

  except TimeoutError:
        await ctx.send("Timeout Reached, Cancelled Search")

 except Exception as e:
        print(e)
        await ctx.send("Could not find that wiki")




@client.command()
async def google(ctx):
 try:
  try:
   await ctx.send("Your Queries of Searching:")
   def check(msg):
         return msg.author == ctx.author and msg.channel == ctx.channel
   message = await client.wait_for("message", check=check, timeout=25)
   text = (message.content)
   for i in search(text, tld='com', num=10, stop=10, pause=2):
         await ctx.send(i)

  except TimeoutError:
        await ctx.send("Timeout Reached, Cancelled Search")
 except Exception as e:
       print(e)
       await ctx.send("Could not search your request")
       
@client.command()
async def secret(ctx):
  await ctx.send("https://tenor.com/view/tyler1-loltyler1-screaming-dead-wtf-gif-17500255")

@client.command()
async def wikia(ctx):
    try:
     await ctx.send("Title of page:")
     primstr = '-'
     def check(msg):
         return msg.author == ctx.author and msg.channel == ctx.channel
     message = await client.wait_for("message",check=check,timeout=7)
     try:
         if message:
             await ctx.send("page you're looking: ")
             message2 = await client.wait_for("message", check=check,timeout=7)
             try:
                 if message2:
                     msgparse = (message.content)
                     msg1parse = (message2.content)
                     msgstring = str(msgparse)
                     msg1string = str(msg1parse)
                     msgfinal = msgstring.replace(' ', primstr)
                     msg1final = msg1string.replace(' ', primstr)
                     fandom.set_wiki(msgfinal)
                     res = fandom.page(msg1final)
                     embed = Discord.Embed(
                         title = f"{res.title} \n {res.url}",
                         description = res.plain_text
                     )
                     await ctx.send(embed=embed)
             except TimeoutError:
                 await ctx.send("Timeout Reached.")
     except TimeoutError:
          await ctx.send("Timeout Reached.")
    except Exception as e:
        print(e)
        await ctx.send("could not find that article")



@client.command()
async def wikiasearch(ctx):
    try:
     await ctx.send("page of game:")
     def check(msg):
         return msg.author == ctx.author and msg.channel == ctx.channel
     message = await client.wait_for("message", check=check, timeout=7)
     try:
         text = (message.content)
         try:
          if message:
              await ctx.send("game page:")
              msg1 = await client.wait_for("message",check=check,timeout=7)
              text1 = (msg1.content)
              if msg1:
                  primstr = '-'
                  msgstr = str(text)
                  msg1str = str(text1)
                  msgfinal = msgstr.replace(' ', primstr)
                  msg1final = msg1str.replace(' ', primstr)
                  searchRes = fandom.search(msg1final, msgfinal)
                  for res in range(len(searchRes)):
                      print(res)
                      await ctx.send("Result: {}".format(searchRes[res]))
         except TimeoutError:
             await ctx.send("Timeout Reached.")
     except TimeoutError:
         await ctx.send("Timeout Reached.")
    except Exception as e:
        print(e)
        await ctx.send("Could not find that article")

keep_alive()
client.run(os.getenv('TOKEN'))
