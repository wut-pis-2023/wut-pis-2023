from slack_bot import SlackBot

SLACK_BOT_TOKEN = "xoxb-5165504015601-5213449868070-wuCsdpZxHh2FCKM3QifKqpP3"
SLACK_APP_TOKEN = "xapp-1-A0561ETAQPR-5384928614113-c7d3611daa7e3ce6dfe5227f780da3b8d7403a2f520ed822003e4ce24f884381"
WORKSPACE_NAME = "wut-pis-2023"


def main():
    slack_bot = SlackBot(token=SLACK_BOT_TOKEN, workspace_name=WORKSPACE_NAME)
    slack_bot.run(app_token=SLACK_APP_TOKEN)


if __name__ == '__main__':
    main()
