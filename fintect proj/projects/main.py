
import warnings
warnings.filterwarnings('ignore')


from datetime import date as date
import wx
import os
import sqlite3 as lite
import random 
import wx.grid as gridlib
import pandas as pd
import time
import threading

from crawl import *



class MyFrame(wx.Frame):
    # path_adj = os.getcwd()
    # stock_list = pd.read_excel(f'{path_adj}/adjustments/list.xls')
    # stock_list = stock_list.iloc[:,:1]
    # stock_list['code'] = stock_list.iloc[:,0].str.split('　').str[0]
    # all = stock_list.code
    weblist = ["ALL",'listed','otc']
    
    def __init__(self):
        
        super().__init__(None, title = "Crawling Interface", size = (1220, 800))
#         self.Centre()
        self.root = os.getcwd()
        panel = wx.Panel(self)
        
        # directories building
        self.multi_path_build()
        
        # layout
        # horizontal 1
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        text1 = wx.StaticText(panel, label = "Target Web Crawling: ", size = (130, -1))
        self.combo1 = wx.ComboBox(panel, -1, choices = self.weblist, value = "ALL", style = wx.CB_READONLY)
        # self.Bind(wx.EVT_COMBOBOX, lambda event: self.page_hint(event), self.combo1)
        hbox1.Add(text1, 0, flag = wx.ALL, border = 10)
        hbox1.Add(self.combo1, 0, flag = wx.ALL, border = 10)
        
        text2 = wx.StaticText(panel, label = "Storing Path: ")
        hbox1.Add(text2, 0, flag = wx.ALL, border = 10)
        self.input1 = wx.TextCtrl(panel, style = wx.TE_READONLY, size = (500, -1))
        self.input1.SetValue(os.getcwd() + f"\databases")
        hbox1.Add(self.input1, 0, flag = wx.ALL | wx.EXPAND, border = 10)
        
        button0 = wx.Button(panel, -1, label = "Change Path")
        self.Bind(wx.EVT_BUTTON, lambda event: self.storing_path(event), button0)
        hbox1.Add(button0, 0, flag = wx.ALL, border = 10)
        
        # horizontal 2
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        text3 = wx.StaticText(panel, label = "Storing Database: ", size = (130, -1))
        self.input5 = wx.TextCtrl(panel, style = wx.TE_READONLY, size = (500, -1))
        self.input5.SetValue(os.getcwd() + f"\databases\All_stock_data.db")
        hbox3.Add(text3, 0, flag = wx.ALL, border = 10)
        hbox3.Add(self.input5, 0, flag = wx.ALL | wx.EXPAND, border = 10)
            

        hbox4 = wx.BoxSizer(wx.VERTICAL)
        hbox4.Add(150, 0, wx.EXPAND)
        submit_button = wx.Button(panel, -1, label = "Submit")
        hbox4.Add(submit_button, 0, flag = wx.ALL , border = 20)
        self.Bind(wx.EVT_BUTTON, lambda event: self.submittion(event), submit_button)


        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        text6 = wx.StaticText(panel, label = "Stock: ", size = (130, -1))
        self.input6 = wx.TextCtrl(panel, size = (500, -1))
        self.input6.SetValue("stock number")
        hbox5.Add(text6, 0, flag = wx.ALL, border = 10)
        hbox5.Add(self.input6, 0, flag = wx.ALL | wx.EXPAND, border = 10)

        long_tail_stk = {}
        
        # self.create_listbox(self)
        # self.Bind(wx.EVT_LISTBOX, self.onListBox, self.listbox)


        hboxm = wx.BoxSizer(wx.HORIZONTAL)
        hboxm.Add((0, 30))

        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.Add(hbox1,  0, flag = wx.ALL | wx.EXPAND)
        self.vbox.Add(hbox2,  0, flag = wx.ALL | wx.EXPAND)
        self.vbox.Add(hbox3,  0, flag = wx.ALL | wx.EXPAND)
        self.vbox.Add(hbox4,  0, flag = wx.ALL | wx.EXPAND)
        self.vbox.Add(hbox5,  0, flag = wx.ALL | wx.EXPAND)

        panel.SetSizer(self.vbox)

    def submittion(self, event):
        print("Starting crawling.")
        thread = Crawl(self, event)       

    def storing_path(self, event):
        path = os.getcwd()
        with wx.DirDialog(self, "Open database as source", f"{path}\databases",
                           style = wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST) as dirDialog:
            if dirDialog.ShowModal() == wx.ID_CANCEL:
                return
            self.input1.SetValue(dirDialog.GetPath())
            
    def browsing(self, event):
        path = os.getcwd()

        with wx.FileDialog(self, "Open DB", f"{path}\databases", wildcard="*.db",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            self.source_path = fileDialog.GetPath()
            print(self.source_path)
            name = self.source_path.split("\\")[-1]
            self.input2.SetValue(name)

    def db_counting(self):
        files = os.listdir(self.input1.GetValue())
        self.db_list = [file for file in files if file.endswith(".db") and file != str(date.today()) + "_crawled.db"]
        self.db_list.append(str(date.today()) + "_crawled.db")
        self.db_list = sorted(self.db_list, reverse = True)


    def multi_path_build(self):
        path = os.getcwd()
        try:
            os.mkdir(path + "\\adjustments")
        except:
            pass
        try:
            os.mkdir(path + "\databases")
        except:
            pass

        
        parent_dir = path + "\databases"
        target_dir = str(date.today())
        self.path = os.path.join(parent_dir, target_dir)
        try:
            os.mkdir(self.path)
        except:
            pass
        parent_dir = path + "\models"
        target_dir = str(date.today())
        self.path = os.path.join(parent_dir, target_dir)
        try:
            os.mkdir(self.path)
        except:
            pass
        parent_dir = path + "\htmls"
        target_dir = str(date.today())
        self.path = os.path.join(parent_dir, target_dir)
        try:
            os.mkdir(self.path)
        except:
            pass
    
    def onListBox(self, event): 
        self.text_lt.AppendText( "longtail: "+ 
            event.GetEventObject().GetStringSelection() + "\n")

    def get_stock_list(self,event):
        stock_list = pd.read_excel(os.getcwd()+'/adjustments/list.xls')
        stock_list = stock_list.iloc[:,:1]
        stock_list['code'] = stock_list.iloc[:,0].str.split('　').str[0]
        return stock_list['code']
    def create_listbox(self,event):

        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        stock_list=[]
        stock_list = self.get_stock_list(self)
        self.text_lt = wx.TextCtrl(self.panel, style = wx.TE_MULTILINE)
        self.listbox = wx.ListBox(self.panel, size=(300,-1), choices = stock_list, style = wx.LB_SINGLE)
        hbox6.Add(self.listbox, 0, wx.EXPAND)
        hbox6.Add(self.text_lt, 1, wx.EXPAND)
        self.vbox.Add(hbox6,  0, flag = wx.ALL | wx.EXPAND)

class Crawl(threading.Thread):
    
    def __init__(self, frame, event):
        threading.Thread.__init__(self)
        self.frame = frame
        self.event = event
        self.start()
    
    def run(self):
        select_type = self.frame.combo1.GetValue()
        if select_type =='ALL':
            crawl_all_ch(self)
            print("BOTH")
            crawl_all_otc(self)
        elif select_type =="listed":
            print("LISTED")

            crawl_all_ch(self)
        elif select_type =='otc':
            print("otc")
            crawl_all_otc(self)


class App(wx.App):
    
    # the constructor of App
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True
    def OnExit(self):
        print("Exit the program.")
        return 0

# main
if __name__ == "__main__":
    app = App()
    app.MainLoop()

