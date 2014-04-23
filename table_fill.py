#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb
import sys
from Tkinter import *
from tkMessageBox import *
import Pmw


class Petclinic (Frame):
    counter = 0
    def __init__(self):
        Frame.__init__(self)
        Pmw.initialise()
        self.pack (expand = YES, fill = BOTH)
        self.master.title(u'Ветеринарная клиника КОТ-ПЕС')
        
        #button for command
        self.buttons = Pmw.ButtonBox( self, padx = 0)
        self.buttons.grid(columnspan = 2)
        self.buttons.add(u"Прием пациента", command = self.visit, font = "Ubuntu 15")
        self.buttons.add(u"Очистить", command = self.clearContents , font = "Ubuntu 15")
        self.buttons.add(u"Поиск карточки", command = self.findCard, font = "Ubuntu 15")
        self.buttons.add(u"Заполнение карточки", command = self.editCard, font = "Ubuntu 15")
        self.buttons.add(u"Породы собак", command = self.show_breeds,font = "Ubuntu 15")
        self.buttons.add(u"quit", command = quit)
        #list of visit entry
        #fields = [u'Id',u'Кличка',u'Хозяин',u'Жалобы',u'Манипуляции',u'Назначения']
        fields = [u'Id', u'\u041a\u043b\u0438\u0447\u043a\u0430', u'\u0425\u043e\u0437\u044f\u0438\u043d', u'\u0416\u0430\u043b\u043e\u0431\u044b', u'\u041c\u0430\u043d\u0438\u043f\u0443\u043b\u044f\u0446\u0438\u0438', u'\u041d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f']

        self.entries = {}
        self.IDEntry = StringVar()
        self.IDEntry.set("")

         #create entries
        for i in range(len(fields)): 
            label = Label(self, text = fields[i], font = "Ubuntu 10")
            label.grid (row =i+1, column = 0)
            entry = Entry(self, name = fields[i].lower(), font = "Ubuntu 20")
            entry.grid(row = i+1, column = 1, sticky = W+E+N+S, padx =5)
            #service field 
            if fields[i] == u'Id':
                entry.config(state =DISABLED, textvariable = self.IDEntry, bg = 'gray')
                entry.insert(2,"0nbn")
                
            #add entry field to dict
            key = fields [i].replace(" ","_")
            #key = key.upper()
            self.entries [key] = entry

            
#[u'Id', u'\u041a\u043b\u0438\u0447\u043a\u0430', u'\u0425\u043e\u0437\u044f\u0438\u043d', u'\u0416\u0430\u043b\u043e\u0431\u044b', u'\u041c\u0430\u043d\u0438\u043f\u0443\u043b\u044f\u0446\u0438\u0438', u'\u041d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f']
    
