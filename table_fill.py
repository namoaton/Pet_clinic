#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb
import sys
from Tkinter import *
from tkMessageBox import *
import Pmw


class Petclinic (Frame):
    def __init__(self):
        Frame.__init__(self)
        Pmw.initialise()
        self.pack (expand = YES, fill = BOTH)
        self.master.title(u'Ветеринарная клиника КОТ-ПЕС')
        
        #button for command
        self.buttons = Pmw.ButtonBox(self.padx = 0)
        self.buttons.grid(columnspan = 2)
        self.buttons.add(u"Прием пациента", command = self.visit)
        self.buttons.add(u"Поиск карточки", command = self.findCard)
        self.buttons.add(u"Заполнение карточки", command = self.editCard)
        self.buttons.add(u"История посещений", command = self.history)
        
        #list of visit entry
        fields = [u'Id',u'Кличка',u'Хозяин',u'Жалобы',u'Манипуляции',u'Назначения']
        
        self.entries = {}
        self.IDEntry = StringVar()
        self.IDEntry.set("")
        
        #create entries
        for i in range (len (fields)):
            label = Label (self, text = fields[i])+"i")
            label.grid (row =i+1, column = 0)
            entry = Entry (self, name = fields[i].lower(), font = "Courier 12")
            entry.grid (row = i+1, column = 1, sticky = W+E+N+S, padx =5)
            #service field 
            if fields[i] == u'Id'
                entry.config(state =DISABLED, textvariable = self.IDEntry, bg = 'gray')
            
