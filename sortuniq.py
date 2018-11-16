#encoding: utf-8

f = open('C:\\Python27\\Projects\\gomunkul\\!resall.txt', 'r')
f1 = open('C:\\Python27\\Projects\\gomunkul\\!resalluniq.txt', 'w')
lines = f.readlines()
for line in  lines:
    a = line[14:]
    i = 0
    for i in range(len(a)):
            if a[i] == ';':
                    phone = line[:10]
                    login = a[:i]
                    password = a[(i+1):]
                    str = phone +' ' + login + ':' + password + '\n'
                    f1.write(str)
            if a[i] == ':':
                    phone = line[:10]
                    login = a[:i]
                    password = a[(i+1):]
                    str = phone +' ' + login + ':' + password
                    f1.write(str)
					
f.close()
f1.close()
print '\nEverything is ok'