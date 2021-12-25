from tkinter import *
# import routine_backend as backend
import routine_postgresdb as backend



def get_selected_row(event):
    global row_selected
    index=lb.curselection()[0]
    row_selected=lb.get(index)

    e1.delete(0,END)
    e1.insert(END,row_selected[1])
    e2.delete(0,END)
    e2.insert(END,row_selected[2])
    e3.delete(0,END)
    e3.insert(END,row_selected[3])
    e4.delete(0,END)
    e4.insert(END,row_selected[4])
    e5.delete(0,END)
    e5.insert(END,row_selected[5])
    e6.delete(0,END)
    e6.insert(END,row_selected[6])

# storing data in database
def add_command():
    backend.insert(date_text.get(),exercise_text.get(),diet_text.get(),wentcollege_text.get(),study_text.get(),code_text.get())

    lb.delete(0,END)
    lb.insert(END,(date_text.get(),exercise_text.get(),diet_text.get(),wentcollege_text.get(),study_text.get(),code_text.get()))


def delete_command():
    backend.delete(row_selected[0])
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)


def view_command():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)

    lb.delete(0,END)
    for row in backend.view():
        lb.insert(END,row)

def search_command():
    lb.delete(0,END)
    for row in backend.search(date_text.get(),exercise_text.get(),diet_text.get(),wentcollege_text.get(),study_text.get(),code_text.get()):
        lb.insert(END,row)

def update_command():
    backend.update(date_text.get(),exercise_text.get(),diet_text.get(),wentcollege_text.get(),study_text.get(),code_text.get(),row_selected[0])
    lb.delete(0,END)
    lb.insert(END,(row_selected[0],date_text.get(),exercise_text.get(),diet_text.get(),wentcollege_text.get(),study_text.get(),code_text.get()))


win=Tk()
win.title("ANITA'S ROUTINE ")
win.resizable(False,False)
win.geometry("700x450")

# labels
l1=Label(win,text='Date : ',padx=5,pady=2 )
l1.grid(row=0,column=0)
l2=Label(win,text='Workout : ',padx=5,pady=2 )
l2.grid(row=2,column=0)
l3=Label(win,text='Diet : ',padx=5,pady=2 )
l3.grid(row=4,column=0)
l4=Label(win,text='Went College : ',padx=5,pady=2 )
l4.grid(row=0,column=4)
l5=Label(win,text='Study : ',padx=5,pady=2 )
l5.grid(row=2,column=4)
l6=Label(win,text='Coding : ',padx=5,pady=2 )
l6.grid(row=4,column=4)

# entry box
date_text=StringVar()
e1=Entry(win,textvariable=date_text,width=30)
e1.grid(row=0,column=2)

exercise_text=StringVar()
e2=Entry(win,textvariable=exercise_text,width=30)
e2.grid(row=2,column=2)

diet_text=StringVar()
e3=Entry(win,textvariable=diet_text,width=30)
e3.grid(row=4,column=2)

wentcollege_text=StringVar()
e4=Entry(win,textvariable=wentcollege_text,width=30)
e4.grid(row=0,column=6)

study_text=StringVar()
e5=Entry(win,textvariable=study_text,width=30)
e5.grid(row=2,column=6)

code_text=StringVar()
e6=Entry(win,textvariable=code_text,width=30)
e6.grid(row=4,column=6)

lb=Listbox(win,width=60,height=20)
lb.grid(row=8,column=0,rowspan=10,columnspan=4,pady=30)

# scrollbar for listbox
sb=Scrollbar(win)
sb.grid(row=8,column=4,rowspan=10)
sb.config(command=lb.yview)

# listbox binding
lb.bind('<<ListboxSelect>>',get_selected_row)

# buttons for doing operations
b1=Button(win,text='CLOSE',width=15,pady=8,font='algerian 12 bold',bg='blue',relief='raised',fg='white',command=win.destroy)
b1.grid(row=8,column=6,pady=30)
b2=Button(win,text='SEARCH',width=15,pady=8,font='algerian 12 bold',bg='red',fg='yellow',relief='sunken',command=search_command)
b2.grid(row=11,column=6)
b3=Button(win,text='DELETE',width=15,pady=8,font='algerian 12 bold',bg='red',fg='yellow',relief='sunken',command=delete_command)
b3.grid(row=12,column=6)
b4=Button(win,text='UPDATE',width=15,pady=8,font='algerian 12 bold',bg='red',fg='yellow',relief='sunken',command=update_command)
b4.grid(row=13,column=6)
b5=Button(win,text='VIEW ALL',width=15,pady=8,font='algerian 12 bold',bg='red',fg='yellow',relief='sunken',command=view_command)
b5.grid(row=10,column=6)
b6=Button(win,text='ADD',width=15,pady=8,font='algerian 12 bold',bg='red',fg='yellow',relief='sunken',command=add_command)
b6.grid(row=9,column=6)


win.mainloop()