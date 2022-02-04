# graphdb.rdf4j.ProtocolApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_protocol_version**](ProtocolApi.md#get_protocol_version) | **GET** /protocol | Fetch the protocol version


# **get_protocol_version**
> int get_protocol_version()

Fetch the protocol version

The version of the protocol that the server uses to communicate over HTTP.

### Example
```python
from __future__ import print_function
import time
import graphdb.rdf4j
from graphdb.rdf4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.rdf4j.ProtocolApi()

try:
    # Fetch the protocol version
    api_response = api_instance.get_protocol_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolApi->get_protocol_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

