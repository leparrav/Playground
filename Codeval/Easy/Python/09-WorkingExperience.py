'''
https://www.codeeval.com/open_challenges/139/
'''
import sys

months = {
			'Jan': 0,
			'Feb': 1,
			'Mar': 2,
			'Apr': 3,
			'May': 4,
			'Jun': 5,
			'Jul': 6,
			'Aug': 7,
			'Sep': 8,
			'Oct': 9,
			'Nov': 10,
			'Dec': 11 }

'''
Return start month, start year, end month and end year - For each date
'''
def getDates(date):
	date_list = date.lstrip().split("-")
	start_date = date_list[0].split(" ")
	smonth = months[start_date[0]]
	syear = start_date[1]
	end_date = date_list[1].split(" ")
	emonth = months[end_date[0]]
	eyear = end_date[1]
	return int(smonth),int(syear),int(emonth),int(eyear)


def main():
	with open(sys.argv[1],'r') as date_file:
		for line in date_file.readlines():
			years = {i: [False for unused in xrange(12)] for i in xrange(1990, 2021)}
			list_dates = line.rstrip().split(";")
			for date in list_dates:
				smonth,syear,emonth,eyear = getDates(date)
			 	period_years = xrange(syear, eyear + 1)
			 	for y in period_years:
					start_point = smonth if y == syear else 0
					end_point = emonth + 1 if y == eyear else 12
					for month in xrange(start_point, end_point):
						years[y][month] = True
			total_months = sum(sum(1 for j in years[i] if j) for i in years.keys())
			print total_months / 12

if __name__ == '__main__':
    main()