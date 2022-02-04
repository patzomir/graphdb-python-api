# graphdb.rdf4j.SparqlApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_get_select_query**](SparqlApi.md#execute_get_select_query) | **GET** /repositories/{repositoryID} | Send queries on a specific repository with ID. This resource represents a SPARQL query endpoint
[**update**](SparqlApi.md#update) | **POST** /repositories/{repositoryID}/statements | Performs updates on the data in the repository


# **execute_get_select_query**
> int execute_get_select_query(repository_id, query, query_ln=query_ln, infer=infer, varname=varname, timeout=timeout, distinct=distinct, limit=limit, offset=offset)

Send queries on a specific repository with ID. This resource represents a SPARQL query endpoint

The main endpoint that is responsible for sending queries to a particular repository

### Example
```python
from __future__ import print_function
import time
import graphdb.rdf4j
from graphdb.rdf4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.rdf4j.SparqlApi()
repository_id = 'repository_id_example' # str | The repository ID
query = 'query_example' # str | The query to evaluate
query_ln = 'query_ln_example' # str | Specifies the query language that is used for the query. Acceptable values are strings denoting the query languages supported by the server, i.e. 'serql' for SeRQL queries and 'sparql' for SPARQL queries. If not specified, the server assumes the query is a SPARQL query (optional)
infer = true # bool | Specifies whether inferred statements should be included in the query evaluation. Inferred statements are included by default. Specifying any value other than 'true' (ignoring case) restricts the query evluation to explicit statements only. (optional)
varname = 'varname_example' # str | Specifies variable bindings. Variables appearing in the query can be bound to a specific value outside the actual query using this option. The value should be an N-Triples encoded RDF value. (optional)
timeout = 56 # int | Specifies a maximum query execution time, in whole seconds. The value should be an integer. A setting of 0 or a negative number indicates unlimited query time (the default). (optional)
distinct = true # bool | Specifies if only distinct query solutions should be returned. The value should be true or false. If the supplied SPARQL query itself already has a DISTINCT modifier, this parameter will have no effect. (optional)
limit = 56 # int | Specifies the maximum number of query solutions to return. The value should be a positive integer. If the supplied SPARQL query itself already has a LIMIT modifier, this parameter will only have an effect if the supplied value is lower than the LIMIT value in the query. (optional)
offset = 56 # int | Specifies the number of query solutions to skip. The value should be a positive integer. This parameter is cumulative with any OFFSET modifier in the supplied SPARQL query itself. (optional)

try:
    # Send queries on a specific repository with ID. This resource represents a SPARQL query endpoint
    api_response = api_instance.execute_get_select_query(repository_id, query, query_ln=query_ln, infer=infer, varname=varname, timeout=timeout, distinct=distinct, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SparqlApi->execute_get_select_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The repository ID | 
 **query** | **str**| The query to evaluate | 
 **query_ln** | **str**| Specifies the query language that is used for the query. Acceptable values are strings denoting the query languages supported by the server, i.e. &#39;serql&#39; for SeRQL queries and &#39;sparql&#39; for SPARQL queries. If not specified, the server assumes the query is a SPARQL query | [optional] 
 **infer** | **bool**| Specifies whether inferred statements should be included in the query evaluation. Inferred statements are included by default. Specifying any value other than &#39;true&#39; (ignoring case) restricts the query evluation to explicit statements only. | [optional] 
 **varname** | **str**| Specifies variable bindings. Variables appearing in the query can be bound to a specific value outside the actual query using this option. The value should be an N-Triples encoded RDF value. | [optional] 
 **timeout** | **int**| Specifies a maximum query execution time, in whole seconds. The value should be an integer. A setting of 0 or a negative number indicates unlimited query time (the default). | [optional] 
 **distinct** | **bool**| Specifies if only distinct query solutions should be returned. The value should be true or false. If the supplied SPARQL query itself already has a DISTINCT modifier, this parameter will have no effect. | [optional] 
 **limit** | **int**| Specifies the maximum number of query solutions to return. The value should be a positive integer. If the supplied SPARQL query itself already has a LIMIT modifier, this parameter will only have an effect if the supplied value is lower than the LIMIT value in the query. | [optional] 
 **offset** | **int**| Specifies the number of query solutions to skip. The value should be a positive integer. This parameter is cumulative with any OFFSET modifier in the supplied SPARQL query itself. | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/sparql-results+xml, application/sparql-results+json, application/x-binary-rdf-results-table

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **update**
> update(repository_id, update=update, base_uri=base_uri)

Performs updates on the data in the repository

The data supplied with this request is expected to contain either an RDF document, a SPARQL 1.1 Update string, or a special purpose transaction document. If an RDF document is supplied, the statements found in the RDF document will be added to the repository. If a SPARQL 1.1 Update string is supplied, the update operation will be parsed and executed. If a transaction document is supplied, the updates specified in the transaction document will be executed.

### Example
```python
from __future__ import print_function
import time
import graphdb.rdf4j
from graphdb.rdf4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.rdf4j.SparqlApi()
repository_id = 'repository_id_example' # str | The repository ID
update = 'update_example' # str | Only relevant for POST operations. Specifies the SPARQL 1.1 Update string to be executed. The value is expected to be a syntactically valid SPARQL 1.1 Update string. (optional)
base_uri = 'base_uri_example' # str | Specifies the base URI to resolve any relative URIs found in uploaded data against. This parameter only applies to the PUT and POST method. (optional)

try:
    # Performs updates on the data in the repository
    api_instance.update(repository_id, update=update, base_uri=base_uri)
except ApiException as e:
    print("Exception when calling SparqlApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The repository ID | 
 **update** | **str**| Only relevant for POST operations. Specifies the SPARQL 1.1 Update string to be executed. The value is expected to be a syntactically valid SPARQL 1.1 Update string. | [optional] 
 **base_uri** | **str**| Specifies the base URI to resolve any relative URIs found in uploaded data against. This parameter only applies to the PUT and POST method. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/rdf+xml, text/plain, text/turtle, text/rdf+n3, text/x-nquads, application/rdf+json, application/trix, application/x-trig, application/x-binary-rdf
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

