#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb
import sys
create_db = "CREATE DATABASE IF NOT EXISTS  petscl"
select_db = "use petscl"

create_pet = "CREATE TABLE pet ( pet_id INT(4) unsigned not null auto_increment,species_id INT(4) unsigned not null,breed_id INT(4) unsigned not null,owner_id INT(4) unsigned not null,nick varchar(30) not null,birth_date DATE, image varchar(50),PRIMARY KEY  (pet_id),FOREIGN KEY (species_id) REFERENCES species(species_id) ON UPDATE CASCADE ON DELETE RESTRICT,FOREIGN KEY (breed_id) REFERENCES breed(breed_id) ON UPDATE CASCADE ON DELETE RESTRICT,FOREIGN KEY (owner_id) REFERENCES owner(owner_id) ON UPDATE CASCADE ON DELETE RESTRICT) TYPE=InnoDb"

create_species = "CREATE TABLE species(species_id INT(4) unsigned not null auto_increment,species varchar(100) not null, PRIMARY KEY  (species_id)) TYPE=InnoDb"

create_breed = "CREATE TABLE breed(breed_id INT(4) unsigned not null auto_increment,species_id INT(4) unsigned not null, breed varchar(100) not null, PRIMARY KEY (breed_id), FOREIGN KEY (species_id) REFERENCES species(species_id) ON UPDATE CASCADE ON DELETE RESTRICT) TYPE=InnoDb"

create_owner = "CREATE TABLE owner(owner_id INT(4) unsigned not null auto_increment,name varchar(100) not null, surname varchar(100) not null, adress varchar(100) not null, email varchar(100) not null, phone varchar(20), home_phone varchar(20) , PRIMARY KEY  (owner_id)) TYPE=InnoDb"

create_visit = "CREATE TABLE visit ( visit_id INT(4) unsigned not null auto_increment, date TIMESTAMP(10),pet_id INT(4) unsigned not null, owner_id INT(4) unsigned not null, diagnose varchar(255) not null, manipulation varchar(255) not null, administration varchar(255) not null, PRIMARY KEY  (visit_id), FOREIGN KEY (pet_id) REFERENCES pet(pet_id) ON UPDATE CASCADE ON DELETE RESTRICT, FOREIGN KEY (owner_id) REFERENCES owner(owner_id) ON UPDATE CASCADE ON DELETE RESTRICT) TYPE=InnoDb"
query_list = [create_db,select_db,create_species,create_breed, create_owner,create_pet,create_visit]

def pp(cur):
    ver = cur.fetchone()
    print ver

def qury_db(lst):
    cur = con.cursor()
    for i in lst:
        cur.execute(i)
        pp(cur)
try:
    con = MySQLdb.connect(host = 'xxx.xxx.xxx.xxx', user = 'user', passwd = 'pass');
    qury_db(query_list)
    
except MySQLdb.Error, e:  
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
    
finally:
    if con:
        con.close()
