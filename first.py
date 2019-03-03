from tkinter import *
import random
import pickle
import zadanyy_algorytm as zad_alg


def student():
    slave = Toplevel(root)
    slave.grab_set()
    slave.title("student")
    slave.focus_set()
    slave.minsize(200, 80)
    slave.maxsize(200, 80)
    Label(slave, text='Данилюк Денис\n'
                      'група ІВ-82\n'
                      'варіант 2\n'
                      '((8+82%60)%30)+1',
          justify=LEFT, font="Arial 14").pack(fill='both')


def from_string_to_set(x):
    x = x.replace(',', ' ')
    x = x.replace(';', ' ')
    x = x.replace(':', ' ')
    x = x.replace('.', ' ')
    x = list(x.split(' '))
    for i in range(x.count('')):
        x.remove('')
    x = {int(i) for i in x}
    return x


def gener_vyp_set(l):
    if entU_do.get() == '':
        do = 0
    else:
        do = int(entU_do.get())
    if entU_vid.get() == '':
        vid = 0
    else:
        vid = int(entU_vid.get())
    s = set()
    for i in range(l):
        s.add(random.randint(vid, do))
    while len(s) < l:
        s.add(random.randint(vid, do))
    return s


def generabc():
    global A, B, C, U
    v = var.get()
    if v == 0:
        if entA.get() == '':
            A = set()
        else:
            A = from_string_to_set(entA.get())

        if entB.get() == '':
            B = set()
        else:
            B = from_string_to_set(entB.get())

        if entC.get() == '':
            C = set()
        else:
            C = from_string_to_set(entC.get())

    if v == 1:
        if lenA.get() == '':
            A = set()
        else:
            A = gener_vyp_set(int(lenA.get()))

        if lenB.get() == '':
            B = set()
        else:
            B = gener_vyp_set(int(lenB.get()))

        if lenC.get() == '':
            C = set()
        else:
            C = gener_vyp_set(int(lenC.get()))

    if entU_do.get() == '':
        do = 0
    else:
        do = int(entU_do.get()) + 1

    if entU_vid.get() == '':
        vid = 0
    else:
        vid = int(entU_vid.get())

    U = set(range(vid, do))
    label_vyvid.configure(text='A = {}\n'
                               'B = {}\n'
                               'C = {}\n'
                               'U = {}'.format(A, B, C, U))


def gener_f(x):
    le = len(x)
    s = set()
    s.add(min(x))
    s.add(max(x))

    for i in range(le - 2):
        s.add(random.randint(min(x), max(x)))
    while len(s) < le:
        s.add(random.randint(min(x), max(x)))
    return s


def vruchnu():
    global A, B, C
    entA['state'] = NORMAL
    entB['state'] = NORMAL
    entC['state'] = NORMAL
    lenA['state'] = DISABLED
    lenB['state'] = DISABLED
    lenC['state'] = DISABLED


def vypadkovo():
    global A, B, C
    entA['state'] = DISABLED
    entB['state'] = DISABLED
    entC['state'] = DISABLED
    lenA['state'] = NORMAL
    lenB['state'] = NORMAL
    lenC['state'] = NORMAL


def save_to_file(x):
    f = open('Результат.txt', 'ab')
    pickle.dump(x, f)
    f.close()


def save_to_file_v2(x):
    f = open('Результат_2.txt', 'ab')
    # pickle.dump(x, f)
    f.write(x)
    f.close()


def window2():
    slave = Toplevel(root)
    slave.title('Обчислення заданого виразу')
    slave.grab_set()
    slave.focus_set()

    def show():
        lf = LabelFrame(slave, text="Розв'язок", font='Arial 12')
        lf.grid(column=0, row=5, columnspan=4)
        Label(lf, text='\n'
                       '1) (A - B) = {f1}\n'
                       '2) (A - (A - B)) = {f2}\n'
                       '3) (A & (A - (A - B))) = {f3}\n'
                       '4) (A & (A - (A - B))) | C  = {rez}\n\n'
                       'Відповідь: {rez}'
              .format(
                    f1=(A - B),
                    f2=(A - (A - B)),
                    f3=(A & (A - (A - B))),
                    rez=zad_alg.vyraz_1(A, B, C, U)),
              font='Arial 14', justify=LEFT).grid(column=0, row=5, sticky=W, columnspan=4)

    def but_disable(event):
        print(event)
        but['text'] = 'Збережено'
        but['state'] = DISABLED

    Label(slave, text='A = {}\n'
                      'B = {}\n'
                      'C = {}\n'.format(A, B, C),
          font="Arial 14", justify=LEFT).grid(column=0, row=1, sticky=W, columnspan=3)

    Label(slave, text='Заданий вираз:\n'
                      'D = (A & (A - (A - B)) | C) = {}\n'.format(zad_alg.vyraz_1(A, B, C, U)),
          font='Arial 14 bold').grid(column=0, row=0, sticky=W, columnspan=2)

    Button(slave, text="Показати розв'язок", font="Arial 12",
           command=show).grid(column=0, row=3)

    but = Button(slave, text='Зберегти в файл', font='Arial 12')
    but.grid(column=1, row=3)
    but.bind("<Button-1>", save_to_file(zad_alg.vyraz_1(A, B, C, U)))
    but.bind("<Button-1>", but_disable)

    photo = PhotoImage(file="photo.png")
    photo_but = Button(slave, activebackground="green")
    photo_but.config(image=photo, width="700", height="100")
    photo_but.grid(column=0, row=4, columnspan=2)
    slave.mainloop()


