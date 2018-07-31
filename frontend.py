from tkinter import *
from tkinter import messagebox
from backend import *
from matplotlib.ft2font import BOLD


def logistic():
    if logisReg(E2.get(),E3.get(),E4.get(),E5.get(),E6.get())>0.5:
        L11['text']='Hired'
    else:
        L11['text']='Not Hired'

def decision():
    if deciReg(E2.get(),E3.get(),E4.get(),E5.get(),E6.get())>0.5:
        L12['text']='Hired'
    else:
        L12['text']='Not Hired'
    

def randomfor():
    if randfor(E2.get(),E3.get(),E4.get(),E5.get(),E6.get())>0.5:
        L13['text']='Hired'
    else:
        L13['text']='Not Hired'
        

def svm():
    if svmReg(E2.get(),E3.get(),E4.get(),E5.get(),E6.get())>0.5:
        L14['text']='Hired'
    else:
        L14['text']='Not Hired'

        
def final():
    n=0
    l=[L11['text'],L12['text'],L13['text'],L14['text']]
    for i in l:
        if i=='Hired':
            n+=1
        else:
            n-=1
    if E1.get()=='' or (E2.get()==0 and E5.get()==0 or E6.get()==0):
        messagebox.showinfo('error!')
        return
    if n>=0:
        L15['text'] = ['Hired']
        finalM(E1.get(),E2.get(),E3.get(),E4.get(),E5.get(),E6.get(),1)
    else:
        L15['text'] = ['Not Hired']
        finalM(E1.get(),E2.get(),E3.get(),E4.get(),E5.get(),E6.get(),0)
    
    

root=Tk()
root.config(background='#7cfc00')
root.geometry('800x700')
topFrame = Frame(root,bg='#2f4f4f')

Label(topFrame,text='Recruitment',bg="#2f4f4f",fg='White',borderwidth='0',relief='ridge',font=('Times',30)).grid(row=0,column=1,columnspan=5,pady=10,ipadx=60)
topFrame.pack()

middleFrame=Frame(root,bg="#eee5de")
l1=Label(middleFrame,text='Name : ',bg='#eee5de',fg='black',font=("Comic Sans MS", 15)).grid(row=1,pady=20,sticky=E)
l2=Label(middleFrame,text='Percentage : ',bg='#eee5de',fg='black',font=('Comic Sans MS',15)).grid(row=2,pady=15,sticky=E)
l3=Label(middleFrame,text='Backlogs : ',fg='black',bg='#eee5de',font=('Comic Sans MS',15)).grid(row=3,pady=15,sticky=E)
l4=Label(middleFrame,text='Internship : ',fg='black',bg='#eee5de',font=('Comic Sans MS',15)).grid(row=4,pady=15,sticky=E)
l5=Label(middleFrame,text='FirstRound : ',fg='black',bg='#eee5de',font=('Comic Sans MS',15)).grid(row=5,pady=15,sticky=E)
l5=Label(middleFrame,text='Communication : ',fg='black',bg='#eee5de',font=('Comic Sans MS',15)).grid(row=6,pady=15,padx=10,sticky=E)

E1,E2,E3,E4,E5,E6=StringVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()

e1=Entry(middleFrame,font=('',13),textvariable=E1,width = 16).grid(row=1,column=1)
e2=Entry(middleFrame,font=('',13),textvariable=E2,width = 16).grid(row=2,column=1)
e3=Entry(middleFrame,font=('',13),textvariable=E3,width = 16).grid(row=3,column=1)
e4=Entry(middleFrame,font=('',13),textvariable=E4,width = 16).grid(row=4,column=1)
e5=Entry(middleFrame,font=('',13),textvariable=E5,width = 16).grid(row=5,column=1)
e6=Entry(middleFrame,font=('',13),textvariable=E6,width = 16).grid(row=6,column=1)



b1=Button(middleFrame,text='Logistic',width=11,command=logistic,font=('MS Serif',13),bg='#2f4f4f',fg='#fff',bd='10').grid(row=2,column=2,ipadx=5,ipady=4)
b2=Button(middleFrame,text='Decision Tree',width=11,command=decision,font=('MS Serif',13),bg='#2f4f4f',fg='#fff',bd='10').grid(row=3,column=2,ipadx=5,ipady=4)
b3=Button(middleFrame,text='Random Forest',width=11,command=randomfor,font=('MS Serif',13),bg='#2f4f4f',fg='#fff',bd='10').grid(row=4,column=2,ipadx=5,ipady=4)
b4=Button(middleFrame,text='SVM',width=11,command=svm,font=('MS Serif',13),bg='#2f4f4f',fg='#fff',bd='10').grid(row=5,column=2,ipadx=5,ipady=4)




L11=Label(middleFrame,font=('',12),height=3,width=13,bg='#fff',borderwidth=2,relief='solid')
L11.grid(row=2,column=5,padx=15)
L12=Label(middleFrame,font=('',12),height=3,width=13,bg='#fff',borderwidth=2,relief='solid')
L12.grid(row=3,column=5,padx=15)
L13=Label(middleFrame,font=('',12),height=3,width=13,bg='#fff',borderwidth=2,relief='solid')
L13.grid(row=4,column=5,padx=15)
L14=Label(middleFrame,font=('',12),height=3,width=13,bg='#fff',borderwidth=2,relief='solid')
L14.grid(row=5,column=5,padx=15)
L15=Label(middleFrame,font=('',12),height=3,width=25,bg='#fff',borderwidth=2,relief='solid')
L15.grid(row=11,column=2,pady=10)
BF=Button(middleFrame,text='Final Result',width=25,font=('MS Serif',15),bg='#2f4f4f',fg='#fff',command=final,bd='10').grid(row=10,column=1,columnspan=5,ipady=5,pady=20)
middleFrame.pack(pady=20,padx=20)
root.mainloop()