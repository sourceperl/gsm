#!/usr/bin/python3

#
#  interface to SMStools for send SMS messages
#
#  code under GPLv3

from smstools import SMS
import pifacedigitalio as p
import time

# some private const
import private
SMS_DEST = private.SMS_DEST

# main code
# Smsd init
sms = SMS()
sms.set_phone(SMS_DEST)
print(sms.get_rssi())

# piface board init
p.init(False)

# init loop
bit  = p.digital_read(0)
_bit = bit

# change detect loop
while(True):
  bit = p.digital_read(0)
  if (bit != _bit): 
    sms.send("Relay 0 : status " + str(bit))
  _bit = bit
  time.sleep(1)
