import os
from procstream import ElasticSearchDataSinkService

config = {"MODULE_NAME": os.environ.get("MODULE_NAME", "LEWS_ES_INJECTOR"),
          "CONSUMER_GROUP": os.environ.get("CONSUMER_GROUP", "LEWS_ES_INJECTOR_CG")}


def main():
    elastic_search_datasink_service = ElasticSearchDataSinkService(config)
    elastic_search_datasink_service.start_service()


if __name__ == "__main__":
    main()
