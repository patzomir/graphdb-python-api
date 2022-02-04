# graphdb.graphdb_workbench.ImportControllerApi

All URIs are relative to *https://localhost:7200*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_server_file_using_post**](ImportControllerApi.md#import_server_file_using_post) | **POST** /rest/data/import/server/{repositoryID} | Import a server file into the repository
[**import_url_upload_using_post**](ImportControllerApi.md#import_url_upload_using_post) | **POST** /rest/data/import/upload/{repositoryID}/url | Import from data URL into the repository
[**interrupt_server_import_using_delete**](ImportControllerApi.md#interrupt_server_import_using_delete) | **DELETE** /rest/data/import/server/{repositoryID} | Cancel server file import operation
[**list_server_files_using_get**](ImportControllerApi.md#list_server_files_using_get) | **GET** /rest/data/import/server/{repositoryID} | Get server files available for import


# **import_server_file_using_post**
> str import_server_file_using_post(import_body, repository_id)

Import a server file into the repository

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.ImportControllerApi()
import_body = graphdb.graphdb_workbench.ServerImportBody() # ServerImportBody | importBody
repository_id = 'repository_id_example' # str | repositoryID

try:
    # Import a server file into the repository
    api_response = api_instance.import_server_file_using_post(import_body, repository_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportControllerApi->import_server_file_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_body** | [**ServerImportBody**](ServerImportBody.md)| importBody | 
 **repository_id** | **str**| repositoryID | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **import_url_upload_using_post**
> str import_url_upload_using_post(import_settings, repository_id)

Import from data URL into the repository

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.ImportControllerApi()
import_settings = graphdb.graphdb_workbench.ImportSettings() # ImportSettings | importSettings
repository_id = 'repository_id_example' # str | repositoryID

try:
    # Import from data URL into the repository
    api_response = api_instance.import_url_upload_using_post(import_settings, repository_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportControllerApi->import_url_upload_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_settings** | [**ImportSettings**](ImportSettings.md)| importSettings | 
 **repository_id** | **str**| repositoryID | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **interrupt_server_import_using_delete**
> str interrupt_server_import_using_delete(repository_id, name=name)

Cancel server file import operation

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.ImportControllerApi()
repository_id = 'repository_id_example' # str | repositoryID
name = 'name_example' # str | The filename import to interrupt. (optional)

try:
    # Cancel server file import operation
    api_response = api_instance.interrupt_server_import_using_delete(repository_id, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportControllerApi->interrupt_server_import_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| repositoryID | 
 **name** | **str**| The filename import to interrupt. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **list_server_files_using_get**
> list[ImportSettings] list_server_files_using_get(repository_id)

Get server files available for import

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.ImportControllerApi()
repository_id = 'repository_id_example' # str | repositoryID

try:
    # Get server files available for import
    api_response = api_instance.list_server_files_using_get(repository_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportControllerApi->list_server_files_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| repositoryID | 

### Return type

[**list[ImportSettings]**](ImportSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

