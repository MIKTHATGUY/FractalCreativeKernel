
import discord
import asyncio
import time
import sys
import os
import keep_alive
import discord
import helper


from discord.ext import commands
client = commands.Bot(command_prefix='$')
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "24.7sempreonn@gmail.com"  # Enter your address
receiver_email = "24.7sempreonn@gmail.com"  # Enter receiver address
password = "sasso1234"
messageg = """\
Subject: NOW YOU ARE DEAD

SOS."""


@client.event
async def on_ready():
 import os

 await client.change_presence(activity=discord.Activity(type=3, name=f' {len(client.guilds)} servers $help is not setupped yet', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=PLahKLy8pQdCM0SiXNn3EfGIXX19QGzUG3', platform='YouTube'))
 print("lal")
   


  


@client.command()
async def hello(ctx):
	await ctx.send("LOL")


@client.event
async def on_member_join(member):
	channel = discord.utils.get(member.guild.channel, name="🎅generale🎅")
	await channel.send(f"bob il coglione {member.mention} che michia fai")


@client.command()
async def coc(ctx):
	embed = discord.Embed(color=discord.Color.gold())
	embed.add_field(
	    name="ma io che cazzo ne so", value="DIO BESTIA ps lo devo cambiare")
	await ctx.send(embed=embed)


@client.command()
async def clearchannel(ctx, amountt=100):
	await ctx.send("lol")

	await ctx.channel.purge(limit=amountt)

	await ctx.send("SIUM {0.user} li ha cancellati TROIETTE ne ha cnacellati".
	               format(client) + f"lol {amountt}")


@client.command()
async def dm(ctx, *, member: discord.Member):
	await ctx.send('what you want to say')

	def check(m):
		return m.author.id == ctx.author.id

	messagef = await client.wait_for('message', check=check)
	await ctx.send(f'send message to{member}')
	await member.send(f'{messagef.content}')


@client.command()
async def email(ctx, amount=4):
	await ctx.send('what you want to say')

	messagez = await client.wait_for('message')

	await ctx.send('a chi?')

	messa = await client.wait_for('message')

	if (messa.author.id == messagez.author.id):
		try:
			assert False
			context = ssl.create_default_context()
			with smtplib.SMTP_SSL(
			    smtp_server, port, context=context) as server:
				server.login(sender_email, password)
				server.sendmail(sender_email, messa.content, messagez.content)

			await ctx.channel.purge(limit=1)
			await ctx.send("mandato a", receiver_email)
		except AssertionError:
			await ctx.channel.purge(limit=1)
			pass

		finally:
			print("lol")
			await ctx.channel.purge(limit=amount)
			await ctx.send("mandato")
			member = messa.author

			embed = discord.Embed(title="mail_sended_from", color=0xffee00)
			embed.add_field(name="to", value=f"{messa.content}", inline=False)
			embed.add_field(name="from", value=f"{sender_email}", inline=False)
			embed.add_field(
			    name="text", value=f"{messagez.content}", inline=True)
			embed.set_footer(text="by 24/7 sempre on")

			file_object = open('lol.txt', 'a')
			# Append 'hello' at the end of file
			file_object.write("\n" + f"[{messagez.author.nick}]" +
			                  "  lo ha mandato a  " + f"[{messa.content}]")
			# Close the file
			file_object.close()

			await member.send(embed=embed)

			print("SIUUUM")
	else:
		await ctx.send("tu non puoi disabiliterò queste risposte")
		time.sleep(3)
		await ctx.channel.purge(limit=10)


def is_it_me(ctx):
	ctx.author.id == 683704664168071168


@client.command()
@commands.check(is_it_me)
async def dm_all(ctx, *, args=None):
	members = ctx.guild.members
	print(members)
	for member in members:
		await member.send(args)
		print("'" + args + "' sent to: " + member.name)


@client.command()
async def pingg(ctx):
	await ctx.send(f"pong {round(client.latency * 1000)} ms")


@client.command()
async def conversazionesegreta(ctx, amountt=30):
	await ctx.send("avete 1 minuto per parlare poi cancellerò tutto")
	time.sleep(10)
	await ctx.channel.purge(limit=amountt)
	await ctx.send("la vostra conversazione è stata eliminata con successo")

@client.command()
async def misentosolo(ctx, amountt=30):
    if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel")
        return
    
    else:
        channel = ctx.message.author.voice.channel

    await channel.connect()



  
@client.command()
async def napoli(ctx, amountt=30):
    channel = ctx.message.author.voice.channel


    await ctx.send(f"oh cazzo sta per derubarmi scappate anche voi da")
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()



     




keep_alive.keep_alive()
client.run(TOKEN)