#add visit data to Base
    def visit(self):
        if self.entries [u'\u041a\u043b\u0438\u0447\u043a\u0430'].get()!="" and self.entries [u'Жалобы'].get()!="" and self.entries [u'Манипуляции'].get()!="" and self.entries [u'Назначения'].get()!="":
            query = "INSERT INTO visit (pet_id, owner_id, diagnose, manipulation, administration) VALUES(" +str(self.entries[u'Id'].get(),self.entries[u'Хозяин'].get(),self.entries[u'Жалобы'].get(),self.entries[u'Манипуляции'].get(),self.entries[u'Назначения'].get())
            query  = query[:-2]+")"
            try :
                print query
                con = MySQLdb.connect(host = 'xxx.xxx.xxx.xxx', user = 'user', passwd = 'pass', db= "petscl");
                cursor =con.cursor()
                cursor.execute(query_list)
            except MySQLdb.OperationalError, mesage:
                errorMessage = "Error %d:\n%s" %(message[0],mesage[1])
                showerror ("Error", errorMessage)
            else:
                cursor.close()
                con.close()
                self.clearContents()
        else:
            showwarning (u"Заполните поля", u"Заполните все поля")
    
    
    def clearContents(self):
        for entry in self.entries.values():
            entry.delete(0,END)
        self.IDEntry.set(u'')

    def findCard(self):
        search_entry={}
        t = Toplevel(self, bd=10)
        t.wm_title(u'Поиск')
        
		#create entries for searchimg
        search_list = [u'Кличка',u'Фамилия хозяина']
        for i in range(len(search_list)): 
            label = Label(t, text = search_list[i], font = "Ubuntu 10")
            label.grid (row =i+1, column = 0)
            entry = Entry(t, name = search_list[i].lower(), font = "Ubuntu 20")
            entry.grid(row = i+1, column = 1, sticky = W+E+N+S, padx =5)
            key = search_list[i]
            search_entry [key] = entry
            print search_entry
        t.buttons = Pmw.ButtonBox( t, padx = 0)
        t.buttons.grid(columnspan = 2)
        t.buttons.add(u"Очистить", command = self.clearContents() , font = "Ubuntu 15")
        t.buttons.add(u"Поиск карточки", command = self.findCard, font = "Ubuntu 15")
        t.buttons.add(u"Закрыть", command = t.destroy, font = "Ubuntu 15")
    
    
    
    def show_breeds(self):
        ss = Toplevel(self)
        ss.wm_title(u'Породы собак')
        con = MySQLdb.connect(host = '192.168.1.100', user = 'admin', passwd = 'root', db ="petscl", use_unicode=True);
        con.set_character_set('utf8')
        cur = con.cursor()
        cur.execute('SET NAMES utf8;')
        cur.execute('SET CHARACTER SET utf8;')
        cur.execute('SET character_set_connection=utf8;')
        query_db ="SELECT * FROM breed ORDER BY breed ASC;"
        cur = con.cursor()
        cur.execute(query_db)
        allRec = cur.fetchall()
        cur.close()
        con.close()
        #print allRec
        q=0
        label = Label(ss, text = u'Вид', font = "Ubuntu 20", justify="left")
        scrollbar = Scrollbar(ss)
        scrollbar.pack( side = RIGHT, fill=Y ) 
        list_db =Listbox(ss, yscrollcommand = scrollbar.set,font = "Ubuntu 15", width ="40")
        for i in allRec:
			q=q+1
			#a ="ID :  "+str(i[])+"  Species  :" + i[1]+"\n"
			a ="  Species  :" + str(i[1])+"\n"
			#label = Label(ss, text = a, font = "Ubuntu 20", justify=LEFT)
			#label.grid (row =q+1, column = 1)
			
			list_db.insert(q, unicode(i[2]))
        list_db.pack(expand=1,fill=BOTH)
        
        
    def editCard(self):
        search_entry={}
        tt = Toplevel(self, bd=10)
        tt.wm_title(u'Владелец')
        
		#create entries for searchimg
        search_list = [u'Имя',u'Фамилия',u'Адрес',u'Email',u'Телефон',u'Доп телефон']
        for i in range(len(search_list)): 
            label = Label(tt, text = search_list[i], font = "Ubuntu 10")
            label.grid (row =i+1, column = 0)
            entry = Entry(tt, name = search_list[i].lower(), font = "Ubuntu 20")
            entry.grid(row = i+1, column = 1, sticky = W+E+N+S, padx =5)
            key = search_list[i]
            search_entry [key] = entry
            print search_entry
        tt.buttons = Pmw.ButtonBox( tt, padx = 0)
        tt.buttons.grid(columnspan = 2)
        tt.buttons.add(u"Очистить", command = self.clearContents() , font = "Ubuntu 15")
        tt.buttons.add(u"Записать", command = self.findCard, font = "Ubuntu 15")
        tt.buttons.add(u"Закрыть", command = tt.destroy, font = "Ubuntu 15")
        
        
     
def main():
    Petclinic().mainloop()
if __name__ == "__main__":
    main()
