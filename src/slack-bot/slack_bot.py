import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

load_dotenv()

SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')
SLACK_APP_TOKEN = os.getenv('SLACK_APP_TOKEN')
WORKSPACE_NAME = os.getenv('WORKSPACE_NAME')


class SlackBot:
    def __init__(self, token, workspace_name):
        self.token = token
        self.workspace_name = workspace_name
        self.app = App(token=token)

        @self.app.message()
        def say_hello(message, say):
            text = message.get('text')
            channel_id = message.get('channel')
            message_id = message.get('ts')

            say(f"Hey there <@{message['user']}>!\nYour message: {text}\nLink to message: {self.get_message_link(channel_id, message_id)}")

    def get_message_link(self, channel_id, message_id):
        return f"https://{self.workspace_name}.slack.com/archives/{channel_id}/p{message_id.replace('.', '')}"

    def run(self, app_token):
        handler = SocketModeHandler(self.app, app_token)
        handler.start()


def main():
    slack_bot = SlackBot(token=SLACK_BOT_TOKEN, workspace_name=WORKSPACE_NAME)
    slack_bot.run(app_token=SLACK_APP_TOKEN)


if __name__ == '__main__':
    main()
