#Kyle Pasco and Kellie Suehisa
#This algorithm is run to parse the airport name, latitude,  and longitude
#Run algorithm in X-Plane 10\Resources\default scenery\default apt dat\Earth nav data
#Move airportdata.py file to C:\X-Plane 10\GarminSmartNav which is a folder created manually
#Call to this function only needs to be done once per update of X-Plane

import string
import re

f = open('apt.dat')
lines = f.readline()
flag2 = False
finalarray = []
airport = ""
lat = ""
lon = ""
while lines :
	if lines == "\n":
		flag = True
		while lines == "\n":
			lines = f.readline()
		#re.split('\s',lines)
	else:
		flag = False
	if flag and (lines[0] == "1"):
		flag2=True
#	elif lines !="\n":
#		flag = False
	if flag2:
		count = 0
		i = 2
		prev = 0
		while (count < 4) and (i < len(lines)-1):
			if(lines[i] != " " and prev == 0):
				count+=1
				prev=1
			else:
				if lines[i] != " ":
					prev = 1
				else:
					prev = 0
			i+=1
		i-=1
		if (count == 4) and (i+5 <= len(lines)):
			for j in range(0,4):
				if not (re.match('[A-Z]|[0-9]', lines[j+i])):
					flag2 = False
					flag = False 
			if lines[j+i+1] != " ":
				flag2 = False
				flag = False
			if flag2 == True:
				airport = lines[i:i+4]
			else:
				flag2 = False
				flag = False
	if flag2:
		lines=f.readline()
		if (lines[0:3] == "100"):
			i=4
			count = 0
			prev = 0
			while (count < 9) and (i < len(lines)-1):
				if(lines[i] != " " and prev == 0):
					count+=1
					prev=1
				else:
					if lines[i] != " ":
						prev = 1
					else:
						prev = 0
				i+=1
			i-=1
			if (count == 9):
				k=i
				while ( lines[i] != "."):
					if (re.match('[-]|[0-9]', lines[i])):
						i+=1
					else:
						flag2 = False
						flag = False
				i+=1
				while ( lines[i] != " "):
					if (re.match('[0-9]', lines[i])):
						i+=1
					else:
						flag2 = False
						flag = False
				if lines[i] != " ":
					flag2 = False
					flag = False
				if flag2 == True:
					lat=lines[k:i]
					count += 1
				else:
					flag2 = False
					flag = False
			if (count == 10):
				while (lines[i] == " "):
					i+=1
				k=i
				while ( lines[i] != "."):
					if (re.match('[-]|[0-9]', lines[i])):
						i+=1
					else:
						flag2 = False
						flag = False
				i+=1
				while ( lines[i] != " "):
					if (re.match('[0-9]', lines[i])):
						i+=1
					else:
						flag2 = False
						flag = False
				if lines[i] != " ":
					flag2 = False
					flag = False
				if flag2 == True:
					lon = lines[k:i]
					finalarray.append(airport)
					finalarray.append(lat)
					finalarray.append(lon)
				else:
					flag2 = False
					flag = False
	lines=f.readline()
	finalarray = finalarray
#f2.close()
f.close()

f2 = open('airportdata.py', 'w+')
#finalarray.tofile('f2')
f2.write("def getApts():\n")
f2.write("\treturn [")
for z in range(0,len(finalarray)):
	if z%3 == 0:
		f2.write("\"")
	f2.write(finalarray[z])
	if z%3 == 0:
		f2.write("\"")
	if z != (len(finalarray)-1):
		f2.write(", ")
f2.write("]")
f2.close