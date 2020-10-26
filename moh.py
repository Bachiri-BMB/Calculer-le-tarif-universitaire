from tkinter import *
import sqlite3

window=Tk()
window.title('My application ')
window.geometry('1100x500')
window.config(background=('#5596A4'))

def action():

    x1 = float(entry_1.get())
    x2 = float(entry_2.get())
    x3 = float(entry_3.get())
    x4 = float(entry_4.get())
    x5 = float(entry_5.get())
    x = float(entry_6.get())
    x7 = float(entry_7.get())
    t1 = float(entry_td1.get())
    t2 = float(entry_td2.get())
    t3 = float(entry_td3.get())
    t4 = float(entry_td4.get())
    t5 = float(entry_td5.get())
    t = float(entry_td6.get())
    t7=float(entry_td7.get())

    c1 = int(entry_C1.get())
    c2 = int(entry_C2.get())
    c3 = int(entry_C3.get())
    c4 = int(entry_C4.get())
    c5 = int(entry_C5.get())
    c6 = int(entry_C6.get())
    c7 = int(entry_C7.get())

    p1 = int(entry_p.get())
    p2 = int(entry_p2.get())
    s1 = p1 / 100
    s2 = p2 / 100

    a = (x1 * s2) + (t1 * s1)
    a = a * c1
    b = (x2 * s2) + (t2 * s1)
    b = b * c2
    c = (x3 * s2) + (t3 * s1)
    c = c * c3
    d = (x4 * s2) + (t4 * s1)
    d = d * c4
    e = (x5 * s2) + (t5 * s1)
    e = e * c5
    f = (x * s2) + (t * s1)
    f = f * c6
    g = (x7*s2) + (t7 * s1)
    g = g*c7
    w = (c1+c2+c3+c4+c5+c6+c7)
    moy = (a+b+c+d+e+f+g) / w
    string_to_display=(str(moy))
    var_1.set(string_to_display)

    if moy>10:

      fen = Tk()
      fen.title('result')
      fen.config(background='#FF6D6D')
      fen.geometry('300x300')
      m=str(entry_10.get())
      label_t=Label(fen,text= '      الف مبروك\n  '+ m ,fg='Black',font=44  )
      label_t.place(x=150, y=150)
      entry_b=Entry(fen,textvariable=var_1,font=22)
      entry_b.place(x=150,y=190)


    else:


        fenetre = Tk()
        fenetre.config(background='#FF7B3D')
        fenetre.geometry('300x300')
        label_te = Label(fenetre, text='Im sorry  \n  '  , font=100)
        label_te.pack()


def somthing():
    exit()




var_1 = StringVar()



label_text = Label(window, text='bienvenue sur application ', fg='BLack', bg='#5596A4', font=33)
# Note EXAMEN
label_text.pack()
lable_t = Label(window, text='please enter your note examen : ',bg='#5596A4')
lable_t.place(x=300, y=70)
entry_1 = Entry(window, font=22)
entry_1.place(x=300, y=100)
entry_2 = Entry(window, font=22)
entry_2.place(x=300, y=130)
entry_3 = Entry(window, font=22)
entry_3.place(x=300, y=160)
entry_4 = Entry(window, font=22)
entry_4.place(x=300, y=190)
entry_5 = Entry(window, font=22)
entry_5.place(x=300, y=220)
entry_6 = Entry(window, font=22)
entry_6.place(x=300, y=250)
entry_7 = Entry(window, font=22)
entry_7.place(x=300, y=280)
# TD NOTE:
label = Label(window, text='Enter coffesion :',bg='#5596A4')
label.place(x=900, y=70)
entry_C1 = Entry(window, font=22)
entry_C1.place(x=900, y=100)
entry_C2 = Entry(window, font=22)
entry_C2.place(x=900, y=130)
entry_C3 = Entry(window, font=22)
entry_C3.place(x=900, y=160)
entry_C4 = Entry(window, font=22)
entry_C4.place(x=900, y=190)
entry_C5 = Entry(window, font=22)
entry_C5.place(x=900, y=220)
entry_C6 = Entry(window, font=22)
entry_C6.place(x=900, y=250)
entry_C7 = Entry(window, font=22)
entry_C7.place(x=900, y=280)
# coffision:
label = Label(window, text='Enter you note td  :',bg='#5596A4')
label.place(x=600, y=70)
entry_td1 = Entry(window, font=22)
entry_td1.place(x=600, y=100)
entry_td2 = Entry(window, font=22)
entry_td2.place(x=600, y=130)
entry_td3 = Entry(window, font=22)
entry_td3.place(x=600, y=160)
entry_td4 = Entry(window, font=22)
entry_td4.place(x=600, y=190)
entry_td5 = Entry(window, font=22)
entry_td5.place(x=600, y=220)
entry_td6 = Entry(window, font=22)
entry_td6.place(x=600, y=250)
entry_td7 = Entry(window, font=22)
entry_td7.place(x=600, y=280)
# purcentage de Td et examen:
label = Label(window, text='Enter your porcentage de TD :', bg='#5596A4')
label.place(x=700, y=15)
entry_p = Entry(window, font=12)
entry_p.place(x=880, y=15)
label_1 = Label(window, text='pourcentage de examen :', bg='#5596A4')
label_1.place(x=700, y=40)
entry_p2 = Entry(window, font=12)
entry_p2.place(x=880, y=40)
button = Button(window, text='moyenne', bg='Black',fg='white' ,command=action)
button.place(x=300, y=450)
button_2 = Button(window, text='exit', font=55, bg='Black',fg='white', command=somthing)
button_2.place(x=690, y=450)
label_2 = Label(window, text='la moyenne est :', bg='#5596A4')
label_2.place(x=600, y=400)
###### affectation
entry = Entry(window, font=22, textvariable=var_1, bg='Red')
entry.place(x=700, y=400)



label_a=Label(window,text=':  حول البرنامج  ',bg='Black',fg='white')
label_a.place(x=160,y=40)
label_a=Label(window,text=' برنامج لحساب معدل الطالب الجامعي  ',bg='#5596A4',fg='Black')
label_a.place(x=40,y=100)
label_a=Label(window,text='المطور  : بشيري محمد البشير ' ,bg='#5596A4',fg='Black')
label_a.place(x=40,y=140)

entry_10=Entry(window)
entry_10.place(x=170,y=400)

label_a=Label(window ,text='Enter your name :',bg='Black',fg='white')
label_a.place(x=60,y=400)

window.mainloop()




