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
from graphdb.graphdb_workbench.api.cluster_management_controller_api import ClusterManagementControllerApi  # noqa: E501
from graphdb.graphdb_workbench.rest import ApiException


class TestClusterManagementControllerApi(unittest.TestCase):
    """ClusterManagementControllerApi unit test stubs"""

    def setUp(self):
        self.api = graphdb.graphdb_workbench.api.cluster_management_controller_api.ClusterManagementControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_clone_worker_using_post(self):
        """Test case for clone_worker_using_post

        Clone a worker  # noqa: E501
        """
        pass

    def test_connect_masters_using_post(self):
        """Test case for connect_masters_using_post

        Connect two masters  # noqa: E501
        """
        pass

    def test_connect_worker_using_post(self):
        """Test case for connect_worker_using_post

        Connect a worker to a master  # noqa: E501
        """
        pass

    def test_disconnect_masters_using_delete(self):
        """Test case for disconnect_masters_using_delete

        Disconnect two masters  # noqa: E501
        """
        pass

    def test_disconnect_worker_using_delete(self):
        """Test case for disconnect_worker_using_delete

        Disconnect a worker from a master  # noqa: E501
        """
        pass

    def test_do_backup_using_get(self):
        """Test case for do_backup_using_get

        Initiate a cluster backup  # noqa: E501
        """
        pass

    def test_do_restore_using_get(self):
        """Test case for do_restore_using_get

        Initiate a cluster restore  # noqa: E501
        """
        pass

    def test_get_master_using_get(self):
        """Test case for get_master_using_get

        Get information about a master  # noqa: E501
        """
        pass

    def test_get_workers_for_master_using_get(self):
        """Test case for get_workers_for_master_using_get

        Get workers connected to a master  # noqa: E501
        """
        pass

    def test_set_master_using_post(self):
        """Test case for set_master_using_post

        Set master attribute  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()