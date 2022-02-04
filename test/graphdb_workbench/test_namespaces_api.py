# coding: utf-8

"""
    RDF4J API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

from graphdb import rdf4j
from graphdb.rdf4j.api.namespaces_api import NamespacesApi  # noqa: E501
from graphdb.rdf4j.rest import ApiException


class TestNamespacesApi(unittest.TestCase):
    """NamespacesApi unit test stubs"""

    def setUp(self):
        self.api = rdf4j.api.namespaces_api.NamespacesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_namespace_for_prefix(self):
        """Test case for delete_namespace_for_prefix

        Remove namespace for a particular prefix  # noqa: E501
        """
        pass

    def test_get_namespace_for_prefix(self):
        """Test case for get_namespace_for_prefix

        Get namespace for a particular prefix  # noqa: E501
        """
        pass

    def test_set_namespace_for_prefix(self):
        """Test case for set_namespace_for_prefix

        Set namespace for a particular prefix  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
