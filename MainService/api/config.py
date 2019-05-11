# -*- coding: utf-8 -*-
# @Author: ahmedkammorah
# @Date:   2017-01-22 02:45:44
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-05-11 15:35:07

import os

BASE_HOST = os.environ.get('BASE_HOST', 'localhost')
BASE_REST_PORT = 5000

RPC_SERVER = BASE_HOST
RPC_PORT = 50051

# AUTH
AK_API_JWT_SECRET_KEY = os.environ.get('AK_API_JWT_SECRET_KEY', None)
AK_JWT_ALGORITHM = 'HS256'

DOCS_HOST = '{}:{}'.format(BASE_HOST,BASE_REST_PORT)

MAIN_DEFAULT_USER = {
  'username':'demo',
  'password':'f82fa358a6a100de1815fa0d57f876fda078d9e136494f1589d9d894'
}

