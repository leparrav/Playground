'''
https://www.codeeval.com/open_challenges/124/
'''
import sys

def getKey(item):
	return item[1]

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			directions = line.strip().split(";")
			cities_org = []
			
			# Get cities and sort them
			for entry in directions:
				if entry:
					entry = entry.split(",")
					city, distance = entry[0],int(entry[1])
					cities_org.append([city,distance])
			cities_org = sorted(cities_org,key=getKey)

			#Print distance asked
			distance_traveled = 0
			distances = []
			for city in cities_org:
				distances.append(str(city[1]-distance_traveled))
				distance_traveled = city[1]
			print ",".join(distances)


if __name__ == '__main__':
    main()