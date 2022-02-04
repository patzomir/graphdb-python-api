from graphdb.rdf4j.api.sparql_api import SparqlApi
from graphdb.rdf4j.configuration import Configuration
from graphdb.rdf4j.api_client import ApiClient



conf = Configuration()
conf.host = "http://nova-dev/graphdb/"
api = SparqlApi(ApiClient(configuration=conf))
repository = "novasenta"
print(api.execute_get_select_query(repository, "select * {?s ?p ?o} limit 10", _return_http_data_only=True))
    