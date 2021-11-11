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
		
print(component.reading["Pressure5"])

plt.plot(component.reading["Pressure5"], component.times)



		
		
    
		

    
		