# Copyright 2017 INAP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client as keystone_client

from almanachclient import exceptions


class KeystoneClient(object):
    def __init__(self, auth_url, username, password, service, region_name,
                 domain_name='default', user_domain_id='default'):
        self.auth_url = auth_url
        self.username = username
        self.password = password
        self.service = service
        self.region_name = region_name
        self.domain_name = domain_name
        self.user_domain_id = user_domain_id

    def get_endpoint_url(self, visibility='admin'):
        keystone = self._get_keystone_client()
        endpoints = keystone.endpoints.list(service=self.service, region=self.region_name)

        for endpoint in endpoints:
            if endpoint.interface == visibility:
                return endpoint.url

        raise exceptions.EndpointNotFound('Endpoint URL Not Found')

    def _get_keystone_client(self):
        auth = v3.Password(auth_url=self.auth_url,
                           username=self.username,
                           password=self.password,
                           domain_name=self.domain_name,
                           user_domain_id=self.user_domain_id)

        sess = session.Session(auth=auth)
        return keystone_client.Client(session=sess)
