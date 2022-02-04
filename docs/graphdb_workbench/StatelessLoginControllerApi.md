# graphdb.graphdb_workbench.StatelessLoginControllerApi

All URIs are relative to *https://localhost:7200*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_using_post**](StatelessLoginControllerApi.md#login_using_post) | **POST** /rest/login/** | Authenticate user with a password


# **login_using_post**
> UserDetails login_using_post(x_graph_db_password)

Authenticate user with a password

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.StatelessLoginControllerApi()
x_graph_db_password = 'x_graph_db_password_example' # str | X-GraphDB-Password

try:
    # Authenticate user with a password
    api_response = api_instance.login_using_post(x_graph_db_password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatelessLoginControllerApi->login_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_graph_db_password** | **str**| X-GraphDB-Password | 

### Return type

[**UserDetails**](UserDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

