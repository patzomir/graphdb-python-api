from graphdb.rdf4j.api.sparql_api import SparqlApi
from graphdb.rdf4j.configuration import Configuration
from graphdb.rdf4j.api_client import ApiClient
import json_stream

GRAPHDB_HOST = "http://localhost:7200"
GRAPHDB_REPO = "test"

def execute_query(query, type="query"):    
    conf = Configuration()
    conf.host = GRAPHDB_HOST
    api = SparqlApi(ApiClient(configuration=conf))
    repository = GRAPHDB_REPO
    if type == "query":
        with api.execute_get_select_query(repository, query, _preload_content=False, _return_http_data_only=True) as o:
            o.auto_close = False
            for y in json_stream.load(o)['results']["bindings"].persistent():
                yield y
                
for result in execute_query("select * { ?s ?p ?o } limit 1000"):
    print(f'{result["s"]["value"]} {result["p"]["value"]} {result["o"]["value"]}')
