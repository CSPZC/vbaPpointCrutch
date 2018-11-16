f = open('C:\Python27\Projects\gomunkul\!resalluniq.txt', 'r')
f1 = open('C:\Python27\Projects\gomunkul\!resteluniq.txt', 'w')
arr = f.readlines()
arr1 = arr
i = 0

for i in range(len(arr)):
	a = arr[i]
	res = a
	c = i+1
	#msg = 'Comparing this number: & ' + a[:10] + ' with list:\n'
	b = arr[i]
	if a[:10] == b[:10]:
		res = list(res)
		res.pop()
		res = ''.join(res)
		res = res + ',' + b[10:]
	f1.write(res)
f1.close()