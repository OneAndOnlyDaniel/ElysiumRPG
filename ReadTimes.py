import io
import datetime as dt
import sys
import time

class myEvent:
	def __init__(self, startTime, endTime, eventName = "eventName", description = ""):
		self.startTime = startTime
		self.endTime = endTime
		self.eventName = eventName
		self.description = description

	def __str__(self):
		return "{0},{1},{2},{3}".format(str(self.startTime), str(self.endTime),self.eventName,self.description)

	def getDuration():
		return (endTime - startTime)

def stringToEvent(inp):
	mySplit = inp.split(",")
	sT = stringToDateTime(mySplit[0])
	eT = stringToDateTime(mySplit[1])
	return myEvent(sT, eT, mySplit[2], mySplit[3])

def stringToDateTime(inp):
	temp = inp.split(" ")
	myDate = temp[0]
	temp2 = myDate.split("-")
	year = temp2[0]
	month = temp2[1]
	day = temp2[2]
	myTime = temp[1]
	temp3 = myTime.split(":")
	hour = temp3[0]
	minute = temp3[1]
	second = temp3[2]

	return dt.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))

formatString = "%Y-%m-%d %H:%M:%S"

f = open("Times.csv", "r")
s = f.read()
ss = s.split('\n')

for r in ss:
	if r == "" or r == "\n":
		break

	print(stringToEvent(r))