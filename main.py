#!/usr/bin/env python3
from tkinter import *
import requests

class Repeater:
    def __init__(self, root):
        self.root = root
        self.cookies = {}

    def start(self):
        self.MainFrame = Frame(self.root)
        self.MainFrame.pack()
        WelcomeLabel = Label(self.MainFrame, text="Repeater-Automater", font=("Arial", 20))
        WelcomeLabel.grid(row=1, column=1, columnspan=4)
        self.inputFrame()

    def inputFrame(self):
        self.inputFr = Frame(self.MainFrame)
        self.inputFr.grid(column=1,columnspan=4)
        self.no_of_key_label = Label(self.inputFr,text="Enter No Of Cookie Key's Needed")
        self.no_of_key_label.grid(row=2,column=1)
        self.no_of_key_value = Entry(self.inputFr)
        self.no_of_key_value.grid(row=2,column=2)
        self.no_of_key_value.insert(END,"0")
        self.generate_button = Button(self.inputFr, text="Generate",command=self.addCookieParam)
        self.generate_button.grid(row=2,column=3,sticky="W")

    def addCookieParam(self):
        self.row = 3
        self.cnt = 1
        self.num = int(self.no_of_key_value.get())
        self.inputFr.destroy()
        self.inputFrame()
        self.cookieGenerator()

    def cookieGenerator(self):
        if (self.cnt <= self.num):
            self.cookie_key_label = Label(self.inputFr, text="Cookie_Key")
            self.cookie_key_label.grid(row=self.row, column=1)
            self.cookie_key_entry = Entry(self.inputFr)
            self.cookie_key_entry.grid(row=self.row, column=2)
            self.cookie_value_label = Label(self.inputFr, text="Cookie_Value")
            self.cookie_value_label.grid(row=self.row + 1, column=1)
            self.cookie_value_entry = Entry(self.inputFr)
            self.cookie_value_entry.grid(row=self.row + 1, column=2)
            self.generate_next_button = Button(self.inputFr, text="Next", command=self.destroyIncrement)
            self.generate_next_button.grid(row=self.row + 1, column=3, sticky="W")
        else:
            self.generateUrlParam()

    def destroyIncrement(self):
        self.cnt += 1
        self.cookies[self.cookie_key_entry.get()] = self.cookie_value_entry.get()
        self.cookie_value_label.destroy()
        self.cookie_key_entry.destroy()
        self.cookie_value_entry.destroy()
        self.cookie_key_label.destroy()
        self.generate_next_button.destroy()
        self.cookieGenerator()

    def generateUrlParam(self):
        self.url_label = Label(self.inputFr, text="Url")
        self.url_label.grid(row=self.row, column=1)
        self.url_entry = Entry(self.inputFr)
        self.url_entry.grid(row=self.row, column=2)
        self.url_entry.insert(END,"https://")
        self.row += 1
        self.generateAttackTimesParam()

    def generateAttackTimesParam(self):
        self.no_of_times_to_repeat_label = Label(self.inputFr, text="Enter No Of Times To Repeat")
        self.no_of_times_to_repeat_label.grid(row=self.row, column=1)
        self.no_of_times_to_repeat_value = Entry(self.inputFr)
        self.no_of_times_to_repeat_value.grid(row=self.row, column=2)
        self.no_of_times_to_repeat_value.insert(END,"1")
        self.get_button = Button(self.inputFr, text="GET", command=self.getResponse)
        self.get_button.grid(row=self.row,column=3,sticky="W")
        self.post_button = Button(self.inputFr, text="POST", command=self.postResponse)
        self.post_button.grid(row=self.row,column=4, sticky="W")
        self.row += 1

    def getResponse(self):
        self.url = self.url_entry.get()
        self.times = int(self.no_of_times_to_repeat_value.get())
        self.cnt = 1

        try:
            self.PTextFrame.destroy()
        except:
            pass

        self.PTextFrame = Frame(self.inputFr)
        self.PScroll = Scrollbar(self.PTextFrame)
        self.PScroll.pack(side=RIGHT, fill=Y)
        self.PTextBox = Text(self.PTextFrame, height=10, width=50, yscrollcommand=self.PScroll.set)
        self.PTextBox.pack()
        self.PScroll.config(command=self.PTextBox.yview)
        self.PTextFrame.grid(column=1, columnspan=2)

        while(self.cnt <= self.times):
            self.res = requests.get(self.url,cookies=self.cookies)
            self.PTextBox.insert('1.0',(str(self.res)+'\n'))
            self.cnt += 1

    def postResponse(self):
        self.url = self.url_entry.get()
        self.times = int(self.no_of_times_to_repeat_value.get())
        self.cnt = 1

        try:
            self.PTextFrame.destroy()
        except:
            pass

        self.PTextFrame = Frame(self.inputFr)
        self.PScroll = Scrollbar(self.PTextFrame)
        self.PScroll.pack(side=RIGHT, fill=Y)
        self.PTextBox = Text(self.PTextFrame, height=10, width=50, yscrollcommand=self.PScroll.set)
        self.PTextBox.pack()
        self.PScroll.config(command=self.PTextBox.yview)
        self.PTextFrame.grid(column=1, columnspan=2)

        while (self.cnt <= self.times):
            self.res = requests.post(self.url,cookies=self.cookies)
            self.PTextBox.insert('1.0', (str(self.res) + '\n'))
            self.cnt += 1

root = Tk()
root.title("Repeater-Automater")
root.geometry("1100x500")
root.resizable(0,0)
gui = Repeater(root)
gui.start()
root.mainloop()
