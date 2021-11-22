from classes import Component 
from config import configReader
import matplotlib.pyplot as plt

components = configReader("CONFIG.CSV")

def dataReader(fileName, componentID, components):
	file = open(fileName, "r")
	line = file.readline()

	for i in components:
		if i.compID == componentID:
			component = i
			break
	
	while line:
		sepLine = line.split(",")
		#print(sepLine)
		if (sepLine[0][0].isdigit() == True):
			compIdR = sepLine[1].split('x')[1]
			if compIdR == componentID:
				timeR = sepLine[0].split(" ")[1]
				dataR = sepLine[2]
				component.addReading(dataR)
				component.addTime(timeR)
				
		else:
			#print("IGNORED!")
			pass
		line = file.readline()
	

dataReader("TEST10.CSV", "585", components)

for i in components:
	if i.compID == "585":
		component = i
		break

keys = component.reading.keys()
#for key in keys:
#	plt.plot(component.reading[key], component.times)
#	plt.ylabel(key)
#	plt.xlabel("Time")
#plt.show()


#print(component.reading["Pressure5"])

plt.plot(component.times,component.reading["Pressure5"],'ro')
plt.plot(component.times,component.reading["Pressure6"],"bo")
plt.plot(component.times,component.reading["Pressure7"],"go")
plt.plot(component.times,component.reading["Pressure8"],"mo")
plt.show()


		
		
    
		

    
		