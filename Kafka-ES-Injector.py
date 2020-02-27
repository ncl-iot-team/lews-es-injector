from abc import ABC, abstractmethod
from kafka import KafkaConsumer
import json
import os
from elasticsearch import Elasticsearch

kafka_servers = os.environ.get("KAFKA_BOOTSTRAP_SERVERS","localhost:9092").split(",")
kafka_listen_topic = os.environ.get('KAFKA_LISTEN_TOPIC', 't_topic').split(",")
es_host = os.environ.get('ES_HOST','elastic.technipun.com')
es_index = os.environ.get('ES_INDEX','lews-tweets')
es_doc_type = os.environ.get('ES_DOCTYPE','_doc')

print("Environment variables:")
print(f"KAFKA_BOOTSTRAP_SERVERS = {kafka_servers}")
print(f"KAFKA_LISTEN_TOPIC = {kafka_listen_topic}")
print(f"ES_HOST = {es_host}")
print(f"ES_INDEX = {es_index}")
print(f"ES_DOCTYPE = {es_doc_type}")

class KafkaElasticSearchInjector(ABC):
        

    def __init__(self,source_topic,es_host):

        self.processor_name = "ES Injector"
        
        self.source_topic = source_topic

        self.es_host = es_host

        self.es_index = es_index
        
        self.kafka_bootstrap_servers = kafka_servers 
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

   kafka_es_injector = KafkaElasticSearchInjector(kafka_listen_topic,es_host)

   for message in kafka_es_injector.consumer:
            try:
                kafka_es_injector.index_data(es_index,es_doc_type,message.value)
            except:
                print("Skipping Record..")




   
   
