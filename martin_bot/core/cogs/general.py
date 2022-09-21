
import discord
from discord.ext import commands

class GeneralCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def embed(self, ctx):

        embed = discord.Embed(title='Example Embed',
                              description='Showcasing the use of Embeds...\nSee the visualizer for more info.',
                              colour=0x98FB98)
        embed.set_author(name='MysterialPy',
                         url='https://gist.github.com/MysterialPy/public',
                         icon_url='http://i.imgur.com/ko5A30P.png')
        embed.set_image(url='https://cdn.discordapp.com/attachments/84319995256905728/252292324967710721/embed.png')

        embed.add_field(name='Embed Visualizer', value='[Click Here!](https://leovoel.github.io/embed-visualizer/)')
        embed.add_field(name='Command Invoker', value=ctx.author.mention)
        embed.set_footer(text='Made in Python with discord.py@rewrite', icon_url='http://i.imgur.com/5BFecvA.png')
        await ctx.send(content='**A simple Embed for discord.py@rewrite in cogs.**', embed=embed)
	
	# def ping(ctx, bot): 
	# await discord.Embed(
	# 	title="Pong",
	# 	description=f"Martin's current ping is **{round(bot.latency * 1000)}ms**",
	# 	timestamp=ctx.message.created_at,
	# 	color=discord.Color.green())

def setup(bot):
    bot.add_cog(GeneralCog(bot))


