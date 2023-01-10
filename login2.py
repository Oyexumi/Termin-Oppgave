from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql
#GUI del

#Funksjoner
def user_enter(event): #Fjerner brukernavn teksten i feltet
    if BrukernavnFyll.get()=='Brukernavn':
        BrukernavnFyll.delete(0,END)

def pass_enter(event): #Fjerner passord teksten i feltet
    if PassordFyll.get()=='Passord':
        PassordFyll.delete(0,END)
def email_enter(event): #Fjerner passord teksten i feltet
    if emailFyll.get()=='Email':
        emailFyll.delete(0,END)
def signup_page(): #Om du trykker på lag bruker så lukker du login2 og kommer til login2
    login_vindu.destroy()
    import lagbruker
def spill_enter(): #Om du trykker på lag bruker så lukker du login2 og kommer til login2
    login_vindu.destroy()
    import spill.py
login_vindu=Tk()
login_vindu.resizable(FALSE,FALSE) #Gjør at appen ikke kan endre størrelse
login_vindu.title('Login Side')
bgImage=ImageTk.PhotoImage(file='bg.jpg') #Bakgrunnsbildet
bgLabel=Label(login_vindu,image=bgImage)
bgLabel.grid()

frame=Frame(login_vindu,width=50,height=20,bg='white')
frame.place(x=554,y=100)


heading=Label(frame,text='Log inn ',font=('Microsoft Yahei UI Light',18,'bold'),bg='white',
fg='firebrick1')
heading.place(x=80,y=200)
heading.grid(row=0,column=0,padx=10,pady=10)
#Det
emailBox=Label(frame,text='Email',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
emailBox.grid(row=1,column=0,sticky='w',padx=25)

emailFyll=Entry(frame,width=25,font=('Microsot Yahei UI Light',10,'bold'),fg='white', bg='firebrick1')
emailFyll.grid(row=2,column=0,sticky='w',padx=25)
emailFyll.insert(0, 'Email')
emailFyll.bind('<FocusIn>', email_enter)

BrukernavnBox=Label(frame,text='Brukernavn',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
BrukernavnBox.grid(row=3,column=0,sticky='w',padx=25,pady=(12,0))

BrukernavnFyll=Entry(frame,width=25,font=('Microsot Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
BrukernavnFyll.grid(row=4,column=0,sticky='w',padx=25)
BrukernavnFyll.insert(0, 'Brukernavn')
BrukernavnFyll.bind('<FocusIn>', user_enter)

PassordBox=Label(frame,text='Passord',
font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
PassordBox.grid(row=5,column=0,sticky='w',padx=25,pady=(12,0))

PassordFyll=Entry(frame,width=25,font=('Microsot Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
PassordFyll.grid(row=6,column=0,sticky='w',padx=25)
PassordFyll.insert(0, 'Passord')
PassordFyll.bind('<FocusIn>', pass_enter)

#Lag Bruker
login=Button(frame,text='Log inn',bd=0,bg='firebrick1',activebackground='firebrick1',activeforeground='white',
                    cursor='hand2',font=('Microsoft Yahei UI Light',17,'bold'),width=17,)
login.grid(row=9,column=0,sticky='w',padx=25,pady=25)

signup=Button(frame,text='Oprett ny bruker',bd=0,bg='firebrick1',activebackground='firebrick1',activeforeground='white',
                    cursor='hand2',font=('Microsoft Yahei UI Light',14,'bold'),width=17,command=signup_page)
signup.grid(row=11,column=0,sticky='w',padx=40,pady=25)

Spill=Button(frame,text='Hopp Over',bd=0,bg='firebrick1',activebackground='firebrick1',activeforeground='white',
                    cursor='hand2',font=('Microsoft Yahei UI Light',14,'bold'),width=10,command=spill_enter)
Spill.grid(row=12,column=0,sticky='w',padx=40,pady=10)

login_vindu.mainloop() #loopen lar programmet kjøre