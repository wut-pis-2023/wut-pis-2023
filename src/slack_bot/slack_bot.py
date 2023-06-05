import os
import logging

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from src.model.similarity_model import SimilarSentenceIdentifier

load_dotenv()
logger = logging.getLogger("slack-bot")


class SlackBot:
    def __init__(self, token, workspace_name):
        self.token = token
        self.workspace_name = workspace_name
        self.client = WebClient(token=token)
        self.app = App(token=token)
        self.model = SimilarSentenceIdentifier()

        @self.app.message()
        def say_hello(message, say):
            MESSAGE_SHORTCUT_LEN = 20
            text = message.get('text')
            channel_id = message.get('channel')
            message_id = message.get('ts')
            logger.info(f"Message: '{text}' is being analyzed")
            
            logger.info(f"Retrieving all messages")
            all_messages = self.read_all_messages()
            print(all_messages)
            self.model.read_slack_dict(data_dict=all_messages, columns_for_model=["link", "text"])
            self.model.preprocess()
            similar_messages = self.model.get_similar(message=text, similarity_strength=0.5)
            
            if len(similar_messages) > 1:
                similar_messages_str = ""
                for link_, message_ in similar_messages:
                    # Ignore the message_ that bot replies to
                    if link_ == self.get_message_link(channel_id, message_id):
                        continue
                    similar_messages_str += f"Message: '{message_[:MESSAGE_SHORTCUT_LEN]}...'\t Link: {link_}\n"           
                say(f"Hey there <@{message['user']}>!\nTheese messages seem to be similar to yours:\n{similar_messages_str}")
            else:
                logger.info("No similar messages found")
                

    def get_message_link(self, channel_id, message_id):
        return f"https://{self.workspace_name}.slack.com/archives/{channel_id}/p{message_id.replace('.', '')}"

    def get_all_channels(self):
        try:
            response = self.client.conversations_list(types='public_channel')
            channels = response['channels']
            return channels
        except SlackApiError as e:
            print(f'Error fetching channels: {e}')
            return []

    def get_messages_from_channel(self, channel_id):
        try:
            response = self.client.conversations_history(channel=channel_id)
            messages = response['messages']

            all_messages = []

            for message in messages:
                if message.get('subtype') is None and message.get('bot_id')!=self.app.client.auth_test().get("bot_id"):
                    message_id = message.get('ts')
                    all_messages.append({
                        'id': message_id,
                        'link': f"https://{self.workspace_name}.slack.com/archives/{channel_id}/p{message_id.replace('.', '')}",
                        'text': message.get('text')
                    })

            return all_messages
        except SlackApiError as e:
            print(f'Error fetching messages for channel {channel_id}: {e}')
            return []

    def read_all_messages(self) -> dict:

        """
        Retrieves all messages from all PUBLIC channels the bot has access to and organizes them by channel.

        :return: dict: A dictionary with channel names as keys and lists of message data as values.
                       Each message data is a dictionary containing 'id', 'link' and 'text' keys.


        Example:
            {
                'first-model': [],
                'general': [
                    {
                        'id': '1683311113.605389',
                        'link': 'https://wut-pis-2023.slack.com/archives/C054DTJ1N6R/p1683311113605389',
                        'text': 'Hi! Nice to meet you all'
                    },
                    ...
                ],
                'random': []
            }

        """

        channels = self.get_all_channels()
        all_messages = {}

        for channel in channels:
            channel_id = channel['id']
            channel_messages = self.get_messages_from_channel(channel_id)
            all_messages[channel['name']] = channel_messages

        return all_messages

    def run(self, app_token):
        print('Running app')
        handler = SocketModeHandler(self.app, app_token)
        handler.start()
