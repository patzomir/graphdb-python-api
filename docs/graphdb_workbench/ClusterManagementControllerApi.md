# graphdb.graphdb_workbench.ClusterManagementControllerApi

All URIs are relative to *https://localhost:7200*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clone_worker_using_post**](ClusterManagementControllerApi.md#clone_worker_using_post) | **POST** /rest/cluster/nodes/clone | Clone a worker
[**connect_masters_using_post**](ClusterManagementControllerApi.md#connect_masters_using_post) | **POST** /rest/cluster/masters/{masterRepositoryId}/peers | Connect two masters
[**connect_worker_using_post**](ClusterManagementControllerApi.md#connect_worker_using_post) | **POST** /rest/cluster/masters/{masterRepositoryId}/workers | Connect a worker to a master
[**disconnect_masters_using_delete**](ClusterManagementControllerApi.md#disconnect_masters_using_delete) | **DELETE** /rest/cluster/masters/{masterRepositoryId}/peers | Disconnect two masters
[**disconnect_worker_using_delete**](ClusterManagementControllerApi.md#disconnect_worker_using_delete) | **DELETE** /rest/cluster/masters/{masterRepositoryId}/workers | Disconnect a worker from a master
[**do_backup_using_get**](ClusterManagementControllerApi.md#do_backup_using_get) | **GET** /rest/cluster/masters/{masterRepositoryId}/backup | Initiate a cluster backup
[**do_restore_using_get**](ClusterManagementControllerApi.md#do_restore_using_get) | **GET** /rest/cluster/masters/{masterRepositoryId}/restore | Initiate a cluster restore
[**get_master_using_get**](ClusterManagementControllerApi.md#get_master_using_get) | **GET** /rest/cluster/masters/{masterRepositoryId} | Get information about a master
[**get_workers_for_master_using_get**](ClusterManagementControllerApi.md#get_workers_for_master_using_get) | **GET** /rest/cluster/masters/{masterRepositoryId}/workers | Get workers connected to a master
[**set_master_using_post**](ClusterManagementControllerApi.md#set_master_using_post) | **POST** /rest/cluster/masters/{masterRepositoryId} | Set master attribute


# **clone_worker_using_post**
> str clone_worker_using_post(bean)

Clone a worker

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.ClusterManagementControllerApi()
bean = graphdb.graphdb_workbench.WorkerCloneBean() # WorkerCloneBean | bean

try:
    # Clone a worker
    api_response = api_instance.clone_worker_using_post(bean)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterManagementControllerApi->clone_worker_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bean** | [**WorkerCloneBean**](WorkerCloneBean.md)| bean | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **connect_masters_using_post**
> str connect_masters_using_post(master_repository_id, bean)

Connect two masters

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.ClusterManagementControllerApi()
master_repository_id = 'master_repository_id_example' # str | master repository ID
bean = graphdb.graphdb_workbench.MasterConnectBean() # MasterConnectBean | bean

try:
    # Connect two masters
    api_response = api_instance.connect_masters_using_post(master_repository_id, bean)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterManagementControllerApi->connect_masters_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **master_repository_id** | **str**| master repository ID | 
 **bean** | [**MasterConnectBean**](MasterConnectBean.md)| bean | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **connect_worker_using_post**
> str connect_worker_using_post(master_repository_id, bean)

Connect a worker to a master

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.ClusterManagementControllerApi()
master_repository_id = 'master_repository_id_example' # str | master repository ID
bean = graphdb.graphdb_workbench.WorkerConnectBean() # WorkerConnectBean | bean

try:
    # Connect a worker to a master
    api_response = api_instance.connect_worker_using_post(master_repository_id, bean)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterManagementControllerApi->connect_worker_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **master_repository_id** | **str**| master repository ID | 
 **bean** | [**WorkerConnectBean**](WorkerConnectBean.md)| bean | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **disconnect_masters_using_delete**
> str disconnect_masters_using_delete(master_repository_id, bidirectional=bidirectional, master_location=master_location, master_node_id=master_node_id, peer_location=peer_location, peer_node_id=peer_node_id, peer_repository_id=peer_repository_id)

Disconnect two masters

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.ClusterManagementControllerApi()
master_repository_id = 'master_repository_id_example' # str | master repository ID
bidirectional = true # bool | whether to connect the masters in both directions (default) (optional)
master_location = 'master_location_example' # str | master repository location (optional)
master_node_id = 'master_node_id_example' # str | master node id (optional)
peer_location = 'peer_location_example' # str | the peer repository location (optional)
peer_node_id = 'peer_node_id_example' # str | the peer node ID (optional)
peer_repository_id = 'peer_repository_id_example' # str | the peer repository ID (optional)

try:
    # Disconnect two masters
    api_response = api_instance.disconnect_masters_using_delete(master_repository_id, bidirectional=bidirectional, master_location=master_location, master_node_id=master_node_id, peer_location=peer_location, peer_node_id=peer_node_id, peer_repository_id=peer_repository_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterManagementControllerApi->disconnect_masters_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **master_repository_id** | **str**| master repository ID | 
 **bidirectional** | **bool**| whether to connect the masters in both directions (default) | [optional] 
 **master_location** | **str**| master repository location | [optional] 
 **master_node_id** | **str**| master node id | [optional] 
 **peer_location** | **str**| the peer repository location | [optional] 
 **peer_node_id** | **str**| the peer node ID | [optional] 
 **peer_repository_id** | **str**| the peer repository ID | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **disconnect_worker_using_delete**
> str disconnect_worker_using_delete(master_repository_id, master_location=master_location, worker_url=worker_url)

Disconnect a worker from a master

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.ClusterManagementControllerApi()
master_repository_id = 'master_repository_id_example' # str | master repository ID
master_location = 'master_location_example' # str | worker repository URL (optional)
worker_url = 'worker_url_example' # str | master repository location (optional)

try:
    # Disconnect a worker from a master
    api_response = api_instance.disconnect_worker_using_delete(master_repository_id, master_location=master_location, worker_url=worker_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterManagementControllerApi->disconnect_worker_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **master_repository_id** | **str**| master repository ID | 
 **master_location** | **str**| worker repository URL | [optional] 
 **worker_url** | **str**| master repository location | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **do_backup_using_get**
> str do_backup_using_get(master_repository_id, backup_name, master_location=master_location)

Initiate a cluster backup

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.ClusterManagementControllerApi()
master_repository_id = 'master_repository_id_example' # str | master repository ID
backup_name = 'backup_name_example' # str | backupName
master_location = 'master_location_example' # str | masterLocation (optional)

try:
    # Initiate a cluster backup
    api_response = api_instance.do_backup_using_get(master_repository_id, backup_name, master_location=master_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterManagementControllerApi->do_backup_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **master_repository_id** | **str**| master repository ID | 
 **backup_name** | **str**| backupName | 
 **master_location** | **str**| masterLocation | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **do_restore_using_get**
> str do_restore_using_get(master_repository_id, backup_name, master_location=master_location)

Initiate a cluster restore

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.ClusterManagementControllerApi()
master_repository_id = 'master_repository_id_example' # str | master repository ID
backup_name = 'backup_name_example' # str | backupName
master_location = 'master_location_example' # str | masterLocation (optional)

try:
    # Initiate a cluster restore
    api_response = api_instance.do_restore_using_get(master_repository_id, backup_name, master_location=master_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterManagementControllerApi->do_restore_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **master_repository_id** | **str**| master repository ID | 
 **backup_name** | **str**| backupName | 
 **master_location** | **str**| masterLocation | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **get_master_using_get**
> MasterNode get_master_using_get(master_repository_id, master_location=master_location)

Get information about a master

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.ClusterManagementControllerApi()
master_repository_id = 'master_repository_id_example' # str | master repository ID
master_location = 'master_location_example' # str | master repository location (optional)

try:
    # Get information about a master
    api_response = api_instance.get_master_using_get(master_repository_id, master_location=master_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterManagementControllerApi->get_master_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **master_repository_id** | **str**| master repository ID | 
 **master_location** | **str**| master repository location | [optional] 

### Return type

[**MasterNode**](MasterNode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **get_workers_for_master_using_get**
> list[WorkerNode] get_workers_for_master_using_get(master_repository_id, master_location=master_location)

Get workers connected to a master

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.ClusterManagementControllerApi()
master_repository_id = 'master_repository_id_example' # str | master repository id
master_location = 'master_location_example' # str | master repository location (optional)

try:
    # Get workers connected to a master
    api_response = api_instance.get_workers_for_master_using_get(master_repository_id, master_location=master_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterManagementControllerApi->get_workers_for_master_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **master_repository_id** | **str**| master repository id | 
 **master_location** | **str**| master repository location | [optional] 

### Return type

[**list[WorkerNode]**](WorkerNode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **set_master_using_post**
> str set_master_using_post(master_repository_id, bean, master_location=master_location)

Set master attribute

### Example
```python
from __future__ import print_function
import time
import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.graphdb_workbench.ClusterManagementControllerApi()
master_repository_id = 'master_repository_id_example' # str | master repository ID
bean = NULL # object | bean
master_location = 'master_location_example' # str | master repository location (optional)

try:
    # Set master attribute
    api_response = api_instance.set_master_using_post(master_repository_id, bean, master_location=master_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterManagementControllerApi->set_master_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **master_repository_id** | **str**| master repository ID | 
 **bean** | **object**| bean | 
 **master_location** | **str**| master repository location | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

