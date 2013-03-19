#!/usr/bin/python3

# 
#  interface to SMStools for send SMS messages
#
#
# code under GPLv3


import tempfile
import os
import stat

## some vars
SMS_DEST = "+33781xxxxxx"

## sub define
def send_sms(sms_number, sms_msg):
  # create temp file
  fdsms, fsms = tempfile.mkstemp(prefix="sms-", dir="/var/spool/sms/outgoing/")
  
  # open it, set SMS data
  outf = os.fdopen(fdsms, "wt")
  outf.write("To: " + sms_number + "\n")
  outf.write("\n")
  outf.write(sms_msg)
  outf.close

  # change file mode (read by smsd user)
  os.chmod(fsms, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)

## main code
# some tests...
send_sms(SMS_DEST, "SMS 1")
