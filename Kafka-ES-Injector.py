from abc import ABC, abstractmethod
from kafka import KafkaConsumer, KafkaProducer
import json
import os
from elasticsearch import Elasticsearch

class KafkaElasticSearchInjector(ABC):
        

    def __init__(self,source_topic,es_host):

        self.processor_name = "ES Injector"
        
        self.source_topic = source_topic

        self.es_host = es_host

        self.es_index = es_index
        
        self.kafka_bootstrap_servers = os.getenv('KAFKA_BROKER','host.docker.internal:9092')
        #self.bootstrap_servers = 'localhost:9092'
        
        print("Initializing Kafka Consumer")
        
        self.consumer = KafkaConsumer(source_topic,group_id = self.processor_name, kafka_bootstrap_servers = self.kafka_bootstrap_servers,value_deserializer=lambda m: json.loads(m.decode('utf-8')))

        print("Initializing ES Injector Module")

        self.es = Elasticsearch([self.es_host], maxsize=25, sniff_on_start=True, sniff_on_connection_fail=True, sniffer_timeout=60,retry_on_timeout=True)


    def index_data(self,es_index,es_doc_type, body):
        res=self.es.index(index=es_index, doc_type=es_doc_type, body=body)
        print(res['result'])





if __name__ == "__main__":

    #processor_name: Unique processor name for the module, 
    #source_topic: Topic from which the module should accept the record to be processed, 
    # target_topic: Topic to which the module publishes the processed record
   s_topic = os.getenv('MODULE_SRC_TOPIC','lews-twitter')
   es_host = os.getenv('ES_HOST','elastic.technipun.com')
   es_index = os.getenv('ES_INDEX','lews-tweets')
   es_doc_type =os.getenv('ES_DOCTYPE','lews_tweet')

   kafka_es_injector = KafkaElasticSearchInjector(s_topic,es_host)

   for message in kafka_es_injector.consumer:
            try:
                kafka_es_injector.index_data(es_index,es_doc_type,message.value)
            except:
                print("Skipping Record..")




   
   
