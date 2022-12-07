from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql


def login_page():
    lagbruker_window.destroy()
    import login2

def connect_database():
    if emailFyll.get()=='' or BrukernavnFyll.get()=='' or PassordFyll.get()=='':
        messagebox.showerror('Error', 'All feltene må bli fyllt inn')
    elif PassordFyll.get() != Pass_BK_Fyll.get():
        messagebox.showerror('Error', 'Passordene matcher ikke')
lagbruker_window=Tk()
lagbruker_window.title('Oprett Bruker') #Applikasjons Tittel
lagbruker_window.resizable(False,False) #Lar dem ikke endre på applikasjon størrelse
background=ImageTk.PhotoImage(file='bg.jpg')
#GUi 

bgLabel=Label(lagbruker_window,image=background)
bgLabel.grid()

frame=Frame(lagbruker_window,width=50,height=20,bg='white')
frame.place(x=554,y=100)

heading=Label(frame,text='Opprett Bruker',font=('Microsoft Yahei UI Light',18,'bold'),bg='white',
fg='firebrick1')
heading.place(x=80,y=200)
heading.grid(row=0,column=0,padx=10,pady=10)

emailBox=Label(frame,text='Email',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
emailBox.grid(row=1,column=0,sticky='w',padx=25)

emailFyll=Entry(frame,width=25,font=('Microsot Yahei UI Light',10,'bold'),fg='white', bg='firebrick1')
emailFyll.grid(row=2,column=0,sticky='w',padx=25)

BrukernavnBox=Label(frame,text='Brukernavn',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
BrukernavnBox.grid(row=3,column=0,sticky='w',padx=25,pady=(12,0))

BrukernavnFyll=Entry(frame,width=25,font=('Microsot Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
BrukernavnFyll.grid(row=4,column=0,sticky='w',padx=25)

PassordBox=Label(frame,text='Passord',
font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
PassordBox.grid(row=5,column=0,sticky='w',padx=25,pady=(12,0))

PassordFyll=Entry(frame,width=25,font=('Microsot Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
PassordFyll.grid(row=6,column=0,sticky='w',padx=25)


Pass_BK_Box=Label(frame,text='Bekreft Passord',
font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
Pass_BK_Box.grid(row=7,column=0,sticky='w',padx=25,pady=(12,0))

Pass_BK_Fyll=Entry(frame,width=25,font=('Microsot Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
Pass_BK_Fyll.grid(row=8,column=0,sticky='w',padx=25)

LagBruker=Button(frame,text='Lag Bruker',bd=0,bg='firebrick1',activebackground='firebrick1',activeforeground='white',
                    cursor='hand2',font=('Microsoft Yahei UI Light',17,'bold'),width=17,command=connect_database)
LagBruker.grid(row=9,column=0,sticky='w',padx=25,pady=25)
lagbruker_window.mainloop() #loopen lar programmet kjøre