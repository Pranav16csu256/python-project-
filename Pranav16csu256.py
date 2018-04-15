#Pranav Garg
#16CSU256

from tkinter import *
win=Tk()
count=0
def addrec():                                 #function to add record
	f=open('abc.txt','a')
	name=s1.get()
	age=s2.get()
	f.writelines(name.ljust(20)+age.ljust(3))
	f.close()
def nextrec():
	f=open('abc.txt','r')                      #function for next record
	i=0
	while(i<=count):
		l=f.readline()
		i=i+1
	l1=l.split()
	s1=set(l1[0])
	s2=set(l1[1])
	count=count+1
	f.close()
s1=StringVar()
s2=StringVar()
v1=IntVar()
v2=IntVar()
v3=IntVar()
l1=Label(win,text="Name")
l2=Label(win,text="Age")                    #labels
l3=Label(win,text="Gender")
r1=Radiobutton(win, text = "Male", variable = v1, value = 1)
r2=Radiobutton(win, text = "Female", variable = v2, value = 2)      #radiobuttons
r3=Radiobutton(win, text = "Other", variable = v3, value = 3)
t1=Entry(win,textvariable=s1)
t2=Entry(win,textvariable=s2)                                      #text field
b1=Button(win,text="Next", command=nextrec)
b2=Button(win,text="Add", command=addrec)          #buttons
l1.grid(row=1,column=1)
l2.grid(row=2,column=1)		
t1.grid(row=1,column=2)
t2.grid(row=2,column=2)
b1.grid(row=6,column=1)             #grid function
b2.grid(row=6,column=2)
l3.grid(row=3,column=1)
r1.grid(row=4,column=1)
r2.grid(row=5 ,column=1)
class App:
  def __init__(self, win):
    fm = Frame(win, width=300, height=200, bg="blue")
    fm.grid(row=1,coulmn=5,coulmnspan=10,rowspan=5)     #background color   

display = App(win)
win.mainloop()
