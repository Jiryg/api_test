import requests

from wework.contact.utils import Utils


class Department(Utils):
    parentid = 1
    id = 2
    def ceate_departmetn(self, token):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        data = {
            "name": "广州研发中心",
            "name_en": "RDGZ",
            "parentid": self.parentid,
            "order": 1,
            "id": self.id
        }
        r = requests.post(url,
                          params={"access_token": token},
                          data=data).json()
        return r

    def update_department(self, token):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/update"
        data = {
            "id": self.id,
            "name": "广州研发中心",
            "name_en": "RDGZ_改名字",
            "parentid": self.parentid,
            "order": 1
        }
        r = requests.post(url,
                          params={"access_token": token},
                          data=data).json()
        return r

    def delete_department(self, token):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"
        r = requests.get(url,
                         params={"access_token": token,
                                  "id": self.id}).json()
        return r

    def get_department_list(self, token):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
        r = requests.get(url, params={"access_token": token}).json()
        return r