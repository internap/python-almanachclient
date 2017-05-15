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

from almanachclient.http_client import HttpClient


class Client(HttpClient):
    api_version = 'v1'

    def __init__(self, url):
        self.url = url

    def get_url(self):
        return self.url

    def get_info(self):
        return self._get('{}/{}/info'.format(self.url, self.api_version))