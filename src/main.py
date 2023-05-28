from slack_bot import SlackBot

SLACK_BOT_TOKEN = "xoxb-5165504015601-5336983364548-pZKSE4r8lJOUMGVSPV75uolZ"
SLACK_APP_TOKEN = "xapp-1-A059UAF9KGB-5331541385349-aab24a49dab98911db6ee3d48391e33576eec8368fd98cfa30af702374996c60"
WORKSPACE_NAME = "wut-pis-2023"


def main():
    slack_bot = SlackBot(token=SLACK_BOT_TOKEN, workspace_name=WORKSPACE_NAME)
    slack_bot.run(app_token=SLACK_APP_TOKEN)


if __name__ == '__main__':
    main()
