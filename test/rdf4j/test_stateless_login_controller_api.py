# coding: utf-8

"""
    GraphDB Workbench API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import graphdb.graphdb_workbench
from graphdb.graphdb_workbench.api.stateless_login_controller_api import StatelessLoginControllerApi  # noqa: E501
from graphdb.graphdb_workbench.rest import ApiException


class TestStatelessLoginControllerApi(unittest.TestCase):
    """StatelessLoginControllerApi unit test stubs"""

    def setUp(self):
        self.api = graphdb.graphdb_workbench.api.stateless_login_controller_api.StatelessLoginControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_login_using_post(self):
        """Test case for login_using_post

        Authenticate user with a password  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
