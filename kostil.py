import os
import re
import sys

def check(d):
	f = open('C:\\Python27\\Projects\\gomunkul\\codes.txt', 'r')
	d = int(d)
	num = 0
	for num in range(38):
		a = f.readline()
		b = int(a[:10])
		c = int(a[11:])
		if (d >= b and d <= c):
			return True
		else:
			num+=1

def phoneSearch(fileName, outputDir, inputDir):

	outputFileName = outputDir + '\\'+ fileName
	inputFileName = inputDir + '\\'+ fileName

	#print inputFileName
	f =  open(outputFileName, 'r')
	f1 = open(inputFileName, 'w')
	lines = f.readlines()
	i = 0 # phone counter

	msg = 'Checking ' + outputFileName
	print msg

	for line in lines:
		try:
			reg_phone = re.compile(r'[9]\d{9}')#numeric sequence of int '9' & 9 integers
			a = reg_phone.search(line).group(0)
			a = str(a)
			if check(a):
				a = a + '    ' + line
				#print a
				f1.write(a)
				i += 1
			else:
				pass
		except AttributeError:
			pass
	#print i
	f.close()
	f1.close()

def resulter(fileName, outputDir, inputDir):

	outputFileName = outputDir + '\\'+ fileName
	inputFileName = inputDir + '\\'+ '!result.txt'

	#print outputFileName
	#print inputFileName
	f =  open(outputFileName, 'r')
	f1 =  open(inputFileName, 'a')
	lines = f.readlines()
	for line in lines:
		a = line
		a = str(a)
		#print a
		f1.write(a)
	f.close()

def main():
	
	if len(sys.argv)==3:
		print('no params. Need 3 params, input folder. output folder and mask')
		sys.exit(1)
	
	i = 0
	outputDir = sys.argv[1]		#from?  outbut blyat
	inputDir = sys.argv[2]		#where ? write to file      #txt? 
	mask = sys.argv[3]
	inputFileName = inputDir + '\\'+ 'result.txt'
	files = os.listdir(outputDir); 
	res = filter(lambda x: x.endswith(mask), files);
	fileNameArray = []
	#print type(res)
	#print type(fileNameArray)
	#print len(res)
	#print i
	for i in range(len(res)):
		#print res[i]
		#fileNameArray.append(inputDir + '\\' + res[i])
		#print fileNameArray[i]
		phoneSearch(res[i], outputDir, inputDir)
		resulter(res[i], inputDir, inputDir)
		
if __name__ == '__main__':
	main()