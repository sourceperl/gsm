## files:

10-fix-serial.rules	fix SYMLINK for serial ports (GSM, GPS)
piface/initpiface	init the piface board on raspberry pi (call at startup)
piface/pifacestart	init.d startup script for initpiface
smsd/smscheck		eventhandler for smsd (call by smsd, see smsd.conf)
smsd/smsd.conf 		/etc/smsd.conf configuration file (for smstools package)

## setup:
	
	# set udev rules for fix serial ports (ex /dev/ttyGSM for modem)
	# ! see syslog to find serial number of every FTDI chip
	# ! update 10-fix-serial.rules with serial number
	cp udev/10-fix-serial.rules /etc/udev/rules.d/

	# reconnect usb serial device
	# check FTDI device SYMLINK
	ls -la /dev/tty*

	# install gpsd	
	sudo apt-get install gpsd gpsd-clients

	# setup gpsd (set manual conf and device is /dev/ttyGPS)
	sudo dpkg-reconfigure gpsd

	# /usr/local/bin is for user script (debian policy)
	sudo cp piface/initpiface /usr/local/bin
	sudo cp piface/smscheck /usr/local/bin
	sudo chmod +x /usr/local/bin/initpiface
	sudo chmod +x /usr/local/bin/sendsms

	# copy init script for launch initpiface at startup
	sudo cp piface/pifacestart /etc/init.d
	cd /etc/init.d
	sudo chown root pifacestart
	sudo chgrp root pifacestart
	# use insserv to enable the init script 
        # since debian 6 : update-rc.d is now deprecated
	sudo insserv -v /etc/init.d/pifacestart
	
	# install smstools
	sudo apt-get install smstools
	# copy smstools config
	sudo cp smsd/smsd.conf /etc/
	# restart (load smsd.conf)
	sudo /etc/init.d/smstools restart

	# to test it reboot or launch directly initpiface to setup the board
