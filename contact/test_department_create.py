import pytest
import requests
from wework.contact.testcase.token import Weiwork
from wework.contact.utils import Utils


class TestDepartmentCreate(object):
    def test_create(self, token):
        self.file_path = "/wework/contact/data/user_create.yaml"
        self.data = {
            "userid": "zhangsan",
            "name": "张三",
            "mobile": "13800000000",
            "department": [1, 2],
            "order": [10, 40],
            "position": "产品经理",
            "email": "zhangsan@gzdev.com",
            "is_leader_in_dept": [1, 0]
        }

        self.content = Utils.getYamlContent(self.file_path)
        self.request_method = self.content["test_info"]["request_type"]
        self.request_url = self.content["test_info"]["url"]
        self.params = self.content["test_info"]["params"]
        print(self.request_method)
        print(self.request_url)
        print(self.params[0])
        for k in self.params[0].keys():
            print(self.params[0][k])
            # if self.params[0][k].startswith('$'):
            #     self.params[0][k].replace('$', '')
            #     print(self.params[0][k])
            if k == 'access_token':
                self.params[0][k] = Weiwork._token
        # print(self.params[0])
        if self.request_method.lower() == 'post':
            r = requests.post(url=self.request_url,
                              params=self.params[0],
                              data=self.data).json()
        print(r)