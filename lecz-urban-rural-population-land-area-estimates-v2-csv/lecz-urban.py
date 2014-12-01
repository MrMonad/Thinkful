import collections

population_dict = collections.defaultdict(int)


with open('lecz-urban-rural-population-land-area-estimates_continent-90m.csv', 'rU') as inputFile:
	header = next(inputFile) #loads header, therefore not printed
	print header

	for line in inputFile:
		line = line.rstrip().split(',') # split by delimiter , rstrip gets rid of spaces
		
		line[5] = int(line[5])
		if line[1] == 'Total National Population':
			#print line[0], line[5], type(line[5])
			population_dict[line[0]] += line[5]


print population_dict

#write header for output
with open('national_population.csv', 'w') as outputFile:
	outputFile.write('continent,2010_population\n')
	
	for i,j in population_dict.iteritems():
		outputFile.write(i + ',' + str(j) +'\n')


