# Importing packages
from tkinter import *
import tkinter.messagebox
# Create the main application window
window = Tk()
window.title("To-Do List App")
# Frame widget to hold the listbox and the scrollbar
frame_task = Frame(window)
frame_task.pack()

# Listbox to display tasks
listbox_task = Listbox(frame_task, bg="black", fg="white", height=15, width=50, font="Helvetica")
listbox_task.pack(side=LEFT)
def add_task():
    task = entry_task.get()
    if task:
        listbox_task.insert(END, task)
        entry_task.delete(0, END)
    else:
        tkinter.messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = listbox_task.curselection()[0]
        listbox_task.delete(selected_task_index)
    except IndexError:
        tkinter.messagebox.showwarning("Warning", "Please select a task to delete.")
# Entry field for adding tasks
entry_task = Entry(window, width=50)
entry_task.pack()

# Add task button
button_add = Button(window, text="Add Task", command=add_task)
button_add.pack()

# Delete task button
button_delete = Button(window, text="Delete Task", command=delete_task)
button_delete.pack()
window.mainloop()
