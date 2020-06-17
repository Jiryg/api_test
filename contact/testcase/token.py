import json
import requests
import yaml
import logging


class Weiwork(object):
    # logging.basicConfig()
    # _logger = logging.getLogger("gongzuo")
    # _logger.setLevel(level=logging.DEBUG)
    _token = ""

    @classmethod
    def get_token(cls):
        if len(cls._token) == 0:
            cls._token = cls.get_token_new()
        return cls._token

    @classmethod
    def get_token_new(cls):
        conf = yaml.safe_load(open("D:\\PycharmProjects\\firstDemo\\wework\\contact\\data\\weiwork.yaml"))
        print(conf["env"])

        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                         params={"corpid": conf["env"]["corpid"],
                                 "corpsecret": conf["env"]["corpsecret"]}
                         )

        # logging.debug("access_token是：", json.dumps(r, indent=2))
        print("gettoken接口的返回是：", r.json())
        print(r.text)
        cls._token = r.json()["access_token"]
        return cls._token

if __name__ == '__main__':
    Weiwork.get_token
    # Weiwork.get_token_new()