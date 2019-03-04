from tkinter import *
import random
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
                      '((8+82%60)%30)+1 = {}'.format(((8 + 82 % 60) % 30) + 1),
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


def save_to_file_2(event):
    with open("file2.txt", 'w') as f:
        f.write(str(event))


def save_to_file_3(event):
    with open("file3.txt", 'w') as f:
        f.write(str(event))


def save_to_file_4(event):
    with open("file4.txt", 'w') as f:
        f.write(str(event))


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
                       '2) (B & A) = {f2}\n'
                       '3) (C | B) = {f3}\n'
                       '4) (A - B) | (B & A) = {f4}\n'
                       '5) ((A - B) | (B & A)) - (C | B)  = {rez}\n\n'
                       'Відповідь: {rez}'
              .format(
                    f1=(A - B),
                    f2=(B & A),
                    f3=(C | B),
                    f4=(A - B) | (B & A),
                    rez=zad_alg.func_1_full(A, B, C)),
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
                      'D = ((A - B) | (B & A)) - (C | B) = {}\n'.format(zad_alg.func_1_full(A, B, C)),
          font='Arial 14 bold').grid(column=0, row=0, sticky=W, columnspan=2)

    Button(slave, text="Показати розв'язок", font="Arial 12",
           command=show).grid(column=0, row=3)

    but = Button(slave, text='Зберегти в файл', font='Arial 12')

    but.grid(column=1, row=3)

    but.bind("<Button-1>", save_to_file_2(zad_alg.func_1_full(A, B, C)))
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
                       '1) (С | B) = {f1}\n'
                       '2) A - (C | B)  = {rez1}\n\n'
                       'Відповідь: {rez1}'
              .format(
                    f1=(C | B),
                    rez1=zad_alg.func_1_small(A, B, C)),
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
                      'D = (A - (C | B)) = {}\n'.format(zad_alg.func_1_small(A, B, C)),
          font='Arial 14 bold').grid(column=0, row=0, sticky=W, columnspan=2)

    Button(slave, text="Показати розв'язок", font="Arial 12",
           command=show).grid(column=0, row=3)

    but = Button(slave, text='Зберегти в файл', font='Arial 12')
    but.grid(column=1, row=3)
    but.bind("<Button-1>", save_to_file_3(zad_alg.func_1_small(A, B, C)))
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

    def show():
        lf = LabelFrame(slave_2, text="Розв'язок", font='Arial 12')
        lf.grid(column=0, row=7, sticky=W, columnspan=4)
        Label(lf, text='Z = {d}\n'.format(d=zad_alg.func_2_my(A, B)),
              font='Arial 14', justify=LEFT, width=87, height=5).grid(column=0, row=7, sticky=W, columnspan=4)

    def but_disable(event):
        print(event)
        but['text'] = 'Збережено'
        but['state'] = DISABLED

    Label(slave_2, text='Множина:\n''X = {A}\n''Y = {B}'.format(A=A, B=B), font='Arial 14 bold') \
        .grid(column=0, row=0, sticky=W, columnspan=2)

    Button(slave_2, text="Показати розв'язок", font="Arial 12", command=show).grid(column=0, row=3)
    but = Button(slave_2, text='Зберегти в файл', font='Arial 12', command=save_to_file_4(zad_alg.func_2_my(A, B)))
    but.grid(column=1, row=3)
    but.bind("<Button-1>", but_disable)

    photo = PhotoImage(file="photo_2.png")
    photo_but = Button(slave_2, activebackground="green")
    photo_but.config(image=photo, width="700", height="90")
    photo_but.grid(column=0, row=5, columnspan=2)
    slave_2.mainloop()


def window5():
    slave = Toplevel(root)
    slave.title('Результати')
    slave.grab_set()
    slave.focus_set()

    f2 = open('file2.txt', 'r')
    f3 = open('file3.txt', 'r')
    f4 = open('file4.txt', 'r')

    d1 = f2.read()
    d2 = f3.read()
    z1 = f4.read()
    z2 = str(A - B)

    rez1 = 'Результати сходяться' if d1 == d2 else 'Помилка в обчисленні'
    rez2 = 'Результати сходяться' if z1 == z2 else 'Помилка в обчисленні'

    def but():
        Label(slave, text=rez1, font="Arial 12", fg='green').grid(column=0, row=3, sticky=W, columnspan=2)
        Label(slave, text=rez2, font="Arial 12", fg='green').grid(column=0, row=9, sticky=W, columnspan=2)

    lf1 = LabelFrame(slave, text='Множина D', font='Arial 12')
    lf2 = LabelFrame(slave, text='Множина Z', font='Arial 12')
    lf1.grid(column=0, row=1, sticky=W, columnspan=2, rowspan=2)
    lf2.grid(column=0, row=7, sticky=W, columnspan=2, rowspan=2)

    Label(slave, text='Результати обчислень', font='Arial 14 bold').grid(column=0, row=0, columnspan=2)
    Label(lf1, text='D(заданий алгоритм) = A & (A - (A - B))) | C =\n\t\t= {}'.format(d1),
          font="Arial 14", justify=LEFT)\
        .grid(column=0, row=1, sticky=W, columnspan=2)
    Label(lf1, text='D(спрощений алгоритм) = (A & B) | C = {}'.format(d2), font="Arial 14", justify=LEFT)\
        .grid(column=0, row=2, sticky=W, columnspan=2)
    Label(slave, text='\t').grid(column=0, row=6, sticky=W, columnspan=2)

    Label(lf2, text='Z(авторський алгоритм) = {}'.format(z1), font="Arial 14", justify=LEFT)\
        .grid(column=0, row=7, sticky=W, columnspan=2)
    Label(lf2, text='Z(алгоритм Python (A & B)) = {}'.format(z2), font="Arial 14", justify=LEFT)\
        .grid(column=0, row=8, sticky=W, columnspan=2)
    Label(slave, text='   ').grid(column=2, row=2, rowspan=2)
    Label(slave, text='\t').grid(column=0, row=11)

    Button(slave, text='Порівняти результати', font="Arial 12", command=but).grid(column=0, row=12)


root = Tk()
root.title('Задати множини')
root.minsize(680, 450)

# menubar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Window_2", command=window2)
filemenu.add_command(label="Window_3", command=window3)
filemenu.add_command(label="Window_4", command=window4)
filemenu.add_command(label="Window_5", command=window5)

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

lenA = Entry(root, width=10, bd=3, state=DISABLED)
lenA.grid(column=4, row=3, sticky=W)
lenB = Entry(root, width=10, bd=3, state=DISABLED)
lenB.grid(column=4, row=4, sticky=W)
lenC = Entry(root, width=10, bd=3, state=DISABLED)
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
Button(root, text='5 віджет', font='Arial 20', command=window5).grid(column=3, row=13)

root.mainloop()
