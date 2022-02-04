# coding: utf-8

"""
    GraphDB Workbench API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from graphdb.graphdb_workbench.configuration import Configuration


class Account(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'app_settings': 'object',
        'date_created': 'datetime',
        'granted_authorities': 'list[str]',
        'password': 'str',
        'username': 'str'
    }

    attribute_map = {
        'app_settings': 'appSettings',
        'date_created': 'dateCreated',
        'granted_authorities': 'grantedAuthorities',
        'password': 'password',
        'username': 'username'
    }

    def __init__(self, app_settings=None, date_created=None, granted_authorities=None, password=None, username=None, _configuration=None):  # noqa: E501
        """Account - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._app_settings = None
        self._date_created = None
        self._granted_authorities = None
        self._password = None
        self._username = None
        self.discriminator = None

        if app_settings is not None:
            self.app_settings = app_settings
        if date_created is not None:
            self.date_created = date_created
        if granted_authorities is not None:
            self.granted_authorities = granted_authorities
        if password is not None:
            self.password = password
        if username is not None:
            self.username = username

    @property
    def app_settings(self):
        """Gets the app_settings of this Account.  # noqa: E501


        :return: The app_settings of this Account.  # noqa: E501
        :rtype: object
        """
        return self._app_settings

    @app_settings.setter
    def app_settings(self, app_settings):
        """Sets the app_settings of this Account.


        :param app_settings: The app_settings of this Account.  # noqa: E501
        :type: object
        """

        self._app_settings = app_settings

    @property
    def date_created(self):
        """Gets the date_created of this Account.  # noqa: E501


        :return: The date_created of this Account.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this Account.


        :param date_created: The date_created of this Account.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def granted_authorities(self):
        """Gets the granted_authorities of this Account.  # noqa: E501


        :return: The granted_authorities of this Account.  # noqa: E501
        :rtype: list[str]
        """
        return self._granted_authorities

    @granted_authorities.setter
    def granted_authorities(self, granted_authorities):
        """Sets the granted_authorities of this Account.


        :param granted_authorities: The granted_authorities of this Account.  # noqa: E501
        :type: list[str]
        """

        self._granted_authorities = granted_authorities

    @property
    def password(self):
        """Gets the password of this Account.  # noqa: E501


        :return: The password of this Account.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Account.


        :param password: The password of this Account.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def username(self):
        """Gets the username of this Account.  # noqa: E501


        :return: The username of this Account.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Account.


        :param username: The username of this Account.  # noqa: E501
        :type: str
        """

        self._username = username

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Account, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Account):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Account):
            return True

        return self.to_dict() != other.to_dict()
