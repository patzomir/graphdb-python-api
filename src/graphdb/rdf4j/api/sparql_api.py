# coding: utf-8

"""
    RDF4J API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from graphdb.rdf4j.api_client import ApiClient


class SparqlApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def execute_get_select_query(self, repository_id, query, **kwargs):  # noqa: E501
        """Send queries on a specific repository with ID. This resource represents a SPARQL query endpoint  # noqa: E501

        The main endpoint that is responsible for sending queries to a particular repository  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.execute_get_select_query(repository_id, query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository_id: The repository ID (required)
        :param str query: The query to evaluate (required)
        :param str query_ln: Specifies the query language that is used for the query. Acceptable values are strings denoting the query languages supported by the server, i.e. 'serql' for SeRQL queries and 'sparql' for SPARQL queries. If not specified, the server assumes the query is a SPARQL query
        :param bool infer: Specifies whether inferred statements should be included in the query evaluation. Inferred statements are included by default. Specifying any value other than 'true' (ignoring case) restricts the query evluation to explicit statements only.
        :param str varname: Specifies variable bindings. Variables appearing in the query can be bound to a specific value outside the actual query using this option. The value should be an N-Triples encoded RDF value.
        :param int timeout: Specifies a maximum query execution time, in whole seconds. The value should be an integer. A setting of 0 or a negative number indicates unlimited query time (the default).
        :param bool distinct: Specifies if only distinct query solutions should be returned. The value should be true or false. If the supplied SPARQL query itself already has a DISTINCT modifier, this parameter will have no effect.
        :param int limit: Specifies the maximum number of query solutions to return. The value should be a positive integer. If the supplied SPARQL query itself already has a LIMIT modifier, this parameter will only have an effect if the supplied value is lower than the LIMIT value in the query.
        :param int offset: Specifies the number of query solutions to skip. The value should be a positive integer. This parameter is cumulative with any OFFSET modifier in the supplied SPARQL query itself.
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.execute_get_select_query_with_http_info(repository_id, query, **kwargs)  # noqa: E501
        else:
            (data) = self.execute_get_select_query_with_http_info(repository_id, query, **kwargs)  # noqa: E501
            return data

    def execute_get_select_query_with_http_info(self, repository_id, query, **kwargs):  # noqa: E501
        """Send queries on a specific repository with ID. This resource represents a SPARQL query endpoint  # noqa: E501

        The main endpoint that is responsible for sending queries to a particular repository  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.execute_get_select_query_with_http_info(repository_id, query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository_id: The repository ID (required)
        :param str query: The query to evaluate (required)
        :param str query_ln: Specifies the query language that is used for the query. Acceptable values are strings denoting the query languages supported by the server, i.e. 'serql' for SeRQL queries and 'sparql' for SPARQL queries. If not specified, the server assumes the query is a SPARQL query
        :param bool infer: Specifies whether inferred statements should be included in the query evaluation. Inferred statements are included by default. Specifying any value other than 'true' (ignoring case) restricts the query evluation to explicit statements only.
        :param str varname: Specifies variable bindings. Variables appearing in the query can be bound to a specific value outside the actual query using this option. The value should be an N-Triples encoded RDF value.
        :param int timeout: Specifies a maximum query execution time, in whole seconds. The value should be an integer. A setting of 0 or a negative number indicates unlimited query time (the default).
        :param bool distinct: Specifies if only distinct query solutions should be returned. The value should be true or false. If the supplied SPARQL query itself already has a DISTINCT modifier, this parameter will have no effect.
        :param int limit: Specifies the maximum number of query solutions to return. The value should be a positive integer. If the supplied SPARQL query itself already has a LIMIT modifier, this parameter will only have an effect if the supplied value is lower than the LIMIT value in the query.
        :param int offset: Specifies the number of query solutions to skip. The value should be a positive integer. This parameter is cumulative with any OFFSET modifier in the supplied SPARQL query itself.
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        rdf4j = ['repository_id', 'query', 'query_ln', 'infer', 'varname', 'timeout', 'distinct', 'limit', 'offset']  # noqa: E501
        rdf4j.append('async_req')
        rdf4j.append('_return_http_data_only')
        rdf4j.append('_preload_content')
        rdf4j.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in rdf4j:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method execute_get_select_query" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository_id' is set
        if self.api_client.client_side_validation and ('repository_id' not in params or
                                                       params['repository_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `repository_id` when calling `execute_get_select_query`")  # noqa: E501
        # verify the required parameter 'query' is set
        if self.api_client.client_side_validation and ('query' not in params or
                                                       params['query'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `query` when calling `execute_get_select_query`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository_id' in params:
            path_params['repositoryID'] = params['repository_id']  # noqa: E501

        query_params = []
        # if 'query' in params:
        #     query_params.append(('query', params['query']))  # noqa: E501
        if 'query_ln' in params:
            query_params.append(('queryLn', params['query_ln']))  # noqa: E501
        if 'infer' in params:
            query_params.append(('infer', params['infer']))  # noqa: E501
        if 'varname' in params:
            query_params.append(('$&lt;varname&gt;', params['varname']))  # noqa: E501
        if 'timeout' in params:
            query_params.append(('timeout', params['timeout']))  # noqa: E501
        if 'distinct' in params:
            query_params.append(('distinct', params['distinct']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        if 'query' in params:
            form_params.append(('query', params['query']))  # noqa: E501
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/sparql-results+xml', 'application/sparql-results+json', 'application/x-binary-rdf-results-table'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/repositories/{repositoryID}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update(self, repository_id, **kwargs):  # noqa: E501
        """Performs updates on the data in the repository  # noqa: E501

        The data supplied with this request is expected to contain either an RDF document, a SPARQL 1.1 Update string, or a special purpose transaction document. If an RDF document is supplied, the statements found in the RDF document will be added to the repository. If a SPARQL 1.1 Update string is supplied, the update operation will be parsed and executed. If a transaction document is supplied, the updates specified in the transaction document will be executed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update(repository_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository_id: The repository ID (required)
        :param str update: Only relevant for POST operations. Specifies the SPARQL 1.1 Update string to be executed. The value is expected to be a syntactically valid SPARQL 1.1 Update string.
        :param str base_uri: Specifies the base URI to resolve any relative URIs found in uploaded data against. This parameter only applies to the PUT and POST method.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_with_http_info(repository_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_with_http_info(repository_id, **kwargs)  # noqa: E501
            return data

    def update_with_http_info(self, repository_id, **kwargs):  # noqa: E501
        """Performs updates on the data in the repository  # noqa: E501

        The data supplied with this request is expected to contain either an RDF document, a SPARQL 1.1 Update string, or a special purpose transaction document. If an RDF document is supplied, the statements found in the RDF document will be added to the repository. If a SPARQL 1.1 Update string is supplied, the update operation will be parsed and executed. If a transaction document is supplied, the updates specified in the transaction document will be executed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_with_http_info(repository_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository_id: The repository ID (required)
        :param str update: Only relevant for POST operations. Specifies the SPARQL 1.1 Update string to be executed. The value is expected to be a syntactically valid SPARQL 1.1 Update string.
        :param str base_uri: Specifies the base URI to resolve any relative URIs found in uploaded data against. This parameter only applies to the PUT and POST method.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        rdf4j = ['repository_id', 'update', 'base_uri']  # noqa: E501
        rdf4j.append('async_req')
        rdf4j.append('_return_http_data_only')
        rdf4j.append('_preload_content')
        rdf4j.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in rdf4j:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository_id' is set
        if self.api_client.client_side_validation and ('repository_id' not in params or
                                                       params['repository_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `repository_id` when calling `update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository_id' in params:
            path_params['repositoryID'] = params['repository_id']  # noqa: E501

        query_params = []
        if 'base_uri' in params:
            query_params.append(('baseURI', params['base_uri']))  # noqa: E501

        header_params = {}

        form_params = []
        if 'update' in params:
            form_params.append(('update', params['update']))  # noqa: E501
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/rdf+xml', 'text/plain', 'text/turtle', 'text/rdf+n3', 'text/x-nquads', 'application/rdf+json', 'application/trix', 'application/x-trig', 'application/x-binary-rdf'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/repositories/{repositoryID}/statements', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
