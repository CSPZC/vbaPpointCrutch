#encoding: utf-8
import httplib
import scrapy
from scrapy.selector import Selector
from bs4 import BeautifulSoup

def xpathgen(i):
	path = '/html/body/table['
	xpath = path + str(i) + ']'
	#print xpath
	print '\n'
	return xpath

conn = httplib.HTTPConnection("192.168.1.2")
conn.request("GET", "/search?q=%22%D0%9F%D0%BE%D1%80%D0%BE%D1%88%D0%B5%D0%BD%D0%BA%D0%BE+%D0%9D%D0%B8%D0%BA%D0%B8%D1%82%D0%B0+%D0%A1%D0%B5%D1%80%D0%B3%D0%B5%D0%B5%D0%B2%D0%B8%D1%87%22&z=0")
r1 = conn.getresponse()
data1 = r1.read()
print data1.decode('utf8').encode('cp866')
#print type(data1)


#body = data1
#n = 25
#for i in range(5, n, 2):
#	a = Selector(text=body).xpath(xpathgen(i)).extract()
#	b = ''.join(a)
#	print b
#
#a = Selector(text=body).xpath('/html/body/table[13]').extract()
#print data1.decode('utf8').encode('cp866')
#soup = BeautifulSoup(data1)
#a = str(soup.get_text)
#print a.decode('utf8').encode('cp866', 'ignore')
#f = open("C:\Python27\Projects\gomunkul\shit.txt", 'w')
#f.write(data1)
#f.close()
#<font size="-1">
#...  АПП 14735р.00к.14735р.00к.<b style="color:#0;background-color:#ffff66">ПОРОШЕНКО НИКИТА СЕРГЕЕВИЧ</b>, 09.05.1987Г.Р., ГР. РФ, М.Р. Г. КАЛИНИНГРАДСВИДЕТЕЛЬСТВО  ...  ВИКЕНТЬЕВНА, 10.07.1962Г.Р. <b style="color:#0;background-color:#ffff66">ПОРОШЕНКО НИКИТА СЕРГЕЕВИЧ</b>, 09.05.1987Г.Р.ПРОЖИВАЕТ: Г.КАЛИНИНГРАД, УЛ. ГРЕКОВА, Д  ...<br>
#<font class="filesizecolor">
#Мой компьютер : C:\BACKUP\BASES\Недвига&amp;Стройка\ - <a href="/get?i=1943079721&amp;q=1796347065">C:\BACKUP\BASES\Недвига&amp;Стройка\Недвижимость\Юстиция(КО)2004.xlsm|xl\sharedStrings.xml</a> - 116&nbsp;469&nbsp;178 - 01.01.1980 0:00:00 - <a href="/get?i=1943079721&amp;q=1796347065">Просмотреть</a> - <a href="/download/1943079721/sharedStrings.xml">Скачать</a>
#</font>
#</font>
#/html/body/table[5]/tbody/tr/td/font
#/html/body/table[5]/tbody/tr/td/font
#body > table:nth-child(6) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > font:nth-child(1)#
#body > table:nth-child(6) > tbody > tr > td > font"""
#/html/body/table[23]/tbody/tr/td/font