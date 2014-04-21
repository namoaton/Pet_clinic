#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb
import sys
import urllib2
from BeautifulSoup import BeautifulSoup

link_list=["http://poisk-druga.ru/breeds/"]
for i in range(27):
    if i>=2:
        link_list.append("http://poisk-druga.ru/breeds/page/"+str(i)+"/")

breed_list={u"Без породы":'1'}
for url in link_list:
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    hit = soup.findAll('div', attrs = { 'class' : 'short-breeds' })
    for z in hit:
        x= {z.text:"1"}
        breed_list.update(x)
for key in breed_list:
    print " (%s, %s);"%(key,breed_list[key])

def add_breed(breed_list):
    con = MySQLdb.connect(host = '192.168.1.100', user = 'admin', passwd = 'root', db ="petscl", use_unicode=True);
    #con.names="utf8"
    con.set_character_set('utf8')
    cur = con.cursor()
    cur.execute('SET NAMES utf8;')
    cur.execute('SET CHARACTER SET utf8;')
    cur.execute('SET character_set_connection=utf8;')
    for key in breed_list:
        query_db =u"INSERT INTO breed (species_id, breed) values ('%s','%s')"%(breed_list[key],key)
        print query_db
        cur.execute(query_db)
    cur.close()
    con.commit()
    con.close()
try:
    add_breed(breed_list)
except MySQLdb.Error, e:  
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
    
