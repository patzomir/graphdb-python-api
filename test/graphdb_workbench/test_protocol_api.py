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
from graphdb.rdf4j.api.protocol_api import ProtocolApi  # noqa: E501
from graphdb.rdf4j.rest import ApiException


class TestProtocolApi(unittest.TestCase):
    """ProtocolApi unit test stubs"""

    def setUp(self):
        self.api = rdf4j.api.protocol_api.ProtocolApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_protocol_version(self):
        """Test case for get_protocol_version

        Fetch the protocol version  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
