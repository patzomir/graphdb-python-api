# graphdb.graphdb_workbench.LocationManagementControllerApi

All URIs are relative to *https://localhost:7200*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_location_using_post**](LocationManagementControllerApi.md#activate_location_using_post) | **POST** /rest/locations/activate | Activate a connected GraphDB location
[**add_location_using_post**](LocationManagementControllerApi.md#add_location_using_post) | **POST** /rest/locations | Connect to a remote GraphDB location
[**change_location_using_put**](LocationManagementControllerApi.md#change_location_using_put) | **PUT** /rest/locations | Modify settings for a connected GraphDB location
[**delete_location_using_delete**](LocationManagementControllerApi.md#delete_location_using_delete) | **DELETE** /rest/locations | Disconnect a GraphDB location
[**get_active_location_using_get**](LocationManagementControllerApi.md#get_active_location_using_get) | **GET** /rest/locations/active | Get active connected GraphDB location
[**get_all_using_get**](LocationManagementControllerApi.md#get_all_using_get) | **GET** /rest/locations | Get all connected GraphDB locations
[**set_default_repository_using_post**](LocationManagementControllerApi.md#set_default_repository_using_post) | **POST** /rest/locations/active/default-repository | Set default repository for active GraphDB location


# **activate_location_using_post**
> str activate_location_using_post(location_uri)

Activate a connected GraphDB location

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.LocationManagementControllerApi()
location_uri = graphdb.graphdb_workbench.LocationUri() # LocationUri | locationUri

try:
    # Activate a connected GraphDB location
    api_response = api_instance.activate_location_using_post(location_uri)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationManagementControllerApi->activate_location_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_uri** | [**LocationUri**](LocationUri.md)| locationUri | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **add_location_using_post**
> str add_location_using_post(location)

Connect to a remote GraphDB location

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.LocationManagementControllerApi()
location = graphdb.graphdb_workbench.Location() # Location | location

try:
    # Connect to a remote GraphDB location
    api_response = api_instance.add_location_using_post(location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationManagementControllerApi->add_location_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | [**Location**](Location.md)| location | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **change_location_using_put**
> str change_location_using_put(location)

Modify settings for a connected GraphDB location

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.LocationManagementControllerApi()
location = graphdb.graphdb_workbench.UpdatedLocation() # UpdatedLocation | location

try:
    # Modify settings for a connected GraphDB location
    api_response = api_instance.change_location_using_put(location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationManagementControllerApi->change_location_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | [**UpdatedLocation**](UpdatedLocation.md)| location | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **delete_location_using_delete**
> str delete_location_using_delete(uri=uri)

Disconnect a GraphDB location

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.LocationManagementControllerApi()
uri = 'uri_example' # str | The GraphDB location URL (optional)

try:
    # Disconnect a GraphDB location
    api_response = api_instance.delete_location_using_delete(uri=uri)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationManagementControllerApi->delete_location_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| The GraphDB location URL | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **get_active_location_using_get**
> Location get_active_location_using_get()

Get active connected GraphDB location

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.LocationManagementControllerApi()

try:
    # Get active connected GraphDB location
    api_response = api_instance.get_active_location_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationManagementControllerApi->get_active_location_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Location**](Location.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **get_all_using_get**
> list[Location] get_all_using_get()

Get all connected GraphDB locations

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.LocationManagementControllerApi()

try:
    # Get all connected GraphDB locations
    api_response = api_instance.get_all_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationManagementControllerApi->get_all_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Location]**](Location.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **set_default_repository_using_post**
> str set_default_repository_using_post(default_repository_location)

Set default repository for active GraphDB location

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.LocationManagementControllerApi()
default_repository_location = graphdb.graphdb_workbench.DefaultRepositoryLocation() # DefaultRepositoryLocation | defaultRepositoryLocation

try:
    # Set default repository for active GraphDB location
    api_response = api_instance.set_default_repository_using_post(default_repository_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationManagementControllerApi->set_default_repository_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **default_repository_location** | [**DefaultRepositoryLocation**](DefaultRepositoryLocation.md)| defaultRepositoryLocation | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

