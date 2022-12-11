from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql
#GUI del

#Funksjoner
def user_enter(event): #Fjerner brukernavn teksten i feltet
    if usernameEntry.get()=='Brukernavn':
        usernameEntry.delete(0,END)

def pass_enter(event): #Fjerner passord teksten i feltet
    if passwordEntry.get()=='Passord':
        passwordEntry.delete(0,END)
def email_enter(event): #Fjerner passord teksten i feltet
    if emailFyll.get()=='Email':
        emailFyll.delete(0,END)
def signup_page(): #Om du trykker på lag bruker så lukker du login2 og kommer til login2
    login_vindu.destroy()
    import login2

login_vindu=Tk()
login_vindu.resizable(FALSE,FALSE)
login_vindu.title('Login Side')
bgImage=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(login_vindu,image=bgImage)
bgLabel.grid()

heading=Label(login_vindu,text='User Login',font=('Microsoft Yahei UI Light',21,'bold'),bg='white')
heading.place(x=400,y=200)

usernameEntry=Entry(login_vindu, width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,)
usernameEntry.place(x=400,y=280)
usernameEntry.insert(0, 'Username')

#Når du trykker på input feltet så fjerner den "USERNAME" teksten
usernameEntry.bind('<FocusIn>', user_enter)

frame1=Frame(login_vindu,width=227,height=2,bg='black')
frame1.place(x=400,y=302)


passwordEntry=Entry(login_vindu, width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,)
passwordEntry.place(x=400,y=340)

#Når du trykker på input feltet så fjerner den "Passord" teksten
passwordEntry.insert(0, 'Password')

passwordEntry.bind('<FocusIn>', pass_enter)

frame2=Frame(login_vindu,width=227,height=2,bg='black')
frame2.place(x=400,y=362)

loginLag=Button(login_vindu,text='Har du ikke bruker? Trykk Her',bd=0,bg='white',activebackground='white',
                    cursor='hand2',font=('Microsoft Yahei UI Light',8,'bold'))
loginLag.place(x=478,y=380)

loginButton=Button(login_vindu,text='Login',font=('Open Sans',16,'bold'),fg='indigo',bg='white')

loginButton.place(x=400,y=425)

ellerLabel=Label(login_vindu,text='------------------Eller------------------',font=('Open Sans',16,'bold'),fg='indigo',bg='white')
ellerLabel.place(x=400,y=501)

login_vindu.mainloop() #loopen lar programmet kjøre

