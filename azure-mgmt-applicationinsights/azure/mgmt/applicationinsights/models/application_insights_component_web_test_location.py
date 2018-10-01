# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ApplicationInsightsComponentWebTestLocation(Model):
    """Properties that define a web test location available to an Application
    Insights Component.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar display_name: The display name of the web test location.
    :vartype display_name: str
    :ivar tag: Internally defined geographic location tag.
    :vartype tag: str
    """

    _validation = {
        'display_name': {'readonly': True},
        'tag': {'readonly': True},
    }

    _attribute_map = {
        'display_name': {'key': 'DisplayName', 'type': 'str'},
        'tag': {'key': 'Tag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ApplicationInsightsComponentWebTestLocation, self).__init__(**kwargs)
        self.display_name = None
        self.tag = None