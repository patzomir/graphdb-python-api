# graphdb.graphdb_workbench.SavedQueriesControllerApi

All URIs are relative to *https://localhost:7200*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_query_using_post**](SavedQueriesControllerApi.md#create_query_using_post) | **POST** /rest/sparql/saved-queries | Create a new saved query
[**delete_sample_query_using_delete**](SavedQueriesControllerApi.md#delete_sample_query_using_delete) | **DELETE** /rest/sparql/saved-queries | Delete an existing saved query
[**edit_sample_query_using_put**](SavedQueriesControllerApi.md#edit_sample_query_using_put) | **PUT** /rest/sparql/saved-queries | Edit an existing saved query
[**get_queries_using_get**](SavedQueriesControllerApi.md#get_queries_using_get) | **GET** /rest/sparql/saved-queries | Get all saved queries visible for the user or single saved query by name and owner.


# **create_query_using_post**
> object create_query_using_post(query)

Create a new saved query

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.SavedQueriesControllerApi()
query = graphdb.graphdb_workbench.SavedQuery() # SavedQuery | query

try:
    # Create a new saved query
    api_response = api_instance.create_query_using_post(query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedQueriesControllerApi->create_query_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**SavedQuery**](SavedQuery.md)| query | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **delete_sample_query_using_delete**
> object delete_sample_query_using_delete(name=name)

Delete an existing saved query

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.SavedQueriesControllerApi()
name = 'name_example' # str | The name of the query (optional)

try:
    # Delete an existing saved query
    api_response = api_instance.delete_sample_query_using_delete(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedQueriesControllerApi->delete_sample_query_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the query | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **edit_sample_query_using_put**
> str edit_sample_query_using_put(query)

Edit an existing saved query

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.SavedQueriesControllerApi()
query = graphdb.graphdb_workbench.SavedQuery() # SavedQuery | query

try:
    # Edit an existing saved query
    api_response = api_instance.edit_sample_query_using_put(query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedQueriesControllerApi->edit_sample_query_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**SavedQuery**](SavedQuery.md)| query | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **get_queries_using_get**
> object get_queries_using_get(name=name, owner=owner)

Get all saved queries visible for the user or single saved query by name and owner.

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.SavedQueriesControllerApi()
name = 'name_example' # str | The name of the query (optional)
owner = 'owner_example' # str | owner (optional)

try:
    # Get all saved queries visible for the user or single saved query by name and owner.
    api_response = api_instance.get_queries_using_get(name=name, owner=owner)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedQueriesControllerApi->get_queries_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the query | [optional] 
 **owner** | **str**| owner | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

