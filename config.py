from classes import Component
from datetime import date

fileName = "CONFIG.CSV"

def configReader(fileName):
	file = open(fileName, "r")
	line = file.readline()
	components = []
	while line != "":
		sepLine = line.split(",")
		compID = sepLine[0]
		name = sepLine[1]	
		dist = sepLine[3]
		tDate = str(date.today())
		qualities = sepLine[5]
		comp = Component(qualities, name, compID, tDate, dist)
		components.append(comp)
		#print("Added component: " + name)
		line = file.readline()
		
	return components

	