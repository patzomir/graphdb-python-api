# coding: utf-8

"""
    RDF4J API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

from  graphdb import rdf4j
from graphdb.rdf4j.api.contexts_api import ContextsApi  # noqa: E501
from graphdb.rdf4j.rest import ApiException


class TestContextsApi(unittest.TestCase):
    """ContextsApi unit test stubs"""

    def setUp(self):
        self.api = rdf4j.api.contexts_api.ContextsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_repository_contexts(self):
        """Test case for get_repository_contexts

        Gets a list of resources that are used as context identifiers.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()