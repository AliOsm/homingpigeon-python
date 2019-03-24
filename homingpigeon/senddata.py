#!/usr/bin/python

import requests

HP_URL = 'https://homingpigeon.herokuapp.com'
REQUEST_URL = '%s/%s'

class SendData():
    def __init__(self, token, data, dtype='string'):
        self.token = token
        self.data = data
        self.dtype = dtype

        # support json in future releases of HomingPigeon
        self.dtype = 'string'

        self.__send_data()

    def __send_data(self):
        print('Start sending the data through your PIGEON!!!')
        r = requests.get(url=REQUEST_URL % (HP_URL, self.token), params={'information': self.data}).json()
        if r['status'] == 'pigeon_message_created':
            print('Your data arrived safely!')
        else:
            print('There was some errors while your data travel')
