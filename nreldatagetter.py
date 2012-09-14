
import urllib, urllib2


base_query = {
	# period must span less than one year
	# if shrmn and ehrmn are different, data for each 5-minute interval
	# between them will be retrieved.
	'syear': '2011',
	'smonth':'08',
	'sday':'16',
	'shrmn':'0000',
	'eyear': '2012',
	'emonth':'08',
	'eday':'15',
	'ehrmn':'2300',

	'outputgif': '0',
	'5':'on',
	'type': 'data'
	}

print 'building query'
query = urllib.urlencode(base_query)

print 'opening url'
data = urllib2.urlopen('http://www.nrel.gov/midc/apps/plotspec.pl', query)

print 'saving response'
csv = open('nrel.csv', 'w')
csv.write(data.read())
csv.close()

