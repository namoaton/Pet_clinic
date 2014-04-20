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
        #self.buttons.add(u"История посещений", command = self.history)
        
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
        self.counter += 1
        t = Toplevel(self)
        t.wm_title("Window #%s" % self.counter)
        l = Label(t, text="This is window #%s" % self.counter, font = "Ubuntu 15")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)
    def editCard(self):
        self.counter += 1
        t = Toplevel(self)
        t.wm_title("Window #%s" % self.counter)
        l = Label(t, text="This is window #%s" % self.counter, font = "Ubuntu 15")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)
def main():
    Petclinic().mainloop()
if __name__ == "__main__":
    main()
