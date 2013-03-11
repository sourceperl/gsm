format.txt	CSV format reference
gsm_log.csv	CSV GSM RSSI database
gsm_plot.gnu	gnuplot file for graphic report
gsmlog.cron	copy to /etc/cron.d/ to launch gsmlogger every 5 min
		write result to /home/pi/log/gsm_log.csv
gsmlogger	python script to retrieve data (rssi, cell_id...) from GSM
