import os
from keep_alive import keep_alive
from discord.ext import commands
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
import discord

bot = commands.Bot(
	command_prefix="!",
	case_insensitive=True
)

bot.author_id = 423013123599892482	

@bot.event 
async def on_ready():
	print("I'm in")
	print(bot.user)

extensions = [
	'cogs.cog_example'
]

@bot.command()
async def post(ctx, *args):
	await ctx.message.delete()
	contents = " ".join(args).split(" | ")
	
	webhook = await ctx.channel.create_webhook(name="e")
	if len(contents) > 4:
		embed = discord.Embed(title=contents[0]+" · "+contents[1], description=contents[2], color=discord.Color.blue(), avatar_url = contents[4])
		embed.set_image(url = contents[3])
		await webhook.send(username=contents[1], embed=embed, avatar_url = contents[3])
	elif len(contents) == 4:
		embed = discord.Embed(title=contents[0]+" · "+contents[1], description=contents[2], color=discord.Color.blue())
		embed.set_image(url = contents[3])
		await webhook.send(username=contents[1], embed=embed, avatar_url = contents[3])
		
	elif len(contents) == 3:
		embed = discord.Embed(title=contents[0]+" · "+contents[1], description=contents[2], color=discord.Color.blue())
		await webhook.send(username=contents[1], embed=embed)
		
	else:
		await ctx.send("You have not passed in sufficient arguments")
	
	webhooks = await ctx.channel.webhooks()
	for webhook in webhooks:
			await webhook.delete()
			
bot.run(os.environ['token'])