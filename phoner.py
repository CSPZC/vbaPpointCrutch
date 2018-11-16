#encoding: utf-8
import httplib
import scrapy
from scrapy.selector import Selector
from bs4 import BeautifulSoup
import time

def xpathgen(i):
	path = '/html/body/table['
	xpath = path + str(i) + ']'
	#print xpath
	#print '\n'
	return xpath

f =  open('C:\\Python27\\Projects\\gomunkul\\shit.txt', 'r')
#f1 = open('C:\\Python27\\Projects\\gomunkul\\!result.txt', 'w')
c = 0

for c in range(1):
	conn = httplib.HTTPConnection("192.168.1.2")
	a = str(f.readline())
	#a = "9114536803"
	#print a.encode('utf8').decode('866')
	b = "&z=1&z=2&z=3&z=4&z=5&z=6&z=7&z=8&z=9&z=10&z=11&z=12&z=13&z=14"#http://192.168.1.2/search?q=9114536803&z=1&z=2&z=3&z=4&z=5&z=6&z=7&z=8&z=9&z=10&z=11&z=12&z=13&z=14
	conn.request("GET", "/search?q=" + a + b)
	r1 = conn.getresponse()
	conn.close()
	data1 = r1.read()
	#str = str(Selector(text=data1).xpath('/html/body/table[2]').extract())
	#print str.encode('utf8').decode('866')
	#print data1
	print data1.decode('utf8').encode('cp866')
	
	#soup = BeautifulSoup(data1)
	#c = str(soup.get_text)
	#print c.decode('utf8').encode('cp866', 'ignore')
	#n = 100
	#for i in range(5, n, 2):
	#	a = Selector(text=body).xpath(xpathgen(i)).extract()
	#	b = ''.join(a)
	#	print b.decode('utf8', 'ignore')
		#f1.write(b)
		#f1.write('\n#######\n')
		
		
		
		
		
		
		

#print data1.decode('utf8').encode('cp866')
#soup = BeautifulSoup(data1)
#a = str(soup.get_text)
#print a.decode('utf8').encode('cp866', 'ignore')
#f = open("C:\Python27\Projects\gomunkul\shit.txt", 'w')
#f.write(data1)
#f.close()
#<font size="-1">
#...  ��� 14735�.00�.14735�.00�.<b style="color:#0;background-color:#ffff66">��������� ������ ���������</b>, 09.05.1987�.�., ��. ��, �.�. �. ������������������������  ...  �����������, 10.07.1962�.�. <b style="color:#0;background-color:#ffff66">��������� ������ ���������</b>, 09.05.1987�.�.���������: �.�����������, ��. �������, �  ...<br>
#<font class="filesizecolor">
#��� ��������� : C:\BACKUP\BASES\�������&amp;�������\ - <a href="/get?i=1943079721&amp;q=1796347065">C:\BACKUP\BASES\�������&amp;�������\������������\�������(��)2004.xlsm|xl\sharedStrings.xml</a> - 116&nbsp;469&nbsp;178 - 01.01.1980 0:00:00 - <a href="/get?i=1943079721&amp;q=1796347065">�����������</a> - <a href="/download/1943079721/sharedStrings.xml">�������</a>
#</font>
#</font>
#/html/body/table[5]/tbody/tr/td/font
#/html/body/table[5]/tbody/tr/td/font
#body > table:nth-child(6) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > font:nth-child(1)#
#body > table:nth-child(6) > tbody > tr > td > font"""
#/html/body/table[23]/tbody/tr/td/font