# -*- coding: utf-8 -*-

"""
SimpleApi
"""

import json
import requests
import string
import random

file_name = 'UserAgents.txt'

SERVICE_URL = 'http://simpleapi.info/apps/numbers-info/info.php?results=json',
SYNC_URL = 'http://simpleapi.info/apps/numbers-info/sync.php?device_id={0}'


def synchronize(number, name='Not Found'):
    """

    :param number: phone number
    :param name: fake personal name
    :return: Success or Failed
    """

    agent = random.choice(open(file_name).readlines())
    rnd = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(16)])
    sync_url = SYNC_URL.format(rnd)
    headers = {'User-Agent': agent.strip()}
    number = '"{0}"'.format(number)
    name = '"{0}"'.format(name)
    # data = '{%s: [%s, %s, %s, %s, %s]}' % (number, name, name, name, name, name)
    data = '{%s: %s}' % (number, name)
    payload = {"data": data}
    response = requests.post(sync_url, headers=headers, data=payload)

    if response.status_code != 200:
        return False

    return response.content.decode('utf-8')
