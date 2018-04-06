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


class Diagnostics(Model):
    """Error diagnostic information for failed jobs.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar message: The error message.
    :vartype message: str
    :ivar severity: The severity of the error. Possible values include:
     'Warning', 'Error', 'Info', 'SevereWarning', 'Deprecated', 'UserWarning'
    :vartype severity: str or
     ~azure.mgmt.datalake.analytics.job.models.SeverityTypes
    :ivar line_number: The line number the error occured on.
    :vartype line_number: int
    :ivar column_number: The column where the error occured.
    :vartype column_number: int
    :ivar start: The starting index of the error.
    :vartype start: int
    :ivar end: The ending index of the error.
    :vartype end: int
    """

    _validation = {
        'message': {'readonly': True},
        'severity': {'readonly': True},
        'line_number': {'readonly': True},
        'column_number': {'readonly': True},
        'start': {'readonly': True},
        'end': {'readonly': True},
    }

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'severity': {'key': 'severity', 'type': 'SeverityTypes'},
        'line_number': {'key': 'lineNumber', 'type': 'int'},
        'column_number': {'key': 'columnNumber', 'type': 'int'},
        'start': {'key': 'start', 'type': 'int'},
        'end': {'key': 'end', 'type': 'int'},
    }

    def __init__(self, **kwargs) -> None:
        super(Diagnostics, self).__init__(**kwargs)
        self.message = None
        self.severity = None
        self.line_number = None
        self.column_number = None
        self.start = None
        self.end = None