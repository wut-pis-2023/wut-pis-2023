import logging

from pyspark.sql import SparkSession, DataFrame
import logging
import numpy as np
from sentence_transformers import SentenceTransformer, util
logger = logging.getLogger("slack-bot")


class SimilarSentenceIdentifier(object):
    def __init__(self):
        self.spark = SparkSession.builder.appName("similarity-model").getOrCreate()
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.df = None
        self.embeddings_links = None

    def read_json(self, path: str = "resources/first-model/2023-04-22.json", columns_for_model=None):
        if columns_for_model is None:
            columns_for_model = ["client_msg_id", "text"]
        self.df = self.spark.read.option("multiline", "true").json(path).select(columns_for_model)

    def read_slack_dict(self, data_dict: dict, columns_for_model=None):
        # get all_messages
        logger.info(f"Data is being added to the model")
        if columns_for_model is None:
            columns_for_model = ["link", "text"]
        for channel_id, messages in data_dict.items():
            if messages:
                self.df = self.spark.createDataFrame(data=messages).select(columns_for_model) 
                

    def preprocess(self):
        self.embeddings_links = self.preprocess_data(self.df)

    def preprocess_data(self, data: DataFrame):
        logger.info(f"Data is being preprocessed")
        data = data.na.drop(how="any")
        embeddings_links = [(link, self.model.encode(sentence
                    .lower()
                    .replace('br','')
                    .replace('<',"") 
                    .replace(">","")
                    .replace('\\',"")
                    .replace('\/',"")), sentence)
                    for link, sentence in data.rdd.collect()]
        
        return embeddings_links

    def get_similar(self, message: str, similarity_strength: float = 0.5):
        # Returns (link_to_message, original_message) sorted from the highest similarity
        logger.info(f"Similarity is being calculated")
        sentence_embedding = self.model.encode(message)
        all_embeddings = [embedding[1] for embedding in self.embeddings_links]
        cos_sim = util.cos_sim(sentence_embedding, np.array(all_embeddings))

        winners = []
        for arr in cos_sim:
            for i, similarity_score in enumerate(arr):
                if similarity_score > similarity_strength:
                    winners.append([self.embeddings_links[i], similarity_score])

        final_winners = sorted(winners, key=lambda x: x[1], reverse=True)
        logger.info(f"Found {len(final_winners)} winners including this message")
        
        return [(winner[0][0], winner[0][2]) for winner in final_winners]

# if __name__ == "__main__":
#     model = SimilarSentenceIdentifier()
#     data = {'first-model': [], 
#             'general': [
#                 {'id': '1685280174.002489', 'link': 'https://wut-pis-2023.slack.com/archives/C054DTJ1N6R/p1685280174002489', 'text': 'all channels'}, 
#                 {'id': '1685280126.018939', 'link': 'https://wut-pis-2023.slack.com/archives/C054DTJ1N6R/p1685280126018939', 'text': 'Hey there <@U0564GB1NS2>!\nYour message: hi\nLink to message: <https://wut-pis-2023.slack.com/archives/C054DTJ1N6R/p1685280124671849>'}, 
#                 {'id': '1685280124.671849', 'link': 'https://wut-pis-2023.slack.com/archives/C054DTJ1N6R/p1685280124671849', 'text': 'hi'}, 
#                 {'id': '1685279745.135749', 'link': 'https://wut-pis-2023.slack.com/archives/C054DTJ1N6R/p1685279745135749', 'text': 'is it?'}, 
#                 {'id': '1685279190.220799', 'link': 'https://wut-pis-2023.slack.com/archives/C054DTJ1N6R/p1685279190220799', 'text': 'Now the bot is running, but it needs time to initialized the spark session.'}, 
#                 {'id': '1685278668.396119', 'link': 'https://wut-pis-2023.slack.com/archives/C054DTJ1N6R/p1685278668396119', 'text': 'is it working'},
#                 {'id': '1685262889.800069', 'link': 'https://wut-pis-2023.slack.com/archives/C054GN4GTL3/p1685262889800069', 'text': 'hello'}, 
#                 {'id': '1682189675.223369', 'link': 'https://wut-pis-2023.slack.com/archives/C054GN4GTL3/p1682189675223369', 'text': 'No pls get to work'}
#             ]}
#     model.read_slack_dict(data)
#     model.preprocess()
#     print(model.get_similar('ways to export files from slack'))
