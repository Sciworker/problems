"""import tkinter
def UpdateLists():
    global taskButtonsList
    for i in range(len(taskButtonsList)):
        taskButtonsList[i].place(x=0, y=130+40*i)
def AddButtonFunc():
    global taskButtonsList
    tempText = textFild.get("1.0", "end")
    temp = tkinter.Button(window, width= 70, height=2, text= tempText)
    temp.config(command= lambda: SelfDestruct(temp))
    taskButtonsList.append(temp)
    UpdateLists()
def SelfDestruct(_self):
    global taskButtonsList
    taskButtonsList.remove(_self)
    _self.destroy()
    UpdateLists()
global taskButtonsList
taskButtonsList=[]
window = tkinter.Tk()
window.geometry("500x500")
window.title("задачник")
textLabel = tkinter.Label(window, text="введите задачу")
textLabel.place(x=0, y=0)
textFild = tkinter.Text(window, width=62, height= 2)
textFild.place(x=0, y=25)
addButton = tkinter.Button(window, width= 70, height=2, text= "добавить задачу", command=AddButtonFunc)
addButton.place(x=0, y= 70)
listLabel = tkinter.Label(window, text="список задач")
listLabel.place(x=0, y=115)
window.mainloop()"""

"""ЗАДАЧА №579		
Модуль суммы
Дана последовательность целых чисел. 
Требуется найти подпоследовательность заданной последовательности с максимальным модулем суммы 
входящих в нее чисел. Напомним, что модуль целого числа x равняется x, если x ≥ 0 и -x, если x < 0."""

posled = int(input())
array = []
for i  in range(0, posled):
    array.append(int(input()))
sum_pol = 0
sum_otr = 0
mod=0
for i in range(0, len(array),1):
    if array[i] > 0:
        sum_pol = sum_pol+array[i] 
    if array[i] < 0:
        sum_otr = sum_otr+array[i] 
if abs(sum_otr) > abs(sum_pol):
    mod = (-1)
else:
    mod = 1
for i in range(0, len(array),1):
    if mod == 1:
        if array[i]>0:
            print(i)
    else:
        if array[i]<0:
            print(i)

