# graphdb.graphdb_workbench.SparqlTemplateControllerApi

All URIs are relative to *https://localhost:7200*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sparql_template_using_post**](SparqlTemplateControllerApi.md#create_sparql_template_using_post) | **POST** /rest/sparql-template/create | Create a new SPARQL template
[**delete_sparql_template_using_delete**](SparqlTemplateControllerApi.md#delete_sparql_template_using_delete) | **DELETE** /rest/sparql-template/delete | Delete an existing SPARQL template
[**get_sparql_template_content_using_get**](SparqlTemplateControllerApi.md#get_sparql_template_content_using_get) | **GET** /rest/sparql-template/configuration | Get a SPARQL template configuration
[**get_sparql_template_i_ds_using_get**](SparqlTemplateControllerApi.md#get_sparql_template_i_ds_using_get) | **GET** /rest/sparql-template | Get IDs of all configured SPARQL templates per current active repository
[**update_sparql_template_using_put**](SparqlTemplateControllerApi.md#update_sparql_template_using_put) | **PUT** /rest/sparql-template/edit | Edit an existing SPARQL template


# **create_sparql_template_using_post**
> object create_sparql_template_using_post(sparql_template)

Create a new SPARQL template

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.SparqlTemplateControllerApi()
sparql_template = graphdb.graphdb_workbench.SparqlTemplate() # SparqlTemplate | sparqlTemplate

try:
    # Create a new SPARQL template
    api_response = api_instance.create_sparql_template_using_post(sparql_template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SparqlTemplateControllerApi->create_sparql_template_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sparql_template** | [**SparqlTemplate**](SparqlTemplate.md)| sparqlTemplate | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **delete_sparql_template_using_delete**
> object delete_sparql_template_using_delete(template_id=template_id)

Delete an existing SPARQL template

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.SparqlTemplateControllerApi()
template_id = 'template_id_example' # str | The ID of the SPARQL template (optional)

try:
    # Delete an existing SPARQL template
    api_response = api_instance.delete_sparql_template_using_delete(template_id=template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SparqlTemplateControllerApi->delete_sparql_template_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The ID of the SPARQL template | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **get_sparql_template_content_using_get**
> object get_sparql_template_content_using_get(template_id=template_id)

Get a SPARQL template configuration

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.SparqlTemplateControllerApi()
template_id = 'template_id_example' # str | The ID of the SPARQL template (optional)

try:
    # Get a SPARQL template configuration
    api_response = api_instance.get_sparql_template_content_using_get(template_id=template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SparqlTemplateControllerApi->get_sparql_template_content_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The ID of the SPARQL template | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **get_sparql_template_i_ds_using_get**
> object get_sparql_template_i_ds_using_get()

Get IDs of all configured SPARQL templates per current active repository

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.SparqlTemplateControllerApi()

try:
    # Get IDs of all configured SPARQL templates per current active repository
    api_response = api_instance.get_sparql_template_i_ds_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SparqlTemplateControllerApi->get_sparql_template_i_ds_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **update_sparql_template_using_put**
> str update_sparql_template_using_put(content=content, template_id=template_id)

Edit an existing SPARQL template

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.SparqlTemplateControllerApi()
content = 'content_example' # str | The SPARQL template content (optional)
template_id = 'template_id_example' # str | The ID of the SPARQL template (optional)

try:
    # Edit an existing SPARQL template
    api_response = api_instance.update_sparql_template_using_put(content=content, template_id=template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SparqlTemplateControllerApi->update_sparql_template_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content** | **str**| The SPARQL template content | [optional] 
 **template_id** | **str**| The ID of the SPARQL template | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

