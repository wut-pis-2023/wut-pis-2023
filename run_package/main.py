from slack_bot.slack_bot import slackbot_main
from slack_bot.slack_bot import logging_config

if __name__ == "__main__":
    logging_config()
    slackbot_main()
