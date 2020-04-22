from tkinter import*

def Calculate(event):
    height = float(textBox.get())/100
    weight = float(textBox2.get())

    labelResult.configure(text=check(weight/height**2))
    labelResult2.configure(text=weight/height**2)


def check(n):
    if n >=30:
        return 'อ้วนมาก'
    elif n >=25:
        return 'อ้วน'
    elif  n>=23:
        return 'น้ำหนักเกิน'
    elif n>=18.6:
        return 'น้ำหนักปกติ'
    else:
        return 'ผอมเกินไป'

main = Tk()
labelHeight = Label(main,text='ส่วนสูง (cm.)').grid(row=0,column=0)
textBox = Entry(main)
textBox.grid(row=0,column=1)

labelWeight = Label(main,text='น้ำหนัก (kg.)').grid(row=1,column=0)
textBox2 = Entry(main)
textBox2.grid(row=1,column=1)

button = Button(main,text='คำนาณ')
button.grid(row=2,column=0)
button.bind('<Button-1>',Calculate)

labelResult = Label(main,text='ผลลัพธ์',)
labelResult.grid(row=2,column=1)

labelResult2 = Label(main,text='BMI',)
labelResult2.grid(row=3,column=1)


main.mainloop()