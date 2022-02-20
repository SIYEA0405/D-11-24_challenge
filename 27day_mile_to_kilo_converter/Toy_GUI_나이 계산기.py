from tkinter import *
from datetime import datetime


def action():
    born_entry = int(was_born_entry.get())
    new_age = now.year - born_entry + 1
    age.config(text=new_age)


window = Tk()
window.title("나이 계산기")
window.config(padx=30, pady=30)

was_born = Label(text="당신의 출생년도는")
was_born.grid(column=0, row=0)

was_born_entry = Entry(width=7)
was_born_entry.grid(column=1, row=0)

n1 = Label(text="입니다.")
n1.grid(column=2, row=0)

button = Button(text="결과보기", command=action)
button.grid(column=1, row=1)

n2 = Label(text="당신은")
n2.grid(column=0, row=2)

now = datetime.now()
current_time = now.strftime('%Y-%m-%d')
today = Label(text=current_time)
today.grid(column=1, row=2)

n3 = Label(text="기준으로")
n3.grid(column=2, row=2)

age = Label(text="")
age.grid(column=1, row=3)

n4 = Label(text="살 입니다")
n4.grid(column=2, row=3)

window.mainloop()
