#!/usr/bin/env python3.9
"""Write."""


import logging
import sys
import time

import pysher  # type: ignore

root = logging.getLogger()
root.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
root.addHandler(ch)

pusher = pysher.Pusher("73bcb26ed6d04c63889a", cluster="eu")

print("test")

AC_RR = 2


def write_status_sextoy(write_vitesse):
    """Write."""
    with open("sextoy.txt", "w", encoding="utf-8") as file:
        file.write(write_vitesse)
        file.close()


def my_func(*args, **kwargs):
    """Write."""
    print("processing Args:", args)
    write_status_sextoy(args[0])
    print("processing Kwargs:", kwargs)


# We can't subscribe until we've connected, so we use a callback handler
# to subscribe when able
def connect_handler():
    """Write."""

    channel = pusher.subscribe("my-channel")
    channel.bind("my-event", my_func)


pusher.connection.bind("pusher:connection_established", connect_handler)
pusher.connect()

while True:
    time.sleep(1)
