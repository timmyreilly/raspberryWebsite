import time
from helperFUNctions import *

from azure.storage import Entity, QueueService

import spidev 

spi = spidev.SpiDev()
spi.open(0,0)

myaccount = getAccount()
mykey = getKey()

queue_service = QueueService(account_name=myaccount, account_key=mykey)

queue_service.create_queue('mlqueue')

i = 0

periods = ('a', 'b', 'c', 'd')


def analog_read(channel):
        r = spi.xfer2([1, (8 + channel) << 4, 0])
        adc_out = ((r[1]&3) << 8) + r[2]
        return adc_out

a_r = analog_read


#a_r = generateRandom

#a_r(0)

def get_state():
    record = {}
    for abcd in periods: 
        time.sleep(0.25)
        record.update({abcd+'X': a_r(0), abcd+'Y': a_r(1), abcd+'Z': a_r(2)})
        print record
    return record

m_l = make_list_from_dict
m_d = make_data
g_r = get_result_from_ml
r_r = return_states_from_request


def receive_states_from_current_state(record):
    '''
    Pass get_state() to receive a tuple of two states
    '''
    return r_r(g_r(m_d(m_l(record),m_l(record))))


while True:
    s = get_state()
    queue_service.put_message('mlqueue', return_states_from_request(get_result_from_ml(make_data(make_list_from_dict(s),make_list_from_dict(s)))))




