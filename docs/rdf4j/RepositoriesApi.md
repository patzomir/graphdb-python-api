# graphdb.rdf4j.RepositoriesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_repository**](RepositoriesApi.md#delete_repository) | **DELETE** /repositories/{repositoryID} | Repository removal
[**delete_statements**](RepositoriesApi.md#delete_statements) | **DELETE** /repositories/{repositoryID}/statements | Deletes statements from the repository.
[**get_all_repositories**](RepositoriesApi.md#get_all_repositories) | **GET** /repositories | An overview of the repositories that are available on a server.
[**get_all_statements**](RepositoriesApi.md#get_all_statements) | **GET** /repositories/{repositoryID}/statements | Fetches statements from the repository.
[**get_repository_size**](RepositoriesApi.md#get_repository_size) | **GET** /repositories/{repositoryID}/size | The repository size (defined as the number of statements it contains)
[**put_statements**](RepositoriesApi.md#put_statements) | **PUT** /repositories/{repositoryID}/statements | Updates data in the repository, replacing any existing data with the supplied data


# **delete_repository**
> delete_repository(repository_id)

Repository removal

Delete a specific repository by ID. Care should be taken with the use of this method: the result of this operation is the complete removal of the repository from the server, including its configuration settings and (if present) data directory

### Example
```python
from __future__ import print_function
import time
import graphdb.rdf4j
from graphdb.rdf4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.rdf4j.RepositoriesApi()
repository_id = 'repository_id_example' # str | The repository ID

try:
    # Repository removal
    api_instance.delete_repository(repository_id)
except ApiException as e:
    print("Exception when calling RepositoriesApi->delete_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The repository ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **delete_statements**
> int delete_statements(repository_id, subj=subj, pred=pred, obj=obj, context=context)

Deletes statements from the repository.

Deletes statements from the repository matching the filtering parameters

### Example
```python
from __future__ import print_function
import time
import graphdb.rdf4j
from graphdb.rdf4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.rdf4j.RepositoriesApi()
repository_id = 'repository_id_example' # str | The repository ID
subj = 'subj_example' # str | Restricts the operation to statements with the specified N-Triples encoded resource as subject. (optional)
pred = 'pred_example' # str | Restricts the operation to statements with the specified N-Triples encoded URI as predicate. (optional)
obj = 'obj_example' # str | Restricts the operation to statements with the specified N-Triples encoded value as object. (optional)
context = 'context_example' # str | If specified, restricts the operation to one or more specific contexts in the repository. The value of this parameter is either an N-Triples encoded URI or bnode ID, or the special value 'null' which represents all context-less statements. If multiple 'context' parameters are specified, the request will operate on the union of all specified contexts. The operation is executed on all statements that are in the repository if no context is specified. (optional)

try:
    # Deletes statements from the repository.
    api_response = api_instance.delete_statements(repository_id, subj=subj, pred=pred, obj=obj, context=context)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->delete_statements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The repository ID | 
 **subj** | **str**| Restricts the operation to statements with the specified N-Triples encoded resource as subject. | [optional] 
 **pred** | **str**| Restricts the operation to statements with the specified N-Triples encoded URI as predicate. | [optional] 
 **obj** | **str**| Restricts the operation to statements with the specified N-Triples encoded value as object. | [optional] 
 **context** | **str**| If specified, restricts the operation to one or more specific contexts in the repository. The value of this parameter is either an N-Triples encoded URI or bnode ID, or the special value &#39;null&#39; which represents all context-less statements. If multiple &#39;context&#39; parameters are specified, the request will operate on the union of all specified contexts. The operation is executed on all statements that are in the repository if no context is specified. | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **get_all_repositories**
> int get_all_repositories()

An overview of the repositories that are available on a server.

Get an list of available repositories, including ID, title, read- and write access parameters for each listed repository. The list is formatted as a tuple query result with variables 'uri', 'id', 'title', 'readable' and 'writable'. The 'uri' value gives the URI/URL for the repository and the 'readable' and 'writable' values are xsd:boolean typed literals indicating read- and write permissions.

### Example
```python
from __future__ import print_function
import time
import graphdb.rdf4j
from graphdb.rdf4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.rdf4j.RepositoriesApi()

try:
    # An overview of the repositories that are available on a server.
    api_response = api_instance.get_all_repositories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_all_repositories: %s\n" % e)
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

# **get_all_statements**
> int get_all_statements(repository_id, subj=subj, pred=pred, obj=obj, context=context, infer=infer)

Fetches statements from the repository.

Get statements from the repository matching the filtering parameters

### Example
```python
from __future__ import print_function
import time
import graphdb.rdf4j
from graphdb.rdf4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.rdf4j.RepositoriesApi()
repository_id = 'repository_id_example' # str | The repository ID
subj = 'subj_example' # str | Restricts the operation to statements with the specified N-Triples encoded resource as subject. (optional)
pred = 'pred_example' # str | Restricts the operation to statements with the specified N-Triples encoded URI as predicate. (optional)
obj = 'obj_example' # str | Restricts the operation to statements with the specified N-Triples encoded value as object. (optional)
context = 'context_example' # str | If specified, restricts the operation to one or more specific contexts in the repository. The value of this parameter is either an N-Triples encoded URI or bnode ID, or the special value 'null' which represents all context-less statements. If multiple 'context' parameters are specified, the request will operate on the union of all specified contexts. The operation is executed on all statements that are in the repository if no context is specified. (optional)
infer = 'infer_example' # str | Specifies whether inferred statements should be included in the result of GET requests. Inferred statements are included by default. Specifying any value other than 'true' (ignoring case) restricts the request to explicit statements only. (optional)

try:
    # Fetches statements from the repository.
    api_response = api_instance.get_all_statements(repository_id, subj=subj, pred=pred, obj=obj, context=context, infer=infer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_all_statements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The repository ID | 
 **subj** | **str**| Restricts the operation to statements with the specified N-Triples encoded resource as subject. | [optional] 
 **pred** | **str**| Restricts the operation to statements with the specified N-Triples encoded URI as predicate. | [optional] 
 **obj** | **str**| Restricts the operation to statements with the specified N-Triples encoded value as object. | [optional] 
 **context** | **str**| If specified, restricts the operation to one or more specific contexts in the repository. The value of this parameter is either an N-Triples encoded URI or bnode ID, or the special value &#39;null&#39; which represents all context-less statements. If multiple &#39;context&#39; parameters are specified, the request will operate on the union of all specified contexts. The operation is executed on all statements that are in the repository if no context is specified. | [optional] 
 **infer** | **str**| Specifies whether inferred statements should be included in the result of GET requests. Inferred statements are included by default. Specifying any value other than &#39;true&#39; (ignoring case) restricts the request to explicit statements only. | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/rdf+xml, text/plain, text/turtle, text/rdf+n3, text/x-nquads, application/rdf+json, application/trix, application/x-trig, application/x-binary-rdf

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **get_repository_size**
> int get_repository_size(repository_id, context=context)

The repository size (defined as the number of statements it contains)

The endpoint will give you the number of statements in the repository or in the given context

### Example
```python
from __future__ import print_function
import time
import graphdb.rdf4j
from graphdb.rdf4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.rdf4j.RepositoriesApi()
repository_id = 'repository_id_example' # str | The repository ID
context = 'context_example' # str | If specified, restricts the operation to one or more specific contexts in the repository. The value of this parameter is either an N-Triples encoded URI or bnode ID, or the special value 'null' which represents all context-less statements. If multiple 'context' parameters are specified, the request will operate on the union of all specified contexts. The operation is executed on all statements that are in the repository if no context is specified. (optional)

try:
    # The repository size (defined as the number of statements it contains)
    api_response = api_instance.get_repository_size(repository_id, context=context)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_repository_size: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The repository ID | 
 **context** | **str**| If specified, restricts the operation to one or more specific contexts in the repository. The value of this parameter is either an N-Triples encoded URI or bnode ID, or the special value &#39;null&#39; which represents all context-less statements. If multiple &#39;context&#39; parameters are specified, the request will operate on the union of all specified contexts. The operation is executed on all statements that are in the repository if no context is specified. | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **put_statements**
> put_statements(repository_id, context=context, base_uri=base_uri, rdf_data=rdf_data)

Updates data in the repository, replacing any existing data with the supplied data

### Example
```python
from __future__ import print_function
import time
import graphdb.rdf4j
from graphdb.rdf4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.rdf4j.RepositoriesApi()
repository_id = 'repository_id_example' # str | The repository ID
context = 'context_example' # str | If specified, restricts the operation to one or more specific contexts in the repository. The value of this parameter is either an N-Triples encoded URI or bnode ID, or the special value 'null' which represents all context-less statements. If multiple 'context' parameters are specified, the request will operate on the union of all specified contexts. The operation is executed on all statements that are in the repository if no context is specified. (optional)
base_uri = 'base_uri_example' # str | Specifies the base URI to resolve any relative URIs found in uploaded data against (optional)
rdf_data = 'rdf_data_example' # str | The supplied data (optional)

try:
    # Updates data in the repository, replacing any existing data with the supplied data
    api_instance.put_statements(repository_id, context=context, base_uri=base_uri, rdf_data=rdf_data)
except ApiException as e:
    print("Exception when calling RepositoriesApi->put_statements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The repository ID | 
 **context** | **str**| If specified, restricts the operation to one or more specific contexts in the repository. The value of this parameter is either an N-Triples encoded URI or bnode ID, or the special value &#39;null&#39; which represents all context-less statements. If multiple &#39;context&#39; parameters are specified, the request will operate on the union of all specified contexts. The operation is executed on all statements that are in the repository if no context is specified. | [optional] 
 **base_uri** | **str**| Specifies the base URI to resolve any relative URIs found in uploaded data against | [optional] 
 **rdf_data** | **str**| The supplied data | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/rdf+xml, text/plain, text/turtle, text/rdf+n3, text/x-nquads, application/rdf+json, application/trix, application/x-trig, application/x-binary-rdf
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

