import unittest
from easyrpa.tools import str_tools,transfer_tools

class StrToolsTest(unittest.TestCase):
    def test_str_to_str_dict(self):
        test_str = '{"message_key1":666,"message_key2":"mkv2","message_key3":{"mk1":"mkv1","mk2":908,"mk3":[5,6,9],"mk4":{"mmk1":78.23},"mk5":[{"mmk51":33.3,"mm52":"32"}]},"message_key4":[{"mk41":369,"mk42":"963","mk43":false}],"message_key5":true,"message_key6":false,"message_key7":null}'
        result = str_tools.str_to_str_dict(test_str)
        print(result)

class TransferToolsTest(unittest.TestCase):
    def test_dict_to_str_dict(self):
        # todo
        pass

#unittest.main()作为主函数入口
if __name__ == '__main__':
    unittest.main()