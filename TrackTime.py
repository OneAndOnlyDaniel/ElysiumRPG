import io
import datetime as dt
import sys
import time

formatString = "%Y-%m-%d %H:%M:%S"

startTime = dt.datetime.today()
print("Starting timetrackign at time : {0}\n".format(startTime.strftime(formatString)))
input("Press any button to stop tracking time")
endTime = dt.datetime.today()
print("Ended timetrackign at time : {0}\n".format(endTime.strftime(formatString)))

event = "Enter Name for the Event"
description = ""

if len(sys.argv) > 1:
	event = sys.argv[1]
	if len(sys.argv) > 2:
		description = sys.argv[2]

f = open("Times.csv", "a")
f.write("{0},{1},{2},{3}\n".format(startTime.strftime(formatString), endTime.strftime(formatString), event, description))

print("Successfully wrote to file")