# LEWS Kafka Elastic Search Injector

This module injects data from a kafka topic to Elasticsearch


## Running in local environment

### Install and run Kafka Broker
#### Ubuntu 18.04
Follow https://www.digitalocean.com/community/tutorials/how-to-install-apache-kafka-on-ubuntu-18-04
#### Windows 
Follow https://medium.com/@shaaslam/installing-apache-kafka-on-windows-495f6f2fd3c8
#### MacOS
Follow https://medium.com/pharos-production/apache-kafka-macos-installation-guide-a5a3754f09c

### Running the module
Install dependancies given in requirements.txt. Add all module dependancies in this file
```bash
pip install -r requirements.txt
```

Running
```bash
python es_ingest.py
```

## Running in Docker (Recommended for Production)
### Building the Docker Image


```bash
docker build --tag lews-es-injector .
```

### Usage

```bash
docker run -e KAFKA_SOURCE_BOOTSTRAP_SERVERS="<comma separated kafka-broker-host:port>" \
-e KAFKA_SOURCE_TOPIC="<module name>" \
-e CONSUMER_GROUP="<consumer group name>" \
-e ES_HOST="<source topic for the module>" \
-e ES_INDEX="<target topic for the module>" \
-e ES_DOCTYPE="<elastic search document type>" lews-pipeline-<module name>
```
