import re, psycopg2
from lxml.html import parse
from lxml.cssselect import CSSSelector
 
def get_user_voites():
 
 user_start_num = 200
 user_end_num = 4722023
 
 try:
  conn=psycopg2.connect("dbname='postgres' user='postgres' password='120789' host='localhost'")
  cur = conn.cursor()
  page_num_sel = CSSSelector('div.pagesFromTo')
 
  for user_num in xrange(user_start_num, user_end_num):
 
   vote_film_list = []
   loop_bool = True
   page_num = 1
 
   while loop_bool:
    try:
     page = parse('http://www.kinopoisk.ru/user/%s/votes/list/ord/date/page/%s/' % (user_num, page_num))
 
     vote_count_div = int(page_num_sel(page)[0].text.split()[-1])
 
     items = page.xpath("//div[contains(@class, 'item')]")
     for item in items:
      try:
       film_div = item.find("div[@class='info']").find("div[@class='nameRus']").find("a")
 
       vote_num = int(item.find("div[@class='num']").text)
       film_id = re.search('film\/(\d)+\/$', film_div.values()[0]).group(0)[5:-1]
       film_name = film_div.text
       vote = item.find("div[@class='vote']").text
 
       if vote and film_id:
        vote_film_list.append({'vote': vote, 'user_id': user_num, 'film_id': film_id})
      except:
       pass
 
     if vote_num <= vote_count_div:
      page_num += 1
 
     print vote_num, page_num, vote_count_div, len(vote_film_list)
     cur.executemany("""INSERT INTO votes(user_id, film_id, vote) VALUES (%(user_id)s, %(film_id)s, %(vote)s)""", vote_film_list)
     conn.commit()
     vote_film_list = []
 
    except Exception, e:
     print e
     loop_bool = False
 
 
 except Exception, e:
  print "I am unable to connect to the database.", e
 
 finally:
  if conn:
   conn.close()