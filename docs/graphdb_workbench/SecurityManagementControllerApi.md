# graphdb.graphdb_workbench.SecurityManagementControllerApi

All URIs are relative to *https://localhost:7200*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_user_settings_using_patch**](SecurityManagementControllerApi.md#change_user_settings_using_patch) | **PATCH** /rest/security/user/** | Change settings for a user
[**create_user_using_post**](SecurityManagementControllerApi.md#create_user_using_post) | **POST** /rest/security/user/** | Create a user
[**delete_user_using_delete**](SecurityManagementControllerApi.md#delete_user_using_delete) | **DELETE** /rest/security/user/** | Delete a user
[**edit_user_using_put**](SecurityManagementControllerApi.md#edit_user_using_put) | **PUT** /rest/security/user/** | Edit a user
[**get_all_users_using_get**](SecurityManagementControllerApi.md#get_all_users_using_get) | **GET** /rest/security/user | Get all users
[**get_user_using_get**](SecurityManagementControllerApi.md#get_user_using_get) | **GET** /rest/security/user/** | Get a user
[**is_enabled_free_access_using_get**](SecurityManagementControllerApi.md#is_enabled_free_access_using_get) | **GET** /rest/security/freeaccess | Check if free access is enabled
[**is_enabled_security_using_get**](SecurityManagementControllerApi.md#is_enabled_security_using_get) | **GET** /rest/security | Check if security is enabled
[**set_enable_free_access_using_post**](SecurityManagementControllerApi.md#set_enable_free_access_using_post) | **POST** /rest/security/freeaccess | Enable or disable free access
[**set_enable_security_using_post**](SecurityManagementControllerApi.md#set_enable_security_using_post) | **POST** /rest/security | Enable or disable security


# **change_user_settings_using_patch**
> object change_user_settings_using_patch(user, x_graph_db_password=x_graph_db_password)

Change settings for a user

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.SecurityManagementControllerApi()
user = graphdb.graphdb_workbench.Account() # Account | user
x_graph_db_password = 'x_graph_db_password_example' # str | X-GraphDB-Password (optional)

try:
    # Change settings for a user
    api_response = api_instance.change_user_settings_using_patch(user, x_graph_db_password=x_graph_db_password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityManagementControllerApi->change_user_settings_using_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**Account**](Account.md)| user | 
 **x_graph_db_password** | **str**| X-GraphDB-Password | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **create_user_using_post**
> object create_user_using_post(user, x_graph_db_password=x_graph_db_password)

Create a user

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.SecurityManagementControllerApi()
user = graphdb.graphdb_workbench.Account() # Account | user
x_graph_db_password = 'x_graph_db_password_example' # str | X-GraphDB-Password (optional)

try:
    # Create a user
    api_response = api_instance.create_user_using_post(user, x_graph_db_password=x_graph_db_password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityManagementControllerApi->create_user_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**Account**](Account.md)| user | 
 **x_graph_db_password** | **str**| X-GraphDB-Password | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **delete_user_using_delete**
> object delete_user_using_delete()

Delete a user

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.SecurityManagementControllerApi()

try:
    # Delete a user
    api_response = api_instance.delete_user_using_delete()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityManagementControllerApi->delete_user_using_delete: %s\n" % e)
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

# **edit_user_using_put**
> object edit_user_using_put(user, x_graph_db_password=x_graph_db_password)

Edit a user

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.SecurityManagementControllerApi()
user = graphdb.graphdb_workbench.Account() # Account | user
x_graph_db_password = 'x_graph_db_password_example' # str | X-GraphDB-Password (optional)

try:
    # Edit a user
    api_response = api_instance.edit_user_using_put(user, x_graph_db_password=x_graph_db_password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityManagementControllerApi->edit_user_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**Account**](Account.md)| user | 
 **x_graph_db_password** | **str**| X-GraphDB-Password | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **get_all_users_using_get**
> list[Account] get_all_users_using_get()

Get all users

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.SecurityManagementControllerApi()

try:
    # Get all users
    api_response = api_instance.get_all_users_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityManagementControllerApi->get_all_users_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Account]**](Account.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **get_user_using_get**
> object get_user_using_get()

Get a user

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.SecurityManagementControllerApi()

try:
    # Get a user
    api_response = api_instance.get_user_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityManagementControllerApi->get_user_using_get: %s\n" % e)
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

# **is_enabled_free_access_using_get**
> AccessBean is_enabled_free_access_using_get()

Check if free access is enabled

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.SecurityManagementControllerApi()

try:
    # Check if free access is enabled
    api_response = api_instance.is_enabled_free_access_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityManagementControllerApi->is_enabled_free_access_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccessBean**](AccessBean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **is_enabled_security_using_get**
> bool is_enabled_security_using_get()

Check if security is enabled

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.SecurityManagementControllerApi()

try:
    # Check if security is enabled
    api_response = api_instance.is_enabled_security_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityManagementControllerApi->is_enabled_security_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **set_enable_free_access_using_post**
> object set_enable_free_access_using_post(freeaccess)

Enable or disable free access

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.SecurityManagementControllerApi()
freeaccess = graphdb.graphdb_workbench.AccessBean() # AccessBean | freeaccess

try:
    # Enable or disable free access
    api_response = api_instance.set_enable_free_access_using_post(freeaccess)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityManagementControllerApi->set_enable_free_access_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **freeaccess** | [**AccessBean**](AccessBean.md)| freeaccess | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **set_enable_security_using_post**
> object set_enable_security_using_post(use_security)

Enable or disable security

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.SecurityManagementControllerApi()
use_security = true # bool | useSecurity

try:
    # Enable or disable security
    api_response = api_instance.set_enable_security_using_post(use_security)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityManagementControllerApi->set_enable_security_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **use_security** | **bool**| useSecurity | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

