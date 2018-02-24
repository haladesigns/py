import sys
logfile = open('./tmp/log.txt', 'a')
#for i in range(0,5):
num_lines = sum(1 for line in open('./tmp/log.txt', 'r')) #count number of lines
logfile.write("Catastrophic ERROR" + str(num_lines + 1) + "\n")
logfile.close()
