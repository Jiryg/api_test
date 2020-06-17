import datetime
import json
import pytest
import requests
import logging
from wework.contact.testcase.department import Department
from wework.contact.utils import Utils


class TestDepartment:
    parentid = ''

    @classmethod
    def setup_class(cls):
        cls.department = Department()
        cls.parentid = cls.department.parentid

    def test_create_depth(self, token):
        for i in range(3):
            data = {
                "name": "第二次_" + str(self.parentid)+ str(datetime.datetime.now().timestamp()),
                "parentid": self.parentid,
            }

            r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                              params={"access_token": token},
                              json=data,
                              # proxies={"https": "http://127.0.0.1:8080",
                              #          "http": "http://127.0.0.1:8080"},
                              # verify=False
                              ).json()
            print(r)
            self.parentid = r["id"]
            assert r["errcode"]==0

    @pytest.mark.run(order=1)
    def test_create_name(self, token):
        r = self.department.ceate_departmetn(token)
        logging.debug(r)

    @pytest.mark.parametrize("name", [
        "广州研发中心",
        "東京アニメーション研究所",
        "도쿄 애니메이션 연구소",
        "معهد طوكيو للرسوم المتحركة",
        "東京動漫研究所"
    ])
    def test_create_order(self, name, token):
        data = {
            "name": name+Utils.udid(),
            "parentid": self.department.parentid,
            "order": 1,
        }

        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                          params={"access_token": token},
                          json=data
                          ).json()

        #解密
        logging.debug(r)
        # assert r["errcode"]==0

    @pytest.mark.run(order=4)
    def test_delete_department(self, token):
        r = self.department.delete_department(token)
        print(json.dumps(r, indent=2))

    @pytest.mark.run(order=3)
    def test_get(self, token):
        r = self.department.get_department_list(token)
        print(json.dumps(r, indent=2))

    @pytest.mark.run(order=2)
    def test_update_department(self, token):
        r = self.department.update_department(token)
        print(json.dumps(r, indent=2))