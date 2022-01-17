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
		try:
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
		except Exception as e:
			print(e)
		finally:
			line = file.readline()
	

dataReader("TEST14.CSV", "585", components)

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

cLen = len(component.times)
startV = cLen-1000
stopV = cLen
print(len(component.times))
times = component.times[startV:stopV]

#plt.plot(times,component.reading["Pressure5"][startV:stopV],'ro')
#plt.plot(times,component.reading["Pressure6"][startV:stopV],"bo")
#plt.plot(times,component.reading["Pressure7"][startV:stopV],"go")
#plt.plot(times,component.reading["Pressure8"][startV:stopV],"mo")
plt.show()


		
		
    
		

    
		