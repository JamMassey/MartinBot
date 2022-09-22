import logging
import os
import discord
from discord.ext import commands
from api import create_app
from util.args_util import parse_args
from util.logging_util import setup_logger
from util import clean_path
import asyncio
logger = logging.getLogger(__name__)
bot = commands.Bot(command_prefix="$$")

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="The Market"))

#Don't worry about this - this is the part that grabs all individual functionality/commands from our cogs and attatches them to our bot.  
#Cogs are simply a grouping of bot commands, if getting technical they allow us to build class based objects while allowing us to pass about the instance of our bot for use.
async def load_cogs():
	logger.info("Attempting to load Cogs")
	path = clean_path('martin_bot/core/cogs')
	for file in os.listdir(path):
		if file.endswith('.py'):
			cog_name = f"core.cogs.{file[:-3]}"
			try:
				bot.load_extension(cog_name)
				logger.info(f'Loaded Extension {cog_name}')
			except Exception as e:
				exc = f'{type(e).__name__}: {e}'
				logger.info(f'Failed to load extension {cog_name}: {exc}')


def main() -> None:
	args = parse_args()
	setup_logger(
        level=args.log_level,
        stream_logs=args.console_log,
		log_file=args.log_file,
		err_file=args.err_file
    )
	logger.info(f"Arguments Passed {args}")
	logger.info("Logger initialised")

	#Optional Background API
	if args.flask_host and args.flask_port:
		logger.info("Attempting to launch background Flask API.")
		try:
			app = create_app(seperate_thread = True)
			app.run(host = args.flask_host, port = args.flask_port)
			logger.info("Successful in launching background Flask API.")
		except Exception as e:
			logger.error(f"Failed launch of background Flask API with error: {str(e)}")

	#Load our cogs and run		
	asyncio.run(load_cogs())
	logger.info("Attempting to run Martin")
	bot.run(args.discord_token)


if __name__ == "__main__":
	main()