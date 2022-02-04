# graphdb.rdf4j.ContextsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_repository_contexts**](ContextsApi.md#get_repository_contexts) | **GET** /repositories/{repositoryID}/contexts | Gets a list of resources that are used as context identifiers.


# **get_repository_contexts**
> int get_repository_contexts(repository_id)

Gets a list of resources that are used as context identifiers.

The list is formatted as a tuple query result with a single variable ?contextID?, which is bound to URIs and bnodes that are used as context identifiers.

### Example
```python
from __future__ import print_function
import time
import graphdb.rdf4j
from graphdb.rdf4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.rdf4j.ContextsApi()
repository_id = 'repository_id_example' # str | The repository ID

try:
    # Gets a list of resources that are used as context identifiers.
    api_response = api_instance.get_repository_contexts(repository_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContextsApi->get_repository_contexts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The repository ID | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/sparql-results+xml, application/sparql-results+json, application/x-binary-rdf-results-table

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

