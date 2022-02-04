# graphdb.graphdb_workbench.SqlViewsControllerApi

All URIs are relative to *https://localhost:7200*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sql_view_using_post**](SqlViewsControllerApi.md#create_sql_view_using_post) | **POST** /rest/sql-views/tables | Create a new SQL view
[**delete_sql_view_using_delete**](SqlViewsControllerApi.md#delete_sql_view_using_delete) | **DELETE** /rest/sql-views/tables/{name} | Delete an existing saved query
[**get_sql_view_names_using_get**](SqlViewsControllerApi.md#get_sql_view_names_using_get) | **GET** /rest/sql-views/tables | Get all SQL view names for current repository.
[**get_sql_view_using_get**](SqlViewsControllerApi.md#get_sql_view_using_get) | **GET** /rest/sql-views/tables/{name} | Get a SQL view configuration.
[**update_sql_view_using_put**](SqlViewsControllerApi.md#update_sql_view_using_put) | **PUT** /rest/sql-views/tables/{name} | Edit an existing SQL view


# **create_sql_view_using_post**
> object create_sql_view_using_post(x_graph_db_repository, sql_view)

Create a new SQL view

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.SqlViewsControllerApi()
x_graph_db_repository = 'x_graph_db_repository_example' # str | The repository for which you want to use the JDBC driver
sql_view = graphdb.graphdb_workbench.SqlView() # SqlView | sqlView

try:
    # Create a new SQL view
    api_response = api_instance.create_sql_view_using_post(x_graph_db_repository, sql_view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SqlViewsControllerApi->create_sql_view_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_graph_db_repository** | **str**| The repository for which you want to use the JDBC driver | 
 **sql_view** | [**SqlView**](SqlView.md)| sqlView | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **delete_sql_view_using_delete**
> object delete_sql_view_using_delete(x_graph_db_repository, name)

Delete an existing saved query

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.SqlViewsControllerApi()
x_graph_db_repository = 'x_graph_db_repository_example' # str | The repository for which you want to use the JDBC driver
name = 'name_example' # str | The name of the SQL view

try:
    # Delete an existing saved query
    api_response = api_instance.delete_sql_view_using_delete(x_graph_db_repository, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SqlViewsControllerApi->delete_sql_view_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_graph_db_repository** | **str**| The repository for which you want to use the JDBC driver | 
 **name** | **str**| The name of the SQL view | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **get_sql_view_names_using_get**
> object get_sql_view_names_using_get(x_graph_db_repository)

Get all SQL view names for current repository.

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.SqlViewsControllerApi()
x_graph_db_repository = 'x_graph_db_repository_example' # str | The repository for which you want to use the JDBC driver

try:
    # Get all SQL view names for current repository.
    api_response = api_instance.get_sql_view_names_using_get(x_graph_db_repository)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SqlViewsControllerApi->get_sql_view_names_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_graph_db_repository** | **str**| The repository for which you want to use the JDBC driver | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **get_sql_view_using_get**
> object get_sql_view_using_get(x_graph_db_repository, name)

Get a SQL view configuration.

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.SqlViewsControllerApi()
x_graph_db_repository = 'x_graph_db_repository_example' # str | The repository for which you want to use the JDBC driver
name = 'name_example' # str | The name of the SQL view

try:
    # Get a SQL view configuration.
    api_response = api_instance.get_sql_view_using_get(x_graph_db_repository, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SqlViewsControllerApi->get_sql_view_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_graph_db_repository** | **str**| The repository for which you want to use the JDBC driver | 
 **name** | **str**| The name of the SQL view | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **update_sql_view_using_put**
> str update_sql_view_using_put(x_graph_db_repository, name, sql_view)

Edit an existing SQL view

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.SqlViewsControllerApi()
x_graph_db_repository = 'x_graph_db_repository_example' # str | The repository for which you want to use the JDBC driver
name = 'name_example' # str | The name of the SQL view
sql_view = graphdb.graphdb_workbench.SqlView() # SqlView | sqlView

try:
    # Edit an existing SQL view
    api_response = api_instance.update_sql_view_using_put(x_graph_db_repository, name, sql_view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SqlViewsControllerApi->update_sql_view_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_graph_db_repository** | **str**| The repository for which you want to use the JDBC driver | 
 **name** | **str**| The name of the SQL view | 
 **sql_view** | [**SqlView**](SqlView.md)| sqlView | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

