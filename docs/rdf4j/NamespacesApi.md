# graphdb.rdf4j.NamespacesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_namespace_for_prefix**](NamespacesApi.md#delete_namespace_for_prefix) | **DELETE** /repositories/{repositoryID}/namespaces/{namespacesPrefix} | Remove namespace for a particular prefix
[**get_namespace_for_prefix**](NamespacesApi.md#get_namespace_for_prefix) | **GET** /repositories/{repositoryID}/namespaces/{namespacesPrefix} | Get namespace for a particular prefix
[**set_namespace_for_prefix**](NamespacesApi.md#set_namespace_for_prefix) | **PUT** /repositories/{repositoryID}/namespaces/{namespacesPrefix} | Set namespace for a particular prefix


# **delete_namespace_for_prefix**
> int delete_namespace_for_prefix(repository_id, namespaces_prefix)

Remove namespace for a particular prefix

Removes the namespace that has been defined for a particular prefix.

### Example
```python
from __future__ import print_function
import time
import graphdb.rdf4j
from graphdb.rdf4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.rdf4j.NamespacesApi()
repository_id = 'repository_id_example' # str | The repository ID
namespaces_prefix = 'namespaces_prefix_example' # str | URI prefix of a RDF resource

try:
    # Remove namespace for a particular prefix
    api_response = api_instance.delete_namespace_for_prefix(repository_id, namespaces_prefix)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespacesApi->delete_namespace_for_prefix: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The repository ID | 
 **namespaces_prefix** | **str**| URI prefix of a RDF resource | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **get_namespace_for_prefix**
> int get_namespace_for_prefix(repository_id, namespaces_prefix)

Get namespace for a particular prefix

Gets the namespace that has been defined for a particular prefix.

### Example
```python
from __future__ import print_function
import time
import graphdb.rdf4j
from graphdb.rdf4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.rdf4j.NamespacesApi()
repository_id = 'repository_id_example' # str | The repository ID
namespaces_prefix = 'namespaces_prefix_example' # str | URI prefix of a RDF resource

try:
    # Get namespace for a particular prefix
    api_response = api_instance.get_namespace_for_prefix(repository_id, namespaces_prefix)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespacesApi->get_namespace_for_prefix: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The repository ID | 
 **namespaces_prefix** | **str**| URI prefix of a RDF resource | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **set_namespace_for_prefix**
> int set_namespace_for_prefix(repository_id, namespaces_prefix, namespace)

Set namespace for a particular prefix

Sets a new namespace for a particular prefix.

### Example
```python
from __future__ import print_function
import time
import graphdb.rdf4j
from graphdb.rdf4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.rdf4j.NamespacesApi()
repository_id = 'repository_id_example' # str | The repository ID
namespaces_prefix = 'namespaces_prefix_example' # str | URI prefix of a RDF resource
namespace = 'namespace_example' # str | The new namespace to be set

try:
    # Set namespace for a particular prefix
    api_response = api_instance.set_namespace_for_prefix(repository_id, namespaces_prefix, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespacesApi->set_namespace_for_prefix: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The repository ID | 
 **namespaces_prefix** | **str**| URI prefix of a RDF resource | 
 **namespace** | **str**| The new namespace to be set | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

