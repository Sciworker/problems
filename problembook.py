import tkinter
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
window.mainloop()

