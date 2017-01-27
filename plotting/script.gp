# GnuPlot script file

set term postscript eps enhanced color
set output '|ps2pdf - plot.pdf'

plot \
 "1.dat" lt rgb "blue" with points, \
 "2.dat" lt rgb "red"  with points
