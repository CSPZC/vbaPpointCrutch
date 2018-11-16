# -*- coding: utf-8 -*-
from splinter import Browser
browser = Browser()
browser.visit('http://fssprus.ru/iss/ip/')
field = browser.find_by_xpath('//*[@id="ip_form"]/div/div[2]/input')
field.fill('Порошенко')

#browser.find_by_xpath('//*[@id="ip_form"]/div/div[1]/select')
#browser.find_by_xpath('//*[@id="ip_form"]/div/div[2]/input')
#browser.find_by_xpath('//*[@id="ip_form"]/div/div[3]/input')
#browser.find_by_xpath('//*[@id="ip_form"]/div/div[4]/input')

   
#//*[@id="sub_fiz"]
"""
   1 - gorod
   2 - surname
   3 - name
   4 - fathership
   """
   