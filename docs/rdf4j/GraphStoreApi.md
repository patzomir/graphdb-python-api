# graphdb.rdf4j.GraphStoreApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_statements_to_indirect_namedgraph**](GraphStoreApi.md#add_statements_to_indirect_namedgraph) | **POST** /repositories/{repositoryID}/rdf-graphs/service | Add statements to an INDIRECTLY referenced named graph
[**add_statements_to_namedgraph**](GraphStoreApi.md#add_statements_to_namedgraph) | **POST** /repositories/{repositoryID}/rdf-graphs/{graph} | Add statements to a DIRECTLY referenced named graph
[**delete_statements_from_indirect_namedgraph**](GraphStoreApi.md#delete_statements_from_indirect_namedgraph) | **DELETE** /repositories/{repositoryID}/rdf-graphs/service | Clear an INDIRECTLY referenced named graph
[**delete_statements_from_namedgraph**](GraphStoreApi.md#delete_statements_from_namedgraph) | **DELETE** /repositories/{repositoryID}/rdf-graphs/{graph} | Clear a DIRECTLY referenced named graph
[**get_all_statements_from_indirect_namedgraph**](GraphStoreApi.md#get_all_statements_from_indirect_namedgraph) | **GET** /repositories/{repositoryID}/rdf-graphs/service | Fetch all statements from an INDIRECTLY referenced named graph
[**get_all_statements_from_namedgraph**](GraphStoreApi.md#get_all_statements_from_namedgraph) | **GET** /repositories/{repositoryID}/rdf-graphs/{graph} | Fetch all statements from a DIRECTLY referenced named graph


# **add_statements_to_indirect_namedgraph**
> int add_statements_to_indirect_namedgraph(repository_id, graph, rdf_data)

Add statements to an INDIRECTLY referenced named graph

Add statements to an INDIRECTLY referenced named graph.

### Example
```python
from __future__ import print_function
import time
import graphdb.rdf4j
from graphdb.rdf4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.rdf4j.GraphStoreApi()
repository_id = 'repository_id_example' # str | The repository ID
graph = 'graph_example' # str | Indirectly referenced named graph name. The named graph URI is mentioned as the value of this parameter. E.g. \"http://example.org/graph1\"
rdf_data = 'rdf_data_example' # str | Valid RDF data is some of the available formats.

try:
    # Add statements to an INDIRECTLY referenced named graph
    api_response = api_instance.add_statements_to_indirect_namedgraph(repository_id, graph, rdf_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphStoreApi->add_statements_to_indirect_namedgraph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The repository ID | 
 **graph** | **str**| Indirectly referenced named graph name. The named graph URI is mentioned as the value of this parameter. E.g. \&quot;http://example.org/graph1\&quot; | 
 **rdf_data** | **str**| Valid RDF data is some of the available formats. | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/rdf+xml, text/plain, text/turtle, text/rdf+n3, text/x-nquads, application/rdf+json, application/trix, application/x-trig, application/x-binary-rdf
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **add_statements_to_namedgraph**
> int add_statements_to_namedgraph(repository_id, graph, data)

Add statements to a DIRECTLY referenced named graph

Add statements to a DIRECTLY referenced named graph

### Example
```python
from __future__ import print_function
import time
import graphdb.rdf4j
from graphdb.rdf4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.rdf4j.GraphStoreApi()
repository_id = 'repository_id_example' # str | The repository ID
graph = 'graph_example' # str | IRI uniquely identifying a named graph. E.g. \"graph1\". The whole url is read as a named graph and statements from it can be retrieved.
data = 'data_example' # str | Valid RDF data is some of the available formats.

try:
    # Add statements to a DIRECTLY referenced named graph
    api_response = api_instance.add_statements_to_namedgraph(repository_id, graph, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphStoreApi->add_statements_to_namedgraph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The repository ID | 
 **graph** | **str**| IRI uniquely identifying a named graph. E.g. \&quot;graph1\&quot;. The whole url is read as a named graph and statements from it can be retrieved. | 
 **data** | **str**| Valid RDF data is some of the available formats. | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/rdf+xml, text/plain, text/turtle, text/rdf+n3, text/x-nquads, application/rdf+json, application/trix, application/x-trig, application/x-binary-rdf
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **delete_statements_from_indirect_namedgraph**
> int delete_statements_from_indirect_namedgraph(repository_id, graph)

Clear an INDIRECTLY referenced named graph

Clear an INDIRECTLY referenced named graph.

### Example
```python
from __future__ import print_function
import time
import graphdb.rdf4j
from graphdb.rdf4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.rdf4j.GraphStoreApi()
repository_id = 'repository_id_example' # str | The repository ID
graph = 'graph_example' # str | Indirectly referenced named graph name. The named graph URI is mentioned as the value of this parameter. E.g. \"http://example.org/graph1\"

try:
    # Clear an INDIRECTLY referenced named graph
    api_response = api_instance.delete_statements_from_indirect_namedgraph(repository_id, graph)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphStoreApi->delete_statements_from_indirect_namedgraph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The repository ID | 
 **graph** | **str**| Indirectly referenced named graph name. The named graph URI is mentioned as the value of this parameter. E.g. \&quot;http://example.org/graph1\&quot; | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **delete_statements_from_namedgraph**
> int delete_statements_from_namedgraph(repository_id, graph)

Clear a DIRECTLY referenced named graph

Clear a DIRECTLY referenced named graph.

### Example
```python
from __future__ import print_function
import time
import graphdb.rdf4j
from graphdb.rdf4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.rdf4j.GraphStoreApi()
repository_id = 'repository_id_example' # str | The repository ID
graph = 'graph_example' # str | IRI uniquely identifying a named graph. The whole url is read as a named graph and statements from it can be retrieved. E.g. \"graph1\"

try:
    # Clear a DIRECTLY referenced named graph
    api_response = api_instance.delete_statements_from_namedgraph(repository_id, graph)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphStoreApi->delete_statements_from_namedgraph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The repository ID | 
 **graph** | **str**| IRI uniquely identifying a named graph. The whole url is read as a named graph and statements from it can be retrieved. E.g. \&quot;graph1\&quot; | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **get_all_statements_from_indirect_namedgraph**
> int get_all_statements_from_indirect_namedgraph(repository_id, graph)

Fetch all statements from an INDIRECTLY referenced named graph

Fetch all statements from an INDIRECTLY referenced named graph.

### Example
```python
from __future__ import print_function
import time
import graphdb.rdf4j
from graphdb.rdf4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.rdf4j.GraphStoreApi()
repository_id = 'repository_id_example' # str | The repository ID
graph = 'graph_example' # str | Indirectly referenced named graph name. The named graph URI is mentioned as the value of this parameter. E.g. \"http://example.org/graph1\"

try:
    # Fetch all statements from an INDIRECTLY referenced named graph
    api_response = api_instance.get_all_statements_from_indirect_namedgraph(repository_id, graph)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphStoreApi->get_all_statements_from_indirect_namedgraph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The repository ID | 
 **graph** | **str**| Indirectly referenced named graph name. The named graph URI is mentioned as the value of this parameter. E.g. \&quot;http://example.org/graph1\&quot; | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/rdf+xml

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **get_all_statements_from_namedgraph**
> int get_all_statements_from_namedgraph(repository_id, graph)

Fetch all statements from a DIRECTLY referenced named graph

Fetch all statements from a DIRECTLY referenced named graph.

### Example
```python
from __future__ import print_function
import time
import graphdb.rdf4j
from graphdb.rdf4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.rdf4j.GraphStoreApi()
repository_id = 'repository_id_example' # str | The repository ID
graph = 'graph_example' # str | IRI uniquely identifying a named graph. After the request is executed the whole url is read as a named graph and statements from it can be retrieved. E.g. \"graph1\".

try:
    # Fetch all statements from a DIRECTLY referenced named graph
    api_response = api_instance.get_all_statements_from_namedgraph(repository_id, graph)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphStoreApi->get_all_statements_from_namedgraph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The repository ID | 
 **graph** | **str**| IRI uniquely identifying a named graph. After the request is executed the whole url is read as a named graph and statements from it can be retrieved. E.g. \&quot;graph1\&quot;. | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/rdf+xml

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

