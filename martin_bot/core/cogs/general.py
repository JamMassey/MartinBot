
import discord
import logging
from discord.ext import commands
logger = logging.getLogger(__name__)

class GeneralCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def embed_help(self, ctx):
		embed = discord.Embed(title='Embed Helper',
							description='A visualiser to help style embeds!',
							colour=0x98FB98)
		embed.add_field(name='Visualizer', value='[Click Here!](https://leovoel.github.io/embed-visualizer/)')
		await ctx.send(embed=embed)
	
	@commands.command()	
	async def ping(self,ctx): 
		embed = discord.Embed(title="Pong",description=f"Martin's current ping is **{round(self.bot.latency * 1000)}ms**",timestamp=ctx.message.created_at,color=discord.Color.green())
		await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(GeneralCog(bot))


