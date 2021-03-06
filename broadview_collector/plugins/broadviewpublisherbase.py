# (C) Copyright Broadcom Corporation 2016
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
#
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from broadview_lib.pt.pt_parser import PTParser
from broadview_lib.bst.bst_parser import BSTParser
from broadview_lib.bhd.bhd_parser import BHDParser

class BroadViewPublisherBase(object):
    def __init__(self):
        pass

    def publish(self, host, data):
        raise NotImplementedError

    def isBST(self, parser):
        return isinstance(parser, BSTParser)

    def isPT(self, parser):
        return isinstance(parser, PTParser)

    def isBHD(self, parser):
        return isinstance(parser, BHDParser)

