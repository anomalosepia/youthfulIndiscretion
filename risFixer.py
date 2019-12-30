# this flips the authors from broken RIS exports.
import fileinput
import string
import os
import sys

aDirectory = sys.argv[1]
AUString = "AU  - " # this is the start of author string.
for subdir, dirs, files in os.walk(aDirectory):
	# print(subdir)
	# print(dirs)
	# this should work, this isn't for distribution, this is such a messs
	for thefile in files:
		if '.ris' in thefile:
			if 'export_' in thefile:
				theFullName = subdir + "/" +thefile
				theFile = open(theFullName, "r")
				# open some output file
				outFileName = aDirectory + 'namesFixed' + thefile[:-3] + '.ris'
				print(outFileName)
				outfile = open(outFileName,'w')
				print(thefile)
				for line in theFile:
					#print(line)
					if AUString in line:
						stripLine = line.strip()
						splitLine = line.split()
						print(splitLine)
						lastName = splitLine[-1]
						restOfName = splitLine[2:-1]
						print(lastName)
						print(restOfName)
						newName = AUString  + lastName + "," + " ".join(restOfName) + "\n"
						print(newName)
						outfile.write(newName)
					else:
						outfile.write(line)
				theFile.close()
