
import discord
import logging
from discord.ext import commands
from pytrends.request import TrendReq
from datetime import datetime

logger = logging.getLogger(__name__)

class GoogleTrendsCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.pytrends = TrendReq(hl='en-US', tz=0)

	@commands.command(aliases=["dailytrends"])
	async def daily_search_trends(self, ctx):
		embed = {	
			"title": "Top 10 Worldwide Daily Search Trends",
			"color": 4903252,
			#"timestamp": str(datetime.now()),
			"footer": {
			"icon_url": "https://pjsoft.in/img/google-trends.png",
			"text": "Google Trends"
			},
			"thumbnail": {
			"url": "https://lawprofessors.typepad.com/.a/6a00d8341bfae553ef0282e115c64c200b-pi"
			},
			"fields":[]
		}
		results = self.pytrends.trending_searches()[0].to_list() #Update to do countries
		#[1,6,2,7,3,8,4,9,5,10]
		for i, rank in enumerate(range(1, 11)):
			embed["fields"].append({
			"name": f"{str(rank)}. {results[i]}",
			"value": "Stats coming soon...",
			"inline" : True
		})
		await ctx.send(embed=discord.Embed.from_dict(embed))


def setup(bot):
    bot.add_cog(GoogleTrendsCog(bot))

