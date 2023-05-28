from src.logger.helpers import config_logging
from src.slack_bot.slack_bot import slackbot_main


if __name__ == "__main__":
    config_logging(0)
    slackbot_main()
