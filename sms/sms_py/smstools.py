#!/usr/bin/python3

# 
# interface to SMStools for send SMS messages
#
#
# code under GPLv3

import tempfile
import os
import stat

class SMS:
  """
  Allows control of smsd server (package debian smstools)

  Example :
    sms = SMS()
    sms.set_phone("+44712345678")
    sms.send("it's a SMS message")
  """

  def __init__(self):
    """Class builder"""
    self.phone_number = ""
    self.out_dir      = "/var/spool/sms/outgoing/"
    self.stat_dir     = "/var/log/smstools/smsd_stats/"
    self.stat_file    = self.stat_dir + "status"
    self.last_rssi    = 0
  
  def set_phone(self, phone_number):
    """Set phone number: syntax like +44712345678"""
    self.phone_number = phone_number
  
  def get_rssi(self):
    """Return the current RSSI (in dBm) or 0 if fail"""
    # open stat file and parse it
    with open(self.stat_file, 'r') as self.statf:
      try:
        self.last_rssi = int(self.statf.readlines()[1].split(',')[5].strip().split(' ')[1])
      except ValueError:
        self.last_rssi = 0
    self.statf.close
    return self.last_rssi
 
  def send(self, sms_msg):
    """Send a SMS: build SMS file for smsd in outgoing dir."""
    # create temp file
    fdsms, fsms = tempfile.mkstemp(prefix="sms-", dir=self.out_dir)
    # open it, set SMS data
    with os.fdopen(fdsms, "wt") as self.outf:
      self.outf.write("To: " + self.phone_number + "\n")
      self.outf.write("\n")
      self.outf.write(sms_msg)
    self.outf.close
    # change file mode (read by smsd user)
    os.chmod(fsms, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
