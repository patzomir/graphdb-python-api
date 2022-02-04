# graphdb.rdf4j.TransactionsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_transaction_action**](TransactionsApi.md#execute_transaction_action) | **PUT** /repositories/{repositoryID}/transactions/{transactionID} | Execute a transaction action
[**rollback_transaction**](TransactionsApi.md#rollback_transaction) | **DELETE** /repositories/{repositoryID}/transactions/{transactionID} | Abort a transaction
[**start_new_transaction**](TransactionsApi.md#start_new_transaction) | **POST** /repositories/{repositoryID}/transactions | Start a new transaction


# **execute_transaction_action**
> int execute_transaction_action(repository_id, transaction_id, action, subj=subj, pred=pred, obj=obj, context=context, query_ln=query_ln, infer=infer, update=update, base_uri=base_uri, using_graph_uri=using_graph_uri, using_named_graph_uri=using_named_graph_uri, remove_graph_uri=remove_graph_uri, insert_graph_uri=insert_graph_uri, rdf_dataquery=rdf_dataquery)

Execute a transaction action

Execute a transaction action.

### Example
```python
from __future__ import print_function
import time
import graphdb.rdf4j
from graphdb.rdf4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.rdf4j.TransactionsApi()
repository_id = 'repository_id_example' # str | The repository ID
transaction_id = 'transaction_id_example' # str | The transaction ID
action = 'action_example' # str | Type of possible actions in a transaction
subj = 'subj_example' # str | Restricts the operation to statements with the specified N-Triples encoded resource as subject. (optional)
pred = 'pred_example' # str | Restricts the operation to statements with the specified N-Triples encoded resource as predicate. (optional)
obj = 'obj_example' # str | Restricts the operation to statements with the specified N-Triples encoded resource as object. (optional)
context = 'context_example' # str | Restricts the operation to statements with the specified N-Triples encoded resource as context. (optional)
query_ln = 'query_ln_example' # str | Specifies the query language that is used for the query. Acceptable values are strings denoting the query languages supported by the server, i.e. 'serql' for SeRQL queries and 'sparql' for SPARQL queries. If not specified, the server assumes the query is a SPARQL query. (optional)
infer = true # bool | Specifies whether inferred statements should be included in the query evaluation. Inferred statements are included by default. Specifying any value other than 'true' (ignoring case) restricts the query evluation to explicit statements only. (optional)
update = 'update_example' # str | Specifies the Update operation to be executed. The value is expected to be a syntactically valid SPARQL 1.1 Update string. (optional)
base_uri = 'base_uri_example' # str | Specifies a base IRI to be used when parsing the SPARQL update operation. (optional)
using_graph_uri = 'using_graph_uri_example' # str | One or more named graph IRIs to be used as the default graph(s) for retrieving statements. (optional)
using_named_graph_uri = 'using_named_graph_uri_example' # str | One or more named graph IRIs to be used as named graphs for retrieving statements. (optional)
remove_graph_uri = 'remove_graph_uri_example' # str | One or more named graph IRIs to be used as the default graph(s) for removing statements. (optional)
insert_graph_uri = 'insert_graph_uri_example' # str | One or more named graph IRIs to be used as the default graph(s) for inserting statements. (optional)
rdf_dataquery = 'rdf_dataquery_example' # str | A parsable RDF document or a query to evaluate; rdf-data is used for the ADD and DELETE actions, query - for the QUERY action. (optional)

try:
    # Execute a transaction action
    api_response = api_instance.execute_transaction_action(repository_id, transaction_id, action, subj=subj, pred=pred, obj=obj, context=context, query_ln=query_ln, infer=infer, update=update, base_uri=base_uri, using_graph_uri=using_graph_uri, using_named_graph_uri=using_named_graph_uri, remove_graph_uri=remove_graph_uri, insert_graph_uri=insert_graph_uri, rdf_dataquery=rdf_dataquery)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->execute_transaction_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The repository ID | 
 **transaction_id** | **str**| The transaction ID | 
 **action** | **str**| Type of possible actions in a transaction | 
 **subj** | **str**| Restricts the operation to statements with the specified N-Triples encoded resource as subject. | [optional] 
 **pred** | **str**| Restricts the operation to statements with the specified N-Triples encoded resource as predicate. | [optional] 
 **obj** | **str**| Restricts the operation to statements with the specified N-Triples encoded resource as object. | [optional] 
 **context** | **str**| Restricts the operation to statements with the specified N-Triples encoded resource as context. | [optional] 
 **query_ln** | **str**| Specifies the query language that is used for the query. Acceptable values are strings denoting the query languages supported by the server, i.e. &#39;serql&#39; for SeRQL queries and &#39;sparql&#39; for SPARQL queries. If not specified, the server assumes the query is a SPARQL query. | [optional] 
 **infer** | **bool**| Specifies whether inferred statements should be included in the query evaluation. Inferred statements are included by default. Specifying any value other than &#39;true&#39; (ignoring case) restricts the query evluation to explicit statements only. | [optional] 
 **update** | **str**| Specifies the Update operation to be executed. The value is expected to be a syntactically valid SPARQL 1.1 Update string. | [optional] 
 **base_uri** | **str**| Specifies a base IRI to be used when parsing the SPARQL update operation. | [optional] 
 **using_graph_uri** | **str**| One or more named graph IRIs to be used as the default graph(s) for retrieving statements. | [optional] 
 **using_named_graph_uri** | **str**| One or more named graph IRIs to be used as named graphs for retrieving statements. | [optional] 
 **remove_graph_uri** | **str**| One or more named graph IRIs to be used as the default graph(s) for removing statements. | [optional] 
 **insert_graph_uri** | **str**| One or more named graph IRIs to be used as the default graph(s) for inserting statements. | [optional] 
 **rdf_dataquery** | **str**| A parsable RDF document or a query to evaluate; rdf-data is used for the ADD and DELETE actions, query - for the QUERY action. | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/rdf+xml, text/plain, text/turtle, text/rdf+n3, text/x-nquads, application/ld+json, application/rdf+json, application/trix, application/x-trig, application/x-binary-rdf, application/sparql-query
 - **Accept**: application/rdf+xml, application/sparql-results+json, application/sparql-results+xml, application/x-binary-rdf-results-table

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **rollback_transaction**
> int rollback_transaction(repository_id, transaction_id)

Abort a transaction

An active transaction can be aborted by means of a HTTP DELETE request on the transaction resource. This will execute a transaction rollback on the repository and will close the transacion. After executing a DELETE, further operations on the same transaction will result in an error.

### Example
```python
from __future__ import print_function
import time
import graphdb.rdf4j
from graphdb.rdf4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.rdf4j.TransactionsApi()
repository_id = 'repository_id_example' # str | The repository ID
transaction_id = 'transaction_id_example' # str | The transaction ID

try:
    # Abort a transaction
    api_response = api_instance.rollback_transaction(repository_id, transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->rollback_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The repository ID | 
 **transaction_id** | **str**| The transaction ID | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **start_new_transaction**
> int start_new_transaction(repository_id)

Start a new transaction

Start a new transaction.

### Example
```python
from __future__ import print_function
import time
import graphdb.rdf4j
from graphdb.rdf4j.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = graphdb.rdf4j.TransactionsApi()
repository_id = 'repository_id_example' # str | The repository ID

try:
    # Start a new transaction
    api_response = api_instance.start_new_transaction(repository_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->start_new_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| The repository ID | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

