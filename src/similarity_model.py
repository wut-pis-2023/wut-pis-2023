# !pip install pyspark
# !pip install -U sentence-transformers

from pyspark.sql import SparkSession, DataFrame
import numpy as np
from sentence_transformers import SentenceTransformer, util

class SimilarSentenceIdentifier(object):
    def __init__(self):
        self.spark = SparkSession.builder.appName("similarity-model").getOrCreate()
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.df= None
        self.embeddings_links=None
        
    def read_json(self, path:str="resources/first-model/2023-04-22.json", columns_for_model=["client_msg_id", "text"]):
        self.df = self.spark.read.option("multiline", "true").json(path).select(columns_for_model)
        
    def read_slack_dict(self, data_dict:dict, columns_for_model=["link", "text"]):
        # get all_messages
        for channel_id, messages in data_dict.items():
            for message_dict in messages:
                self.df = self.spark.createDataFrame(message_dict).select(columns_for_model) 
        
    def preprocess(self):
        self.embeddings_links = self.preprocess_data(self.df)

    def preprocess_data(self, data: DataFrame):
        data = data.na.drop(how="any")                
        embeddings_links = [(link, self.model.encode(sentence
                    .lower()
                    .replace('br','')
                    .replace('<',"") 
                    .replace(">","")
                    .replace('\\',"")
                    .replace('\/',"")))
                    for link, sentence in data.rdd.collect()]
        return embeddings_links
        
    def get_similar(self, message:str, similarity_strength:int=0.25):
        sentence_embedding = self.model.encode(message)
        all_embeddings = [embedding[1] for embedding in self.embeddings_links]
        print(sentence_embedding, all_embeddings)
        cos_sim = util.cos_sim(sentence_embedding, np.array(all_embeddings))

        winners = []
        for arr in cos_sim:
            for i, similarity_score in enumerate(arr):
                if(similarity_score>0.25):
                    winners.append([self.embeddings_links[i], similarity_score])

        final_winners = sorted(winners, key=lambda x: x[1], reverse=True)
        return [winner[0][0] for winner in final_winners]

if __name__ == "__main__":
    model = SimilarSentenceIdentifier()
    model.read_json()
    model.preprocess()
    print(model.get_similar('ways to export files from slack'))