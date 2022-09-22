
import discord
import logging
from discord.ext import commands
from datetime import datetime

logger = logging.getLogger(__name__)

class FinanceCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases=["stockprice"])
	async def daily_stock_price(self, ctx, ticker):
		embed = discord.Embed.from_dict({	
			"title": f"Daily Price for {ticker}",
			"color": 4903252,
			#"timestamp": str(datetime.now()),
			"footer": {
			"icon_url": "https://play-lh.googleusercontent.com/jQVXIz4MbsuOJSzoeFsTeL2gHoaZTlBtz2JbyG9JAuhsrTPB2vSvsRqsINWYVUr3Xw",
			"text": "Yahoo Finance"
			}
		})
		await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(FinanceCog(bot))
