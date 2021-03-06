# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.all_containers_response_description import AllContainersResponseDescription  # noqa: F401,E501
from swagger_server import util


class AllContainersResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, command: str=None, description: List[AllContainersResponseDescription]=None):  # noqa: E501
        """AllContainersResponse - a model defined in Swagger

        :param command: The command of this AllContainersResponse.  # noqa: E501
        :type command: str
        :param description: The description of this AllContainersResponse.  # noqa: E501
        :type description: List[AllContainersResponseDescription]
        """
        self.swagger_types = {
            'command': str,
            'description': List[AllContainersResponseDescription]
        }

        self.attribute_map = {
            'command': 'command',
            'description': 'description'
        }
        self._command = command
        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'AllContainersResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AllContainersResponse of this AllContainersResponse.  # noqa: E501
        :rtype: AllContainersResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def command(self) -> str:
        """Gets the command of this AllContainersResponse.

        type of results: ok or error  # noqa: E501

        :return: The command of this AllContainersResponse.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command: str):
        """Sets the command of this AllContainersResponse.

        type of results: ok or error  # noqa: E501

        :param command: The command of this AllContainersResponse.
        :type command: str
        """

        self._command = command

    @property
    def description(self) -> List[AllContainersResponseDescription]:
        """Gets the description of this AllContainersResponse.


        :return: The description of this AllContainersResponse.
        :rtype: List[AllContainersResponseDescription]
        """
        return self._description

    @description.setter
    def description(self, description: List[AllContainersResponseDescription]):
        """Sets the description of this AllContainersResponse.


        :param description: The description of this AllContainersResponse.
        :type description: List[AllContainersResponseDescription]
        """

        self._description = description