def window3():
    slave = Toplevel(root)
    slave.title('Обчислення заданого виразу')
    slave.grab_set()
    slave.focus_set()

    def show():
        lf = LabelFrame(slave, text="Розв'язок", font='Arial 12')
        lf.grid(column=0, row=5, columnspan=4)
        Label(lf, text='\n'
                       '1) (A - B) = {f1}\n'
                       '2) (A - (A - B)) = {f2}\n'
                       '3) (A & (A - (A - B))) = {f3}\n'
                       '4) (A & (A - (A - B))) | C  = {rez}\n\n'
                       'Відповідь: {rez}'
              .format(
                    f1=(A - B),
                    f2=(A - (A - B)),
                    f3=(A & (A - (A - B))),
                    rez=zad_alg.vyraz_1(A, B, C, U)),
              font='Arial 14', justify=LEFT).grid(column=0, row=5, sticky=W, columnspan=4)

    def but_disable(event):
        print(event)
        but['text'] = 'Збережено'
        but['state'] = DISABLED

    Label(slave, text='A = {}\n'
                      'B = {}\n'
                      'C = {}\n'.format(A, B, C),
          font="Arial 14", justify=LEFT).grid(column=0, row=1, sticky=W, columnspan=3)

    Label(slave, text='Заданий вираз:\n'
                      'D = (A & (A - (A - B)) | C) = {}\n'.format(zad_alg.vyraz_1(A, B, C, U)),
          font='Arial 14 bold').grid(column=0, row=0, sticky=W, columnspan=2)

    Button(slave, text="Показати розв'язок", font="Arial 12",
           command=show).grid(column=0, row=3)

    but = Button(slave, text='Зберегти в файл', font='Arial 12')
    but.grid(column=1, row=3)
    but.bind("<Button-1>", save_to_file(zad_alg.vyraz_1(A, B, C, U)))
    but.bind("<Button-1>", but_disable)

    photo = PhotoImage(file="photo.png")
    photo_but = Button(slave, activebackground="green")
    photo_but.config(image=photo, width="700", height="100")
    photo_but.grid(column=0, row=4, columnspan=2)
    slave.mainloop()


def window4():
    slave_2 = Toplevel(root)
    slave_2.title('Обчислення 2 виразу')
    slave_2.grab_set()
    slave_2.focus_set()
    global Dx, Fx
    Dx = zad_alg.vyraz_1(A, B, C, U)
    Fx = gener_f(zad_alg.vyraz_1(A, B, C, U))

    def show():
        lf = LabelFrame(slave_2, text="Генерування", font='Arial 12')
        lf.grid(column=0, row=6, sticky=W, columnspan=4)
        Label(lf, text='F = {d}\n'.format(d=Fx),
              font='Arial 14', justify=LEFT, width=75, height=5).grid(column=0, row=6, sticky=W, columnspan=4)

    def show_2():
        lf = LabelFrame(slave_2, text="Розв'язок", font='Arial 12')
        lf.grid(column=0, row=7, sticky=W, columnspan=4)
        Label(lf, text='X = {d}\n'.format(d=zad_alg.vyraz_2(Fx, Dx, U)),
              font='Arial 14', justify=LEFT, width=75, height=5).grid(column=0, row=7, sticky=W, columnspan=4)

    def but_disable(event):
        print(event)
        but['text'] = 'Збережено'
        but['state'] = DISABLED

    Label(slave_2, text='Множина:\n''D = {}'.format(Dx), font='Arial 14 bold') \
        .grid(column=0, row=0, sticky=W, columnspan=4)

    Button(slave_2, text="Генерувати F", font="Arial 12", command=show).grid(column=0, row=3)
    Button(slave_2, text="Показати розв'язок", font="Arial 12", command=show_2).grid(column=0, row=4)
    but = Button(slave_2, text='Зберегти в файл', font='Arial 12', command=save_to_file(zad_alg.vyraz_2(Fx, Dx, U)))
    but.grid(column=1, row=4)
    but.bind("<Button-1>", but_disable)

    photo = PhotoImage(file="photo_2_v2.png")
    photo_but = Button(slave_2, activebackground="green")
    photo_but.config(image=photo, width="250", height="60")
    photo_but.grid(column=0, row=5, columnspan=2)
    slave_2.mainloop()


