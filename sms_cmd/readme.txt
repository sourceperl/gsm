## files:

initpiface	init the piface board on raspberry pi (call at startup)
pifacestart	init.d startup script for initpiface
smscheck	eventhandler for smsd (call by smsd, see smsd.conf)
smsd.conf 	/etc/smsd.conf configuration file (for smstools package)
sendsms 	bash script for send SMS from command line

## setup:
	
	# /usr/local/bin is for user script (debian policy)
	sudo cp initpiface /usr/local/bin
	sudo cp smscheck /usr/local/bin
	sudo cp sendsms /usr/local/bin
	sudo chmod +x /usr/local/bin/initpiface
	sudo chmod +x /usr/local/bin/smscheck
	sudo chmod +x /usr/local/bin/sendsms

	# copy init script for launch initpiface at startup
	sudo cp pifacestart /etc/init.d
	sudo chown root pifacestart
	sudo chgrp root pifacestart
	# use insserv to enable the init script 
        # since debian 6 : update-rc.d is now deprecated
	sudo insserv -v /etc/init.d/pifacestart
	
	# install smstools
	sudo apt-get install smstools
	# copy smstools config
	sudo cp smsd.conf /etc/
	# restart (load smsd.conf)
	sudo /etc/init.d/smstools restart

	# to test it reboot or launch directly initpiface to setup the board
