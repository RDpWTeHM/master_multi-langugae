# masterencore/tests.py
"""
Usage:
  masterEn/ $ python -m unittest masterencore/tests.py

Note:
  The reason of 'Usage' CMD work at masterEn/ directory
is masterencore/ as pakage, and depends on conf/ directory to
setup some configurations.
  That effect "from .fanyiapi import baidu as translapi" too
which need relative import.
"""

# import os
# import sys
import unittest


class TestBaiduFanyiAPI(unittest.TestCase):
    from .fanyiapi import baidu as translapi

    def test_EN_to_CN_functional(self):
        en = 'apple'
        cn_for_check = '苹果'
        cn_from_api = None

        api_resp = self.translapi.fanyi(en)
        cn_from_api = api_resp['trans_result'][0]['dst']

        self.assertEqual(cn_from_api, cn_for_check,
                         "'apple' --to--> '苹果' failure!!!")


if __name__ == '__main__':
    unittest.main()
