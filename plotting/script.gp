# GnuPlot script file

set title "LinearLeastSquares"

set term postscript eps enhanced color
set output '|ps2pdf - plot.pdf'

#set terminal postscript
#set output "plot.eps"
plot "1.dat" with lines lw 2 lt -1, "2.dat" with points lw 7 lt 3
