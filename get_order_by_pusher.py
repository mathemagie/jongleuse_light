#!/usr/bin/env python3.9

import sys
import time
import logging
import pysher

root = logging.getLogger()
root.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
root.addHandler(ch)

pusher = pysher.Pusher('73bcb26ed6d04c63889a',cluster='eu')

def write_status_sextoy(write_vitesse):
    f = open("sextoy.txt", "w")
    f.write(write_vitesse)
    f.close()

def my_func(*args, **kwargs):
    print("processing Args:", args)
    write_status_sextoy(args[0])
    print("processing Kwargs:", kwargs)

# We can't subscribe until we've connected, so we use a callback handler
# to subscribe when able
def connect_handler(data):
    channel = pusher.subscribe('my-channel')
    channel.bind('my-event', my_func)

pusher.connection.bind('pusher:connection_established', connect_handler)
pusher.connect()

while True:
    time.sleep(1)