root = Tk()
root.title('Задати множини')
root.minsize(680, 450)

# menubar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Window2", command=window2)
filemenu.add_command(label="Window_my", command=window3)
menubar.add_cascade(label="Windows", menu=filemenu)
root.config(menu=menubar)

var = IntVar()
var.set(0)
rad0 = Radiobutton(root, text="Вручну", variable=var, value=0, command=vruchnu)
rad1 = Radiobutton(root, text="Випадково", variable=var, value=1, command=vypadkovo)
rad0.grid(column=0, row=0, columnspan=2, sticky=W)
rad1.grid(column=0, row=1, columnspan=2, sticky=W)

Label(root, text='Задати множини вручну', font="Arial 14", width=20, height=2, justify=LEFT) \
    .grid(column=0, row=2, columnspan=3)

Label(root, text='A:').grid(column=0, row=3, sticky=E)
Label(root, text='B:').grid(column=0, row=4, sticky=E)
Label(root, text='C:').grid(column=0, row=5, sticky=E)

entA = Entry(root, width=29, bd=3, state=DISABLED)
entA.grid(column=1, row=3, sticky=W)
entB = Entry(root, width=29, bd=3, state=DISABLED)
entB.grid(column=1, row=4, sticky=W)
entC = Entry(root, width=29, bd=3, state=DISABLED)
entC.grid(column=1, row=5, sticky=W)

Label(root, text='Задати множини випадково', font="Arial 14", width=30, height=2, justify=LEFT) \
    .grid(column=3, row=2, columnspan=3)

Label(root, text='Потужність A:').grid(column=3, row=3, sticky=E)
Label(root, text='Потужність B:').grid(column=3, row=4, sticky=E)
Label(root, text='Потужність C:').grid(column=3, row=5, sticky=E)

lenA = Entry(root, width=10, bd=3, state=NORMAL)
lenA.grid(column=4, row=3, sticky=W)
lenB = Entry(root, width=10, bd=3, state=NORMAL)
lenB.grid(column=4, row=4, sticky=W)
lenC = Entry(root, width=10, bd=3, state=NORMAL)
lenC.grid(column=4, row=5, sticky=W)
Label(root, text='Задати універсальну множину', font="Arial 14", width=30, height=2, justify=LEFT) \
    .grid(column=0, row=6, columnspan=3)

Label(root, text='від').grid(column=0, row=7, sticky=E)
Label(root, text='до').grid(column=0, row=8, sticky=E)

entU_vid = Entry(root, width=10, bd=3)
entU_vid.grid(column=1, row=7, sticky=W)

entU_do = Entry(root, width=10, bd=3)
entU_do.grid(column=1, row=8, sticky=W)

A = set()
B = set()
C = set()
U = set()
but_OK = Button(root, text='Згенерувати множини', font='Arial 12', command=generabc)
but_OK.grid(column=1, row=9, columnspan=4)

open('Результат.txt', 'wb').close()

label_vyvid = Label(root, text='A = {}\n'
                               'B = {}\n'
                               'C = {}\n'
                               'U = {}'.format(A, B, C, U),
                    font="Arial 14", justify=LEFT)
label_vyvid.grid(column=1, row=11, columnspan=100, sticky=W)

but_student = Button(root, text='Студент', font='Arial 12',
                     command=student)
but_student.grid(column=5, row=0, sticky=E, rowspan=2, columnspan=2)

Button(root, text='2 віджет', font='Arial 20', command=window2).grid(column=1, row=13, sticky=W)
Button(root, text='3 віджет', font='Arial 20', command=window3).grid(column=1, row=13)
Button(root, text='4 віджет', font='Arial 20', command=window4).grid(column=1, row=13, sticky=E)
Button(root, text='5 віджет', font='Arial 20', command=window4).grid(column=3, row=13)

root.mainloop()
