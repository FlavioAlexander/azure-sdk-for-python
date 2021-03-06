# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GroupAddMemberParameters(Model):
    """Request parameters for adding a member to a group.

    :param url: Member Object Url as
     "https://graph.windows.net/0b1f9851-1bf0-433f-aec3-cb9272f093dc/directoryObjects/f260bbc4-c254-447b-94cf-293b5ec434dd",
     where "0b1f9851-1bf0-433f-aec3-cb9272f093dc" is the tenantId and
     "f260bbc4-c254-447b-94cf-293b5ec434dd" is the objectId of the member
     (user, application, servicePrincipal, group) to be added.
    :type url: str
    """ 

    _validation = {
        'url': {'required': True},
    }

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
    }

    def __init__(self, url):
        self.url = url
