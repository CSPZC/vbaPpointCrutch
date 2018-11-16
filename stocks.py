#!/usr/bin/python
# -*- coding: utf-8 -*-

# Version 2

import webbrowser

#получаем данные
while True:
	keyword  = raw_input(">>>")
	if keyword == '':
		continue
	elif keyword == ' ':
		continue
	else: 
		shutterstock =  'https://www.shutterstock.com/search?searchterm=' + keyword + '&search_source=base_search_form&language=ru&page=1&sort=popular&image_type=photo&measurement=px&safe=true'

		stocksy = 'https://www.stocksy.com/search/' + keyword + '?text=' + keyword + '&sort=curated&page=1'

		stock_adobe = 'https://stock.adobe.com/uk/search?load_type=search&native_visual_search=&similar_content_id=&is_recent_search=&k=' + keyword

		istockphoto = 'https://www.istockphoto.com/gb/en/%D1%84%D0%BE%D1%82%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D0%B8/pine?phrase=' + keyword + '&excludenudity=true&sort=best'

		stockphoto = 'https://stockphoto.com/search.php?q=' + keyword
		
		alamy = 'https://www.alamy.com/search.html?CreativeOn=1&adv=1&ag=0&all=1&creative=&et=0x000000000000000000000&vp=0&loc=0&qt='+ keyword +'&qn=&lic=6&lic=1&imgt=0&archive=1&dtfr=&dtto=&hc=&selectdate=&size=0xFF&aqt=&epqt=&oqt=&nqt=&gtype=0'

		#dreamstime = 'https://www.dreamstime.com/search.php?securitycheck=fefe5a84ce0d01293d252dddf3fad3d0&firstvalue=&lastsearchvalue=&srh_field='+ keyword +'&s_all=y&s_ph=y&s_il=y&s_video=y&s_audio=y'
		
		list = [stocksy, shutterstock, stock_adobe, alamy]
		
		for item in list:
			webbrowser.open_new_tab(item)