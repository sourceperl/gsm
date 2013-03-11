# this is a gnuplot file
# file in public domain
set terminal png size 1200, 700
set output "gsm_rssi.png"

set title "GSM rapport de couverture"
set key left

# setup graph margin
set lmargin 10
set bmargin 8

# time format on CSV file
set timefmt "%d-%m-%Y %H:%M"
# time format to print
set format x "%d/%m/%Y"

# display grid on background
set grid

set xdata time
set xtics rotate by -45

# x/y axes legends
set xlabel "date" offset 0,-2
set ylabel "RSSI (dBm)"

# y between -110 and -48 dBm
set yrange [-110:-48]

# for decode CSV file
set datafile separator ","
# plot result
plot "gsm_log.csv" using 9:7 title "orange" lt rgb "#cc3333", \
     "gsm_log.csv" using 9:8 title "sfr" lt rgb "#33cc33", \
     "gsm_log.csv" using 9:8 title "bouygues" lt rgb "#3333cc", \
     "gsm_log.csv" using 9:8 title "free" lt rgb "#333333"
