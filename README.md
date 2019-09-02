# LEWS Kafka Elastic Search Injector

This module injects data from a kafka topic to Elasticsearch


## Running in local environment
### Install all dependancies
Install dependancies given in requirements.txt. You may add your dependancies in this file for you module
```bash
pip install -r requirements.txt
```
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
python Kafka-ES-Injector.py
```

## Running in Docker (Recommended for Production)
### Building the Docker Image


```bash
docker build --tag lews-pipeline-<module name> .
```

### Usage

```bash
docker run -e KAFKA_BROKER="<kafka-broker-host:port>" \
-e MODULE_SRC_TOPIC="<module name>" \
-e ES_HOST="<source topic for the module>" \
-e ES_INDEX="<target topic for the module>" \
-e ES_DOCTYPE="<elastic search document type>" lews-pipeline-<module name>
```
