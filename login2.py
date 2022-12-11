from tkinter import *
from PIL import ImageTk
#GUI del

#Funksjoner
def user_enter(event): #Fjerner brukernavn teksten i feltet
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def pass_enter(event): #Fjerner passord teksten i feltet
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)
def signup_page():
    login_vindu.destroy()
    import lagbruker2

login_vindu=Tk()
login_vindu.geometry('900x600+50+50') #Størrelse på vinduet
login_vindu.resizable(0,0)
login_vindu.title('Login Side')
bgImage=ImageTk.PhotoImage(file='vista.jpg')

bgLabel=Label(login_vindu,image=bgImage)
bgLabel.place(x=0, y=0)

heading=Label(login_vindu,text='User Login',font=('Microsoft Yahei UI Light',21,'bold'),bg='white')
heading.place(x=400,y=200)

usernameEntry=Entry(login_vindu, width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,)
usernameEntry.place(x=400,y=280)
usernameEntry.insert(0, 'Username')

usernameEntry.bind('<FocusIn>', user_enter)

frame1=Frame(login_vindu,width=227,height=2,bg='black')
frame1.place(x=400,y=302)


passwordEntry=Entry(login_vindu, width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,)
passwordEntry.place(x=400,y=340)
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

