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
from graphdb.graphdb_workbench.api.import_controller_api import ImportControllerApi  # noqa: E501
from graphdb.graphdb_workbench.rest import ApiException


class TestImportControllerApi(unittest.TestCase):
    """ImportControllerApi unit test stubs"""

    def setUp(self):
        self.api = graphdb.graphdb_workbench.api.import_controller_api.ImportControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_import_server_file_using_post(self):
        """Test case for import_server_file_using_post

        Import a server file into the repository  # noqa: E501
        """
        pass

    def test_import_url_upload_using_post(self):
        """Test case for import_url_upload_using_post

        Import from data URL into the repository  # noqa: E501
        """
        pass

    def test_interrupt_server_import_using_delete(self):
        """Test case for interrupt_server_import_using_delete

        Cancel server file import operation  # noqa: E501
        """
        pass

    def test_list_server_files_using_get(self):
        """Test case for list_server_files_using_get

        Get server files available for import  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
