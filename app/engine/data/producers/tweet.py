import tweepy
from confluent_kafka.avro import AvroProducer


class TweetStreamClient(tweepy.StreamingClient):

    def __init__(self, *args, **kwargs):
        super(TweetStreamClient, self).__init__(*args, **kwargs)
        self.kafka_producer = None
