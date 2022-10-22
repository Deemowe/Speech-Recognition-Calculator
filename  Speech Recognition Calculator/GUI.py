from tkinter import*
#import PyAudio
from SR_DB import val

me=Tk()
me.geometry("354x460")
me.title("CALCULATOR")
melabel = Label(me,text="CALCULATOR",bg='White',font=("Times",30,'bold'))
melabel.pack(side=TOP)
me.config(background='Dark gray')

def printSomething():

    me.wm_attributes('-transparentcolor', '#ab23ff')
    label = Label(me, text= val,font=("Courier New",12,'bold'),bg='powder blue')
    # this creates x as a new label to the GUI
    label.pack()
    label.place(x=60,y=61)



class Image:
    def __init__(self, path):
        self.path = path

    def creaticon(self):
        p1 = PhotoImage(file= self.path)
        # Icon set for program window
        me.iconphoto(False, p1)
        # Button creation



icon = Image("1280px-Qassim_University_logo.svg.png")
icon.creaticon()



print('= ',val)

metext=Entry(me,font=("Courier New",12,'bold'),width=25,bd=10,bg='powder blue')
metext.pack()

but1=Button(me,padx=14,pady=14,bd=4,bg='white',text="1",font=("Courier New",16,'bold'))
but1.place(x=10,y=100)

but2=Button(me,padx=14,pady=14,bd=4,bg='white',text="2",font=("Courier New",16,'bold'))
but2.place(x=10,y=170)

but3=Button(me,padx=14,pady=14,bd=4,bg='white',text="3",font=("Courier New",16,'bold'))
but3.place(x=10,y=240)

but4=Button(me,padx=14,pady=14,bd=4,bg='white',text="4",font=("Courier New",16,'bold'))
but4.place(x=75,y=100)

but5=Button(me,padx=14,pady=14,bd=4,bg='white',text="5",font=("Courier New",16,'bold'))
but5.place(x=75,y=170)

but6=Button(me,padx=14,pady=14,bd=4,bg='white',text="6",font=("Courier New",16,'bold'))
but6.place(x=75,y=240)

but7=Button(me,padx=14,pady=14,bd=4,bg='white',text="7",font=("Courier New",16,'bold'))
but7.place(x=140,y=100)

but8=Button(me,padx=14,pady=14,bd=4,bg='white',text="8",font=("Courier New",16,'bold'))
but8.place(x=140,y=170)

but9=Button(me,padx=14,pady=14,bd=4,bg='white',text="9",font=("Courier New",16,'bold'))
but9.place(x=140,y=240)

but0=Button(me,padx=14,pady=14,bd=4,bg='white',text="0",font=("Courier New",16,'bold'))
but0.place(x=10,y=310)

butdot=Button(me,padx=47,pady=14,bd=4,bg='white',text=".",font=("Courier New",16,'bold'))
butdot.place(x=75,y=310)

butpl=Button(me,padx=14,pady=14,bd=4,bg='white',text="+",font=("Courier New",16,'bold'))
butpl.place(x=205,y=100)

butsub=Button(me,padx=14,pady=14,bd=4,bg='white',text="-",font=("Courier New",16,'bold'))
butsub.place(x=205,y=170)

butml=Button(me,padx=14,pady=14,bd=4,bg='white',text="*",font=("Courier New",16,'bold'))
butml.place(x=205,y=240)

butdiv=Button(me,padx=14,pady=14,bd=4,bg='white',text="/",font=("Courier New",16,'bold'))
butdiv.place(x=205,y=310)

butclear=Button(me,padx=14,pady=119,bd=4,bg='white',text="CE",font=("Courier New",16,'bold'))
butclear.place(x=270,y=100)

butequal=Button(me,padx=150,pady=14,bd=4,bg='white',command=printSomething,text="=",font=("Courier New",16,'bold'))
butequal.place(x=10,y=380)
me.mainloop()
