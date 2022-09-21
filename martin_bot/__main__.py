import logging
from discord.ext import commands
from martin_bot.api import create_app
from martin_bot.util.args_util import parse_args
from martin_bot.util.logging_util import setup_logger
from martin_bot.core.cogs.general import GeneralCog

logger = logging.getLogger(__name__)

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

	if args.flask_host and args.flask_port:
		logger.info("Attempting to launch background Flask API.")
		try:
			app = create_app(seperate_thread = True)
			app.run(host = args.flask_host, port = args.flask_port)
			logger.info("Successful in launching background Flask API.")
		except Exception as e:
			logger.error(f"Failed launch of background Flask API with error: {str(e)}")
	bot = commands.Bot(command_prefix='$')
	bot.add_cog(GeneralCog(bot))
	logger.info("Attempting to run Zorak")
	bot.run(args.discord_token)


if __name__ == "__main__":
	main()