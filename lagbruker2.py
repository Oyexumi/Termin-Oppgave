from tkinter import *
from PIL import ImageTk

lagbruker_window=Tk()
lagbruker_window.title('Oprett Bruker') #Applikasjons Tittel
lagbruker_window.resizable(False,False) #Lar dem ikke endre på applikasjon størrelse
background=ImageTk.PhotoImage(file='bg.jpg')
#GUi 

bgLabel=Label(lagbruker_window,image=background)
bgLabel.grid()

frame=Frame(lagbruker_window,bg='white')
frame.place(x=554,y=100)

heading=Label(frame,text='OPPRETT EN BRUKER',font=('Microsoft Yahei UI Light',20,'bold'),bg='white',fg='firebrick')
heading.grid(row=0,column=0,padx=4,pady=2)

heading.place(x=400,y=200)
