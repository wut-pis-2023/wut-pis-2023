from src.slack_bot.slack_bot import slackbot_main
from logging_config import logging_config

logging_config()

if __name__ == "__main__":
    slackbot_main()