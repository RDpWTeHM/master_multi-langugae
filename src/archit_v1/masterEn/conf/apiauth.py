# conf/apiauth.py
"""the third-part API configuration file
"""

import os
from collections import namedtuple


BaiduAuth = namedtuple(
    'BaiduAuth',
    ['app_id', 'key', ])

baiduauth = BaiduAuth(
    app_id=os.environ.get('appid', '20151113000005349'),
    key=os.environ.get('authkey', 'osubCEzlGjzvw8qdQc41'),
)


#
# check enviornment!
#
# n/a
