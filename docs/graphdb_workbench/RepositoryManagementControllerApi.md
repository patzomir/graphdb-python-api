# graphdb.graphdb_workbench.RepositoryManagementControllerApi

All URIs are relative to *https://localhost:7200*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_repository_using_post**](RepositoryManagementControllerApi.md#create_repository_using_post) | **POST** /rest/repositories | Create a repository in an attached Sesame location (ttl file)
[**delete_repository_using_delete**](RepositoryManagementControllerApi.md#delete_repository_using_delete) | **DELETE** /rest/repositories/{repositoryID} | Delete a repository in an attached Sesame location
[**download_repository_config_turtle_using_get**](RepositoryManagementControllerApi.md#download_repository_config_turtle_using_get) | **GET** /rest/repositories/{repositoryID}/download | Download repository configuration as a Turtle file
[**download_repository_config_zip_using_get**](RepositoryManagementControllerApi.md#download_repository_config_zip_using_get) | **GET** /rest/repositories/{repositoryID}/downloadZip | Download repository configuration as a zip file
[**edit_repository_using_put**](RepositoryManagementControllerApi.md#edit_repository_using_put) | **PUT** /rest/repositories/{repositoryID} | Edit repository configuration
[**get_default_config_using_get**](RepositoryManagementControllerApi.md#get_default_config_using_get) | **GET** /rest/repositories/defaultConfig/{repositoryType} | Get the default repository configuration for the repository type
[**get_repositories_using_get**](RepositoryManagementControllerApi.md#get_repositories_using_get) | **GET** /rest/repositories | Get all repositories in the active location or another location
[**get_repository_config_json_using_get**](RepositoryManagementControllerApi.md#get_repository_config_json_using_get) | **GET** /rest/repositories/{repositoryID} | Get repository configuration as JSON
[**repository_size_using_get**](RepositoryManagementControllerApi.md#repository_size_using_get) | **GET** /rest/repositories/{repositoryID}/size | Get repository size
[**restart_repository_using_post**](RepositoryManagementControllerApi.md#restart_repository_using_post) | **POST** /rest/repositories/{repositoryID}/restart | Restart a repository


# **create_repository_using_post**
> object create_repository_using_post(config=config, location=location, constraint_file=constraint_file, obda_file=obda_file, owl_file=owl_file, properties_file=properties_file)

Create a repository in an attached Sesame location (ttl file)

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.RepositoryManagementControllerApi()
config = '/path/to/file.txt' # file | A ttl configuration file for the repository (optional)
location = 'location_example' # str | Sesame location (optional)
constraint_file = '/path/to/file.txt' # file | constraintFile (optional)
obda_file = '/path/to/file.txt' # file | obdaFile (optional)
owl_file = '/path/to/file.txt' # file | owlFile (optional)
properties_file = '/path/to/file.txt' # file | propertiesFile (optional)

try:
    # Create a repository in an attached Sesame location (ttl file)
    api_response = api_instance.create_repository_using_post(config=config, location=location, constraint_file=constraint_file, obda_file=obda_file, owl_file=owl_file, properties_file=properties_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementControllerApi->create_repository_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config** | **file**| A ttl configuration file for the repository | [optional] 
 **location** | **str**| Sesame location | [optional] 
 **constraint_file** | **file**| constraintFile | [optional] 
 **obda_file** | **file**| obdaFile | [optional] 
 **owl_file** | **file**| owlFile | [optional] 
 **properties_file** | **file**| propertiesFile | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **delete_repository_using_delete**
> object delete_repository_using_delete(repository_id, location=location)

Delete a repository in an attached Sesame location

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.RepositoryManagementControllerApi()
repository_id = 'repository_id_example' # str | repositoryID
location = 'location_example' # str | location (optional)

try:
    # Delete a repository in an attached Sesame location
    api_response = api_instance.delete_repository_using_delete(repository_id, location=location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementControllerApi->delete_repository_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| repositoryID | 
 **location** | **str**| location | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **download_repository_config_turtle_using_get**
> object download_repository_config_turtle_using_get(repository_id, location=location)

Download repository configuration as a Turtle file

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.RepositoryManagementControllerApi()
repository_id = 'repository_id_example' # str | repositoryID
location = 'location_example' # str | location (optional)

try:
    # Download repository configuration as a Turtle file
    api_response = api_instance.download_repository_config_turtle_using_get(repository_id, location=location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementControllerApi->download_repository_config_turtle_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| repositoryID | 
 **location** | **str**| location | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/turtle

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **download_repository_config_zip_using_get**
> download_repository_config_zip_using_get(repository_id, location=location)

Download repository configuration as a zip file

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.RepositoryManagementControllerApi()
repository_id = 'repository_id_example' # str | repositoryID
location = 'location_example' # str | location (optional)

try:
    # Download repository configuration as a zip file
    api_instance.download_repository_config_zip_using_get(repository_id, location=location)
except ApiException as e:
    print("Exception when calling RepositoryManagementControllerApi->download_repository_config_zip_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| repositoryID | 
 **location** | **str**| location | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **edit_repository_using_put**
> object edit_repository_using_put(bean, repository_id)

Edit repository configuration

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.RepositoryManagementControllerApi()
bean = graphdb.graphdb_workbench.RepositoryConfigBean() # RepositoryConfigBean | bean
repository_id = 'repository_id_example' # str | repositoryID

try:
    # Edit repository configuration
    api_response = api_instance.edit_repository_using_put(bean, repository_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementControllerApi->edit_repository_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bean** | [**RepositoryConfigBean**](RepositoryConfigBean.md)| bean | 
 **repository_id** | **str**| repositoryID | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **get_default_config_using_get**
> RepositoryConfigBean get_default_config_using_get(repository_type, repository_id=repository_id, repository_title=repository_title)

Get the default repository configuration for the repository type

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.RepositoryManagementControllerApi()
repository_type = 'repository_type_example' # str | repository type: 'se', 'master', 'worker', 'free' or 'ontop'
repository_id = 'repository_id_example' # str | repositoryID (optional)
repository_title = 'repository_title_example' # str | repositoryTitle (optional)

try:
    # Get the default repository configuration for the repository type
    api_response = api_instance.get_default_config_using_get(repository_type, repository_id=repository_id, repository_title=repository_title)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementControllerApi->get_default_config_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_type** | **str**| repository type: &#39;se&#39;, &#39;master&#39;, &#39;worker&#39;, &#39;free&#39; or &#39;ontop&#39; | 
 **repository_id** | **str**| repositoryID | [optional] 
 **repository_title** | **str**| repositoryTitle | [optional] 

### Return type

[**RepositoryConfigBean**](RepositoryConfigBean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **get_repositories_using_get**
> list[GraphDBRepository] get_repositories_using_get(location=location)

Get all repositories in the active location or another location

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.RepositoryManagementControllerApi()
location = 'location_example' # str | location (optional)

try:
    # Get all repositories in the active location or another location
    api_response = api_instance.get_repositories_using_get(location=location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementControllerApi->get_repositories_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| location | [optional] 

### Return type

[**list[GraphDBRepository]**](GraphDBRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **get_repository_config_json_using_get**
> object get_repository_config_json_using_get(repository_id, location=location)

Get repository configuration as JSON

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.RepositoryManagementControllerApi()
repository_id = 'repository_id_example' # str | repositoryID
location = 'location_example' # str | location (optional)

try:
    # Get repository configuration as JSON
    api_response = api_instance.get_repository_config_json_using_get(repository_id, location=location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementControllerApi->get_repository_config_json_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| repositoryID | 
 **location** | **str**| location | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **repository_size_using_get**
> RepositorySizeInfo repository_size_using_get(repository_id, location=location)

Get repository size

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.RepositoryManagementControllerApi()
repository_id = 'repository_id_example' # str | repositoryID
location = 'location_example' # str | location (optional)

try:
    # Get repository size
    api_response = api_instance.repository_size_using_get(repository_id, location=location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementControllerApi->repository_size_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| repositoryID | 
 **location** | **str**| location | [optional] 

### Return type

[**RepositorySizeInfo**](RepositorySizeInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restart_repository_using_post**
> object restart_repository_using_post(repository_id, sync=sync)

Restart a repository

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.RepositoryManagementControllerApi()
repository_id = 'repository_id_example' # str | repositoryID
sync = true # bool | sync (optional)

try:
    # Restart a repository
    api_response = api_instance.restart_repository_using_post(repository_id, sync=sync)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementControllerApi->restart_repository_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| repositoryID | 
 **sync** | **bool**| sync | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

