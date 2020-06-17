import time
import yaml
import pystache


class Utils:
    @classmethod
    def parse(cls, template_path, dict):
        template = "".join(open(template_path).readlines())
        return pystache.render(template, dict)

    @classmethod
    def udid(cls):
        return str(time.time()).replace(".", "")[0:11]

    @classmethod
    def getYamlContent(cls, path):
        dict = yaml.safe_load(open(path, 'r', encoding='UTF-8'))
        print(dict)
        return dict

    # @classmethod
    # def analyzingYaml(cls, path):
    #     dict = yaml.safe_load(open(path, 'r', encoding='UTF-8'))
    #     print(dict)

if __name__ == '__main__':
    file_path = 'wework/contact/data/user_create.yaml'
    Utils.getYamlContent(file_path)