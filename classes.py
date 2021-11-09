#TODO write translate function

# qualities => Description of what is being recorded 
# reading => main disctionary where data is saved
# date => date where data was recorded (todays date as default)
# times => times data was recorded
# dist => distribution 

class Component:
	def __init__(self, qualities, name, compID, tDate, dist):
		self.qualities = qualities.split("-")
		self.reading = {}
		#self.ID = compID + self.fileName
		#self.fileName = ""
		self.compID = compID #int("0x" + compID, 16)
		self.date = tDate
		self.name = name
		self.times = []
		self.dist = dist

	def addFileName(self, fileName):
		self.fileName = fileName
		return

	def separate(self, reading, dist):
		sepRead = []
		dists = list(dist)
		current = list(reading)
		#print(dists)
		for i in dists:
				sepRead.append(list(current)[:(int(i)*2)-1])
				for j in range((int(i)*2)-1):
					current.pop(j)
		return sepRead

	def translate(list):
		return list

	def addReading(self, reading):
		values = self.separate(reading, self.dist) 
		#for components that record multiple values in one go, code to separate the readings accordingly
		for i in range(len(self.qualities)):
				nReading = values[i] # as values are recorded as hex digits and may have more modifications these must be undone to get the actual value
				if self.qualities[i] in self.reading.keys() :
					self.reading[self.qualities[i]].append(nReading)		
				else:
					self.reading[self.qualities[i]] = [nReading]
		return			

	def addTime(self, t):
		self.times.append(t) # where times is a list of strings that denote when the readings were taken, index 0 on this list will correspond to index 0 on the readings
		return

