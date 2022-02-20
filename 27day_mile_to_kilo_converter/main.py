from tkinter import *

def action():
    mile = float(entry.get())
    kil = round((mile) * 1.609)
    result.config(text=f"{kil}km")

window = Tk()
window.title("Mile to Km Converter / 마일 > 킬로미터 변환기")
window.config(padx=20, pady=20)

males = Label(text="Miles")
males.grid(column=2, row=0)

km = Label(text="KM")
km.grid(column=2, row=1)

equal = Label(text="is equal to")
equal.grid(column=0, row=1)

button = Button(text="Calculate", command=action)
button.grid(column=1, row=2)

entry = Entry(width=7)
entry.grid(column=1, row=0)

result = Label(text="0")
result.grid(column=1, row=1)

window.mainloop()
