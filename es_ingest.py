import os
from procstream import ElasticSearchDataSinkService

config = {"ES_MAXSIZE": os.environ.get("ES_MAXSIZE", "25"),
          "ES_SNIFFER_TIMEOUT": os.environ.get("ES_SNIFFER_TIMEOUT", "60"),
          "MODULE_NAME": os.environ.get("MODULE_NAME", "LEWS_ES_INJECTOR"),
          "CONSUMER_GROUP": os.environ.get("CONSUMER_GROUP", "LEWS_ES_INJECTOR_CG"),
          "ES_HOST": os.environ.get('ES_HOST', ''),
          "ES_INDEX": os.environ.get('ES_INDEX', ''),
          "ES_DOCTYPE": os.environ.get('ES_DOCTYPE', '_doc')
          }


def main():
    elastic_search_datasink_service = ElasticSearchDataSinkService(config)
    elastic_search_datasink_service.start_service()


if __name__ == "__main__":
    main()
