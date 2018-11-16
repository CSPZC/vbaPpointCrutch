import re

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

f =  open('C:\\Python27\\Projects\\gomunkul\\Leaks\\YandexPochta.txt', 'r')
lines = f.readlines()
i = 0 # phone counter
f1 = open('C:\\Python27\\Projects\\gomunkul\\!res\\YandexPochta.txt', 'w')
for line in lines:
	try:
		reg_phone = re.compile(r'[9]\d{9}')#numeric sequence of int '9' & 9 integers
		a = reg_phone.search(line).group(0)
		a = str(a)
		if check(a):
			a = a + '    ' + line
			print a
			f1.write(a)
			i += 1
		else:
			pass
	except AttributeError:
		pass
print i