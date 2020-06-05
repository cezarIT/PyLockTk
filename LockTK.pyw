#\/\/Окно ввода пороля на модуле Tkinter на языке Python/\/\#
from  import *
#
window = Tk()
window.geometry('150x110+500+300')
window.title('ввод пороля')
#
data = IntVar()
data2 = StringVar()
code = 0000 # ваш пороль
#
def CodeProgramm():
	window.destroy()
	#место для кода(рекомендую основной код писать в другом файле и импортировать сюда)
def open():
	if data.get() == code:   
		CodeProgramm()
	else:
		data2.set('пороль не верный')
#
button = Button(window, text = 'ввести пороль', command = open)
entry = Entry(window, textvariable = data)
label = Label(window, textvariable = data2)
#
button.pack()
entry.pack()
label.pack()
window.mainloop()